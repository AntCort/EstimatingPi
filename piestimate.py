import random
import math
import matplotlib.pyplot as plt
import numpy as np

def main(num_points):
    points_in_circle = 0  # Counter for points within the circle
    total_points = 0  # Counter for total points generated

    # Lists to store the x and y coordinates of points
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    # Loop through each point to determine its position
    for _ in range(num_points):
        x = random.uniform(0, 1)  # Random x-coordinate between 0 and 1
        y = random.uniform(0, 1)  # Random y-coordinate between 0 and 1

        # Calculate the distance from the origin (0, 0)
        distance = math.sqrt(x**2 + y**2)

        # Check if the point is inside the circle
        if distance <= 1:
            points_in_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

        total_points += 1  # Increment the total points counter

    # Estimate Pi using the ratio of points inside the circle
    pi_estimate = 4 * (points_in_circle / total_points)

    # Plot points inside and outside the circle
    plt.scatter(x_inside, y_inside, color="red", label="Inside Circle")
    plt.scatter(x_outside, y_outside, color="blue", label="Outside Circle")

    # Add legend, labels, and title with the estimated Pi value
    plt.legend()
    plt.xlabel("X - Axis")
    plt.ylabel("Y - Axis")
    plt.title(f"Monte Carlo Simulation for Estimating Pi\nEstimated Pi: {pi_estimate:.5f}")

    # Show the plot
    plt.show()

# Entry point of the program
if __name__ == "__main__":
    try:
        num_points = int(input("Enter the number of points for the simulation: "))
        if num_points <= 0:
            raise ValueError("The number of points must be a positive integer.")
        main(num_points)
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid positive integer.")
