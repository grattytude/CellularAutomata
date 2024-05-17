import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Grid dimensions
rows = 50
cols = 50

# Initialize grid
grid = np.random.choice([0, 1], size=(rows, cols), p=[0.9, 0.1])

# History of generations
history = [grid]

# Function to update the grid for the next generation
def update_grid(grid):
    new_grid = np.copy(grid)
    
    for i in range(rows):
        for j in range(cols):
            # Count live neighbors
            live_neighbors = np.sum(grid[max(i-1, 0):min(i+2, rows), max(j-1, 0):min(j+2, cols)]) - grid[i, j]
            
            if grid[i, j] == 0 and live_neighbors == 3:
                new_grid[i, j] = 1
            elif grid[i, j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[i, j] = 0
                
    return new_grid

# Update the grid for the next generation and add to history
def update_history(history):
    new_grid = update_grid(history[-1])
    history.append(new_grid)
    
    # Delete the oldest generation
    if len(history) > 10:  # Keep only 10 generations in history
        del history[0]

# Create animation
fig, ax = plt.subplots()

def animate(frame):
    update_history(history)
    
    ax.clear()
    ax.imshow(history[-1], cmap='binary')
    ax.set_title(f'Generation {frame}')

ani = animation.FuncAnimation(fig, animate, frames=100, interval=200, repeat=True)

plt.show()
