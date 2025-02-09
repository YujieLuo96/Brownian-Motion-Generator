import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_points = 100  # Number of points
box_size = 24    # Size of the box
time_steps = 80000 # Number of time steps
step_size = 0.01  # Step size for random displacement
start_point = [box_size / 2, box_size / 2]  # Start at the center of the box

# Initialize positions
positions = np.full((num_points, 2), start_point)  # All points start at the same position

# Store the paths of the points
path_data = [[] for _ in range(num_points)]  # Store positions for each point's path

# Simulate Brownian motion
for _ in range(time_steps):
    # Generate random displacements for Brownian motion
    displacements = np.random.normal(0, step_size, (num_points, 2))  # Random Gaussian steps
    positions += displacements

    # Ensure points stay within the box (optional, for visualization purposes)
    positions = np.clip(positions, 0, box_size)

    # Append the current position to the path
    for i in range(num_points):
        path_data[i].append(positions[i].copy())

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10), dpi=300)  # High-resolution figure
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_aspect('equal')
ax.set_title("2D Brownian Motion of 15 Points", fontsize=14)

# Plot the paths with different colors
colors = plt.cm.viridis(np.linspace(0, 1, num_points))  # Assign unique colors
for i in range(num_points):
    path_x, path_y = zip(*path_data[i])
    ax.plot(path_x, path_y, color=colors[i], alpha=0.7, lw=0.2, label=f'Point {i+1}')

# Plot the final positions of the points
#ax.scatter(positions[:, 0], positions[:, 1], color=colors, s=50, edgecolor='black')

# Add a legend
#ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1), fontsize=8)

# Save the figure as a high-resolution image
plt.savefig('brownian_motion_high_res.png', dpi=300, bbox_inches='tight')

# Show the plot
plt.show()