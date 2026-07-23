import pygame
import math
import random
import numpy as np

# ---------- configuration ----------
WIDTH, HEIGHT = 900, 700
BACKGROUND = (8, 8, 16)
SHIP_COLOR = (120, 200, 255)
CELL_SIZE = 220
STARS_PER_CELL = 2
GEN_MARGIN = 1.6
MAX_CELLS = 1_000_000
MAX_STAR_PX = 5

# ---------- jednotky ----------
FPS = 60
YEARS_PER_SEC = 50.0 + 1e-4
DTAU = YEARS_PER_SEC / FPS
ENGINE_ACCEL = 0.02
ROTATE_SPEED = 0.04


def fmt_time(years):
    if years < 0:
        years = 0.0
    yrs = int(years)
    rem = (years - yrs) * 365.25
    d = int(rem)
    rem = (rem - d) * 24
    h = int(rem)
    rem = (rem - h) * 60
    m = int(rem)
    s = int((rem - m) * 60)
    return f"{yrs:,} let  {d:03d} d  {h:02d}:{m:02d}:{s:02d}"


# ---------- blackbody color + lookup table ----------
def _clamp(v):
    return max(0, min(255, int(v)))


def blackbody_color(temp):
    t = temp / 100.0
    r = 255 if t <= 66 else 329.698727446 * ((t - 60) ** -0.1332047592)
    if t <= 66:
        g = 99.4708025861 * math.log(t) - 161.1195681661
    else:
        g = 288.1221695283 * ((t - 60) ** -0.0755148492)
    if t >= 66:
        b = 255
    elif t <= 19:
        b = 0
    else:
        b = 138.5177312231 * math.log(t - 10) - 305.0447927307
    return (_clamp(r), _clamp(g), _clamp(b))


NLUT = 2048
T_MIN, T_MAX = 500.0, 120000.0
_LOG_MIN = math.log(T_MIN)
_LUT_SCALE = (NLUT - 1) / (math.log(T_MAX) - _LOG_MIN)
COLOR_LUT = np.array(
    [
        blackbody_color(
            math.exp(_LOG_MIN + i / (NLUT - 1) * (math.log(T_MAX) - _LOG_MIN))
        )
        for i in range(NLUT)
    ],
    dtype=np.uint8,
)


def colors_from_temp(temps):
    idx = ((np.log(np.clip(temps, T_MIN, T_MAX)) - _LOG_MIN) * _LUT_SCALE).astype(
        np.int32
    )
    np.clip(idx, 0, NLUT - 1, out=idx)
    return COLOR_LUT[idx]


# ---------- deterministic infinite starfield (fully vectorised, hash-based) ----------
_CHOICES = np.array([1, 1, 1, 2, 2, 3], dtype=np.int32)


def _rand01(CX, CY, salt):
    k = CX.astype(np.uint64) * np.uint64(73856093)
    k = k ^ (CY.astype(np.uint64) * np.uint64(19349663))
    k = k ^ (np.uint64(salt) * np.uint64(2654435761))
    k = k ^ (k >> np.uint64(33))
    k = k * np.uint64(0xFF51AFD7ED558CCD)
    k = k ^ (k >> np.uint64(33))
    k = k * np.uint64(0xC4CEB9FE1A85EC53)
    k = k ^ (k >> np.uint64(33))
    return (k >> np.uint64(11)).astype(np.float64) * (1.0 / 9007199254740992.0)


def visible_stars(center, gamma, vel_dir, zoom):
    R = 0.5 * math.hypot(WIDTH, HEIGHT) * GEN_MARGIN / zoom
    ux, uy = vel_dir.real, vel_dir.imag
    a, b = gamma * R, R
    half_w = math.sqrt((a * ux) ** 2 + (b * uy) ** 2)
    half_h = math.sqrt((a * uy) ** 2 + (b * ux) ** 2)
    ncells = (2 * half_w / CELL_SIZE + 1) * (2 * half_h / CELL_SIZE + 1)
    if ncells > MAX_CELLS:
        s = math.sqrt(MAX_CELLS / ncells)
        half_w *= s
        half_h *= s
    cx0 = math.floor((center.real - half_w) / CELL_SIZE)
    cx1 = math.floor((center.real + half_w) / CELL_SIZE)
    cy0 = math.floor((center.imag - half_h) / CELL_SIZE)
    cy1 = math.floor((center.imag + half_h) / CELL_SIZE)
    cxs = np.arange(cx0, cx1 + 1, dtype=np.int64)
    cys = np.arange(cy0, cy1 + 1, dtype=np.int64)
    if cxs.size == 0 or cys.size == 0:
        return (np.empty(0, np.complex128), np.empty(0), np.empty(0, np.int32))
    CX, CY = np.meshgrid(cxs, cys)
    CX = CX.ravel()
    CY = CY.ravel()
    n = CX.size
    pos = np.empty(n * STARS_PER_CELL, np.complex128)
    temp = np.empty(n * STARS_PER_CELL, np.float64)
    size = np.empty(n * STARS_PER_CELL, np.int32)
    for i in range(STARS_PER_CELL):
        rx = _rand01(CX, CY, 100 + i)
        ry = _rand01(CX, CY, 200 + i)
        rt = _rand01(CX, CY, 300 + i)
        rs = _rand01(CX, CY, 400 + i)
        sl = slice(i * n, (i + 1) * n)
        pos[sl] = (CX + rx) * CELL_SIZE + 1j * ((CY + ry) * CELL_SIZE)
        temp[sl] = 1500 + 30000 * rt**3
        size[sl] = _CHOICES[np.clip((rs * 6).astype(np.int32), 0, 5)]
    return pos, temp, size


