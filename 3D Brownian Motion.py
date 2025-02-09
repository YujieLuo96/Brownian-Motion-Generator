import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation, PillowWriter

# Parameters
num_points = 30  # Number of points
box_size = 30    # Size of the box
time_steps = 30000 # Number of time steps
step_size = 0.05  # Step size for random displacement
start_point = [box_size / 2, box_size / 2, box_size / 2]  # Start at the center of the box

# Initialize positions
positions = np.full((num_points, 3), start_point)  # All points start at the same position

# Store the paths of the points
path_data = [[] for _ in range(num_points)]  # Store positions for each point's path

# Simulate Brownian motion
for _ in range(time_steps):
    # Generate random displacements for Brownian motion
    displacements = np.random.normal(0, step_size, (num_points, 3))  # Random Gaussian steps in 3D
    positions += displacements

    # Ensure points stay within the box (optional, for visualization purposes)
    positions = np.clip(positions, 0, box_size)

    # Append the current position to the path
    for i in range(num_points):
        path_data[i].append(positions[i].copy())

# Create the figure and axis
fig = plt.figure(figsize=(10, 10), dpi=100)  # Adjust DPI for GIF size
ax = fig.add_subplot(111, projection='3d')

# Remove the 3D coordinate frame
ax.set_axis_off()  # Disable the axes

# Set limits for the plot (optional, to ensure points stay within the box)
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_zlim(0, box_size)

# Plot the paths with different colors
colors = plt.cm.viridis(np.linspace(0, 1, num_points))  # Assign unique colors
lines = [ax.plot([], [], [], color=colors[i], alpha=0.7, lw=1, label=f'Point {i+1}')[0] for i in range(num_points)]

# Plot the final positions of the points
scatter = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], color=colors, s=1, edgecolor='black')

# Function to initialize the animation
def init():
    for line in lines:
        line.set_data([], [])
        line.set_3d_properties([])
    return lines + [scatter]

# Function to update the animation (rotate the view)
def update(frame):
    # Rotate the view
    ax.view_init(elev=30, azim=frame)  # Adjust elevation and azimuth for rotation

    # Update the paths
    for i, line in enumerate(lines):
        path_x, path_y, path_z = zip(*path_data[i])
        line.set_data(path_x, path_y)
        line.set_3d_properties(path_z)

    return lines + [scatter]

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 360, 2), init_func=init, blit=True, interval=50)

# Save the animation as a GIF
writer = PillowWriter(fps=20)  # Use PillowWriter to save as GIF
ani.save('3d_brownian_motion_rotation.gif', writer=writer)

# Show the plot (optional)
plt.show()