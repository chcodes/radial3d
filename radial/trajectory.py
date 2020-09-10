import math
from math import pi

import numpy as np


def calc_full_radial_coord(nx):
    """Calculates the radial coordinates for a single full spoke.

    Args:
        nx (int): Size of image along one side.
    """
    ind = math.floor(nx / 2)  # End point
    r = np.linspace(-ind, ind, num=nx, dtype=np.float32)
    return r


def calc_half_radial_coord(nx, ramp=False, device=-1):
    """Calculates the radial coordinates for a single half spoke.

    Args:
        nx (int): Size of image along one side.
        ramp (bool): Whether ramp sampling is included.
    """
    ind = math.floor(nx / 2)  # End point
    num_points = nx / 2
    r = np.linspace(0, ind, num=num_points, dtype=np.float32)
    # TODO: Implement ramping and ramp sampling
    return r


def unif_radial_3d(nx, num_theta):
    """Uniform 3D radial trajectory.

    `theta` is the polar angle (rotates away from z axis).
    `phi` is azimuthal angle (rotates in xy-plane)

    Args:
        nx (int): Size of image along one side.
        num_theta (int): Number of polar positions theta.

    Returns:
        traj (array): Trajectory. Shape (na, ns, 3).
    """
    r = calc_full_radial_coord(nx)

    # Calculate polar coordinates
    thetas, dtheta = np.linspace(0, pi, num=num_theta,
                                 endpoint=False, retstep=True)

    area = dtheta * dtheta
    # This is roughly the area that one sample should occupy
    # (divided by radius)

    traj = []

    for theta in thetas:
        if theta == 0:
            dphi = 2 * pi
        else:
            dphi = area / dtheta / np.sin(theta)

        num_phi = math.ceil(2 * pi / dphi / 2)

        phis = np.linspace(0, pi, num=num_phi, endpoint=False)
        # Only 0 to pi because full spoke (other half is sampled)

        for phi in phis:
            z = r * np.cos(theta)
            y = r * np.sin(theta) * np.sin(phi)
            x = r * np.sin(theta) * np.cos(phi)

            traj.append(np.stack((x, y, z), 1))

    traj = np.stack(traj, axis=0)
    return traj


def ga_radial_2d(nx, na):
    """Golden angle 2D radial trajectory.

    Args:
        nx (int): Size of image along one side.
        na (int): Number of spokes.

    Returns:
        traj (array): Trajectory. Shape (na, ns, 2).
    """
    tau = (np.sqrt(5) + 1) / 2
    golden_angle = 180 / tau
    theta_init = 90
    angles = np.linspace(theta_init, theta_init + golden_angle*(na - 1), na)

    r = calc_full_radial_coord(nx)

    traj = np.zeros((na, nx, 2), dtype=np.float32)
    thetas = np.expand_dims(np.radians(angles), axis=1)
    traj[:, :, 0] = np.cos(thetas) * r
    traj[:, :, 1] = np.sin(thetas) * r
    return traj
