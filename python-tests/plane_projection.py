import numpy as np
import matplotlib.pyplot as plt

N = 10_000
THREE = True


def compute_dists(pairs):
    target = pairs[0]

    delta_theta = np.remainder(pairs[:, 0] - target[0], 2*np.pi)
    delta_psi = np.abs(pairs[:, 1] - target[1])

    delta_theta = np.minimum(delta_theta, 2*np.pi - delta_theta)
    delta_psi = np.minimum(delta_psi, 2*np.pi - delta_psi)

    distances = np.sqrt(delta_theta**2 + delta_psi**2)

    return distances


def compute_flat_dists(pairs, as_boolean=False):
    target = pairs[0]

    delta_theta = np.abs(pairs[:, 0] - target[0])
    delta_zeta = np.abs(pairs[:, 1] - target[1])

    delta_theta = np.minimum(delta_theta, 2*np.pi - delta_theta)
    delta_zeta = np.minimum(delta_zeta, 2*np.pi - delta_zeta)

    distances = np.sqrt(delta_theta**2 + delta_zeta**2)
    distances = distances.max() - distances

    if as_boolean:
        med = np.median(distances)
        distances = distances > med*(8/5)

    return distances



pairs = np.random.uniform(0, 2*np.pi, size=(N, 2))
poloid = pairs[:, 0]
toroid = pairs[:, 1]

print(pairs.shape)
print(poloid.shape)
print(toroid.shape)


# Plot 3d
if THREE:
    R = 8
    r = 2
    s_theta = 1
    s_zeta = 1

    x = (R + r * np.cos(poloid)) * np.cos(toroid)
    y = s_zeta * (R + r * np.cos(poloid)) * np.sin(toroid)
    z = s_theta * r * np.sin(poloid)
    dists = compute_dists(pairs)

    print(f'Target: ({x[0]}, {y[0]}, {z[0]})')
    print(pairs[0])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.scatter(x[1:], y[1:], z[1:], c=dists.max()-dists[1:])
    ax.scatter(x[0], y[0], z[0], color='red', s=200)

    # ax.set_xlim3d(-R, R)
    # ax.set_ylim3d(-R, R)
    # ax.set_zlim3d(-R, R)
    ax.set_aspect('equal')

    plt.gray()
    plt.show()

# else:
theta = pairs[:, 0]
zeta = pairs[:, 1]
dists = compute_flat_dists(pairs)

# Create a 2D plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.scatter(theta[1:], zeta[1:], c=dists[1:], cmap='viridis')
ax.scatter(theta[0], zeta[0], c='red', s=200)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Toroidal Poloidal Coordinate Projection')

# Show the plot
plt.show()