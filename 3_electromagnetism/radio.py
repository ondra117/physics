import numpy as np
import matplotlib.pyplot as plt
import subprocess

L_A1 = 20
L_A2 = 20
D = 50
R = 1
F = 0.15
A = 0.5
DT = 0.1

DX = 0.5

c = 1  # 299_792_458
eps = 1  # 8.854e-12

sigma_vacuum = 0
sigma_iron = 1000  # 1e7
sigma_light_bulb = 3


def get_sigma(cords):
    X = np.where(
        (
            (cords[..., 0] >= D - R)
            & (cords[..., 0] <= D + R)
            & (np.abs(cords[..., 1]) <= L_A1)
        )
        | (
            (cords[..., 0] >= -D - R)
            & (cords[..., 0] <= -D + R)
            & (np.abs(cords[..., 1]) <= L_A2)
        ),
        sigma_iron,
        sigma_vacuum,
    )
    X = np.where(
        (
            (cords[..., 0] >= D - R)
            & (cords[..., 0] <= D + R)
            & (np.abs(cords[..., 1]) <= R)
        ),
        0,
        X,
    )
    # X = np.where(
    #     (
    #         (np.abs(cords[..., 0]) <= R) &
    #         (np.abs(cords[..., 1]) >= 2 * R)
    #     ),
    #     sigma_iron,
    #     X,
    # )
    return np.where(
        (
            (cords[..., 0] >= -D - R)
            & (cords[..., 0] <= -D + R)
            & (np.abs(cords[..., 1]) <= R)
        ),
        sigma_light_bulb,
        X,
    )


def get_I(cords, t):
    I = A * np.sin(F * t)
    return np.where(
        (
            (cords[..., 0] >= D - R)
            & (cords[..., 0] <= D + R)
            & (np.abs(cords[..., 1]) <= R)
        )[..., None],
        [0, I],
        [0, 0],
    )


def get_light_bulb(cords):
    return np.where(
        (
            (cords[..., 0] >= -D - R)
            & (cords[..., 0] <= -D + R)
            & (np.abs(cords[..., 1]) <= R)
        ),
        1,
        0,
    )


l = max(L_A1, L_A2)
l_s = -l - 10
l_e = l + 10

d_s = -D - 10
d_e = D + 10

ext = [d_s, d_e, l_s, l_e]
ext_old = [d_s, d_e, l_s, l_e]

coords = np.stack(
    np.meshgrid(
        np.linspace(d_s, d_e, 1 + int((d_e - d_s) / DX)),
        np.linspace(l_s, l_e, 1 + int((l_e - l_s) / DX)),
        indexing="ij",
    ),
    axis=-1,
)

sigma = get_sigma(coords)

light_bulb = get_light_bulb(coords)

rgba = np.zeros(sigma.shape + (4,))
rgba[..., :3] = [0.12, 0.62, 0.46]
rgba[..., 3] = sigma / sigma.max()

B_z = np.zeros_like(sigma, dtype=np.float64)
E_x = np.zeros_like(sigma, dtype=np.float64)
E_y = np.zeros_like(sigma, dtype=np.float64)

data = [B_z, E_x, E_y, 0]


def fdx(f):
    return (np.roll(f, -1, 0) - f) / DX  # dopredna, podel x


def fdy(f):
    return (np.roll(f, -1, 1) - f) / DX  # dopredna, podel y


def bdx(f):
    return (f - np.roll(f, 1, 0)) / DX  # zpetna, podel x


def bdy(f):
    return (f - np.roll(f, 1, 1)) / DX  # zpetna, podel y


mur = (c * DT - DX) / (c * DT + DX)


def mur_boundary(Enew, Eold):
    # leva a prava hrana (kolme na x): index 0 a -1, soused 1 a -2
    Enew[1, :] = Eold[2, :] + mur * (Enew[2, :] - Eold[1, :])
    Enew[-1, :] = Eold[-2, :] + mur * (Enew[-2, :] - Eold[-1, :])
    # dolni a horni hrana (kolme na y): index 1 a -1, soused 1 a -2
    Enew[:, 1] = Eold[:, 2] + mur * (Enew[:, 2] - Eold[:, 1])
    Enew[:, -1] = Eold[:, -2] + mur * (Enew[:, -2] - Eold[:, -1])


def step(inp):
    B_z, E_x, E_y, t = inp

    t += DT

    ex_prev = E_x.copy()  # <- ciste E^n (pred updatem)
    ey_prev = E_y.copy()
    bz_prev = B_z.copy()

    I = get_I(coords, t)

    B_z = B_z - DT * (fdx(E_y) - fdy(E_x))

    ca = (1 - sigma * DT / (2 * eps)) / (1 + sigma * DT / (2 * eps))
    cb = DT / (1 + sigma * DT / (2 * eps))

    E_x = ca * E_x + cb * (c**2 * bdy(B_z) - I[..., 0] / eps)
    E_y = ca * E_y + cb * (-(c**2) * bdx(B_z) - I[..., 1] / eps)

    # mur_boundary(E_x, ex_prev)
    # mur_boundary(E_y, ey_prev)
    E_x[1, :] = E_x[-1, :] = E_x[:, 1] = E_x[:, -1] = 0
    E_y[1, :] = E_y[-1, :] = E_y[:, 1] = E_y[:, -1] = 0

    return B_z, E_x, E_y, t


fig = plt.figure(figsize=(11, 5))
ax = fig.add_subplot(111)

w, h = fig.canvas.get_width_height()

proc = subprocess.Popen(
    [
        "ffmpeg",
        "-y",
        "-f",
        "rawvideo",
        "-pix_fmt",
        "rgba",
        "-s",
        f"{w}x{h}",
        "-r",
        "30",
        "-i",
        "-",
        "-pix_fmt",
        "yuv420p",
        "antena.mp4",
    ],
    stdin=subprocess.PIPE,
)

n = 0
try:
    while True:
        data = step(data)
        _, E_x, E_y, _ = data

        n += 1
        if n % 5 == 0:
            P = sigma_light_bulb * np.sum((E_x**2 + E_y**2) * light_bulb)
            B_z = data[0]
            ax.clear()
            v = np.percentile(np.abs(B_z), 99.5) + 1e-9  # skala barev podle pole
            ax.imshow(
                B_z.T,
                origin="lower",
                extent=ext,
                aspect="equal",
                cmap="RdBu_r",
                vmin=-v,
                vmax=v,
            )  # pole: cervena/modra
            ax.imshow(
                np.transpose(rgba, (1, 0, 2)),
                origin="lower",
                extent=ext,
                aspect="equal",
            )  # vodic navrch

            bulb = np.zeros(sigma.shape + (4,))
            intensity = np.clip(P * 10, 0, 1)  # 0..1
            bulb[..., 0] = 1.0 * intensity  # R roste
            bulb[..., 1] = 0.85 * intensity  # G roste
            bulb[..., 2] = 0.1 * intensity  # B (skoro nic)
            bulb[..., 3] = light_bulb  # alfa pevna: kde je tyc, kresli
            ax.imshow(
                np.transpose(bulb, (1, 0, 2)),
                origin="lower",
                extent=ext,
                aspect="equal",
            )

            fig.canvas.draw()
            proc.stdin.write(fig.canvas.buffer_rgba())  # snimek -> ffmpeg
            proc.stdin.flush()
            plt.pause(1 / 60)
finally:
    proc.stdin.close()  # at ffmpeg cistne dopise hlavicku
    proc.wait()
