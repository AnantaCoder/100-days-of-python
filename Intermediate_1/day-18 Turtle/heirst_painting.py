import matplotlib.pyplot as plt
import numpy as np

# Set the canvas size
fig, ax = plt.subplots(figsize=(10, 10))

# Number of dots
num_dots = 100
# Set random seed for consistent results
np.random.seed(42)

# Loop to create the dots
for _ in range(num_dots):
    # Random coordinates for the dots
    x = np.random.uniform(0, 10)
    y = np.random.uniform(0, 10)
    
    # Random color for each dot
    color = np.random.rand(3,)
    
    # Draw the dots (circles)
    ax.scatter(x, y, s=1000, color=color, edgecolor='black')

# Turn off axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])

# Display the "Hirst-style" dot painting
plt.show()
