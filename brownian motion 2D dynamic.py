import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
num_points = 15  # Number of points
box_size = 30    # Size of the box
time_steps = 3000 # Number of time steps
step_size = 0.05  # Step size for random displacement
start_point = [box_size / 2, box_size / 2]  # Start at the center of the box

# Initialize positions
positions = np.full((num_points, 2), start_point)  # All points start at the same position

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, box_size)
ax.set_ylim(0, box_size)
ax.set_aspect('equal')
ax.set_title("2D Brownian Motion of 15 Points")

# Create the points with different colors
colors = plt.cm.viridis(np.linspace(0, 1, num_points))  # Assign unique colors
points, = ax.plot(positions[:, 0], positions[:, 1], 'o', markersize=1)  # Plot initial points

# Store the paths of the points
paths = [ax.plot([], [], color=colors[i], alpha=0.5, lw=1)[0] for i in range(num_points)]  # Paths for each point
path_data = [[] for _ in range(num_points)]  # Store positions for each point's path

# Function to update the positions of the points
def update(frame):
    global positions

    # Generate random displacements for Brownian motion
    displacements = np.random.normal(0, step_size, (num_points, 2))  # Random Gaussian steps
    positions += displacements

    # Ensure points stay within the box (optional, for visualization purposes)
    positions = np.clip(positions, 0, box_size)

    # Append the current position to the path
    for i in range(num_points):
        path_data[i].append(positions[i].copy())

    # Update the positions of the points in the plot
    points.set_data(positions[:, 0], positions[:, 1])

    # Update the paths
    for i in range(num_points):
        if len(path_data[i]) > 1:
            path_x, path_y = zip(*path_data[i])
            paths[i].set_data(path_x, path_y)

    return [points] + paths

# Create the animation
ani = FuncAnimation(fig, update, frames=time_steps, interval=50, blit=True)

# Show the plot
plt.show()