# ============================================================
#  THIS IS THE ONLY PART YOU IMPLEMENT
# ============================================================
class Observer:
    def __init__(self):
        self.cords = 0 + 0j
        self.momentum = 0 + 0j
        self.angle = 0.0
        self.view_mode = 0
        self.real_view_mode = 0.0
        self.target_pos = None
        self.warp = 0
        self.st_distance = 0.0
        self.time = 0.0
        self.proper_time = 0.0

    @property
    def velocity(self):
        m = abs(self.momentum)
        return self.momentum / math.sqrt(1 + m**2)

    @property
    def velocity_dir(self):
        return self.momentum / abs(self.momentum) if self.momentum != 0 else 1 + 0j

    @property
    def gamma(self):
        v = abs(self.velocity)
        return 1 / math.sqrt(1 - v**2)

    def rotate(self, d_angle):
        self.angle += d_angle

    def speedup(self, force):
        self.momentum += force * np.exp(1j * self.angle) * DTAU

    def slowdown(self, force):
        dm = (
            force * self.momentum / abs(self.momentum) * DTAU
            if self.momentum != 0
            else 0
        )
        if abs(dm) > abs(self.momentum):
            self.momentum = 0 + 0j
        else:
            self.momentum -= dm

    def update(self):
        self.time += self.gamma * DTAU
        self.proper_time += DTAU
        self.cords += self.momentum * DTAU
        if self.view_mode != round(self.real_view_mode, 5):
            self.real_view_mode += (self.view_mode * 2 - 1) * 0.01
            self.real_view_mode = min(1.0, max(0.0, self.real_view_mode))

        match self.warp:
            case 1:
                if self.momentum != 0:
                    self.slowdown(ENGINE_ACCEL)
                else:
                    self.warp = 2
            case 2:
                ang = np.angle(
                    (self.target_pos - self.cords) * np.exp(1j * self.angle).conjugate()
                )
                if np.abs(ang) > 0.1:
                    self.rotate(ROTATE_SPEED * np.sign(ang))
                else:
                    self.rotate(ang)
                    self.st_distance = np.abs(self.target_pos - self.cords)
                    self.warp = 3
            case 3:
                if self.st_distance * 0.75 < np.abs(self.target_pos - self.cords):
                    self.speedup(ENGINE_ACCEL)
                else:
                    self.warp = 4
            case 4:
                if self.st_distance * 0.25 > np.abs(self.target_pos - self.cords):
                    self.warp = 5
            case 5:
                if np.abs(self.momentum) > 0:
                    self.slowdown(ENGINE_ACCEL)
                else:
                    self.warp = 0
            case _:
                pass

    def eye_transform(self, aligned, temp):
        b = abs(self.velocity)
        g = self.gamma
        mag = np.maximum(np.abs(aligned), 1e-12)
        ang = aligned / mag
        ar = ang.real
        d = 1 + b * ar
        aligned = mag * ((ar + b) / d + 1j * ang.imag / (g * d))
        mag2 = np.maximum(np.abs(aligned), 1e-12)
        temp = temp / (g * (1 - b * aligned.real / mag2))
        return aligned, temp

    def map_transform(self, aligned, temp):
        return aligned.real / self.gamma + 1j * aligned.imag, temp

    def transform(self, rel, temp):
        aligned = rel * np.conj(self.velocity_dir)
        rv = self.real_view_mode
        if rv <= 0.0:
            aligned, temp = self.eye_transform(aligned, temp)
        elif rv >= 1.0:
            aligned, temp = self.map_transform(aligned, temp)
        else:
            ea, et = self.eye_transform(aligned, temp)
            ma, mt = self.map_transform(aligned, temp)
            aligned = (1.0 - rv) * ea + rv * ma
            temp = (1.0 - rv) * et + rv * mt
        return aligned * self.velocity_dir, temp

    def wiev_swap(self):
        self.view_mode = 0 if self.view_mode else 1

    def target(self, pos):
        self.target_pos = pos
        self.warp = 1


# ============================================================


