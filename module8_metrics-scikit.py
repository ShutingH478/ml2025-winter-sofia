import numpy as np
from sklearn.metrics import precision_score, recall_score

# Ask user for input N (positive integer)
N = int(input("Enter the number of points (N): "))
while N <= 0:
    print("Please enter a positive integer.")
    N = int(input("Enter the number of points (N): "))

# Initialize numpy arrays for storing x (ground truth) and y (predicted) values
x = np.zeros(N, dtype=int)
y = np.zeros(N, dtype=int)

# Read N (x, y) points
for i in range(N):
    x_val = int(input(f"Enter x value for point {i + 1} (0 or 1): "))
    while x_val not in [0, 1]:
        print("Please enter 0 or 1.")
        x_val = int(input(f"Enter x value for point {i + 1} (0 or 1): "))
    
    y_val = int(input(f"Enter y value for point {i + 1} (0 or 1): "))
    while y_val not in [0, 1]:
        print("Please enter 0 or 1.")
        y_val = int(input(f"Enter y value for point {i + 1} (0 or 1): "))
    
    x[i] = x_val
    y[i] = y_val

# Calculate Precision and Recall using Scikit-learn
precision = precision_score(x, y)
recall = recall_score(x, y)

# Output the results
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