def main():
    global WIDTH, HEIGHT
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Relativistic ship")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 18)

    center = complex(WIDTH // 2, HEIGHT // 2)
    ship = Observer()
    fullscreen = False
    windowed_size = (WIDTH, HEIGHT)
    frame = np.empty((WIDTH, HEIGHT, 3), dtype=np.uint8)

    vis_world = np.empty(0, np.complex128)
    vis_screen = np.empty(0, np.complex128)
    selected_world = None
    zoom = 1.0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE and not fullscreen:
                WIDTH, HEIGHT = event.w, event.h
                windowed_size = (WIDTH, HEIGHT)
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                center = complex(WIDTH // 2, HEIGHT // 2)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ship.wiev_swap()
                elif event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        info = pygame.display.Info()
                        WIDTH, HEIGHT = info.current_w, info.current_h
                        screen = pygame.display.set_mode(
                            (WIDTH, HEIGHT), pygame.FULLSCREEN
                        )
                    else:
                        WIDTH, HEIGHT = windowed_size
                        screen = pygame.display.set_mode(
                            (WIDTH, HEIGHT), pygame.RESIZABLE
                        )
                    center = complex(WIDTH // 2, HEIGHT // 2)
                elif event.key == pygame.K_ESCAPE and fullscreen:
                    fullscreen = False
                    WIDTH, HEIGHT = windowed_size
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                    center = complex(WIDTH // 2, HEIGHT // 2)
                elif event.key == pygame.K_e:
                    if selected_world is not None:
                        ship.target(selected_world)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = complex(*event.pos)
                if vis_screen.size:
                    d = np.abs(vis_screen - mouse)
                    j = int(np.argmin(d))
                    selected_world = vis_world[j] if d[j] < 15 else None
                else:
                    selected_world = None
            elif event.type == pygame.MOUSEWHEEL:
                zoom = max(0.05, min(20.0, zoom * (1.1**event.y)))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            ship.rotate(-ROTATE_SPEED)
        if keys[pygame.K_d]:
            ship.rotate(ROTATE_SPEED)
        if keys[pygame.K_w]:
            ship.speedup(ENGINE_ACCEL)
        if keys[pygame.K_s]:
            ship.speedup(-ENGINE_ACCEL)
        if keys[pygame.K_q]:
            ship.slowdown(ENGINE_ACCEL)

        ship.update()

        if frame.shape[0] != WIDTH or frame.shape[1] != HEIGHT:
            frame = np.empty((WIDTH, HEIGHT, 3), dtype=np.uint8)
        frame[:] = BACKGROUND

        gamma_gen = ship.gamma if ship.real_view_mode > 0 else 1.0
        pos, temp, size = visible_stars(ship.cords, gamma_gen, ship.velocity_dir, zoom)

        view_rot = np.exp(-1j * ship.angle) * (-1j) * zoom
        vis_world = np.empty(0, np.complex128)
        vis_screen = np.empty(0, np.complex128)

        if pos.size:
            rel = pos - ship.cords
            trel, ttemp = ship.transform(rel, temp)
            sr = trel * view_rot
            px = center.real + sr.real
            py = center.imag + sr.imag
            on = (px >= 0) & (px < WIDTH) & (py >= 0) & (py < HEIGHT)
            if on.any():
                pxi = px[on].astype(np.int32)
                pyi = py[on].astype(np.int32)
                cols = colors_from_temp(ttemp[on])
                ds = np.clip((size[on] * zoom).astype(np.int32), 1, MAX_STAR_PX)
                maxs = int(ds.max())
                for dx in range(maxs):
                    for dy in range(maxs):
                        m = (dx < ds) & (dy < ds)
                        if not m.any():
                            continue
                        xs = pxi[m] + dx
                        ys = pyi[m] + dy
                        v = (xs < WIDTH) & (ys < HEIGHT)
                        frame[xs[v], ys[v]] = cols[m][v]
                vis_world = pos[on]
                vis_screen = px[on] + 1j * py[on]

        pygame.surfarray.blit_array(screen, frame)

        if selected_world is not None:
            rel = selected_world - ship.cords
            trel, _ = ship.transform(rel, 0.0)
            sr = trel * view_rot
            hx = float(sr.real) + center.real
            hy = float(sr.imag) + center.imag
            if 0 <= hx < WIDTH and 0 <= hy < HEIGHT:
                pygame.draw.circle(screen, (255, 255, 80), (int(hx), int(hy)), 8, 2)

        pygame.draw.polygon(
            screen,
            SHIP_COLOR,
            [
                (int(center.real), int(center.imag) - 14),
                (int(center.real) - 9, int(center.imag) + 10),
                (int(center.real) + 9, int(center.imag) + 10),
            ],
        )

        p_mag = abs(ship.momentum)
        beta = p_mag / math.sqrt(1 + p_mag * p_mag)
        b = min(beta, 0.999999)
        gamma = 1.0 / math.sqrt(1 - b * b)
        mode_label = "OKNO - co oko vidi" if ship.view_mode == 0 else "MAPA - kde to je"
        hud = f"{beta * 100:6.2f} % c   gamma = {gamma:5.2f}   [MEZERNIK] {mode_label}   [F] cela obrazovka"
        screen.blit(font.render(hud, True, (200, 200, 210)), (12, 10))
        screen.blit(
            font.render(
                f"svet (venku):   {fmt_time(ship.time)}", True, (150, 210, 150)
            ),
            (12, 34),
        )
        screen.blit(
            font.render(
                f"lod (tvuj cas): {fmt_time(ship.proper_time)}", True, (210, 190, 120)
            ),
            (12, 56),
        )

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
