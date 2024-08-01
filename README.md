# Monte Carlo Simulation for Estimating Pi

This project is a simple implementation of the Monte Carlo method to estimate the value of π (Pi). The Monte Carlo method is a computational algorithm that relies on repeated random sampling to obtain numerical results. This implementation uses random point generation within a unit square to estimate the value of Pi based on the ratio of points inside a quarter-circle to the total number of points.

## Overview

The project estimates the value of Pi using the following steps:

1. **Generate Random Points**: Randomly generate points within a unit square.
2. **Check Circle Inclusion**: Determine whether each point falls inside a quarter-circle with a radius of 1.
3. **Calculate Pi Estimate**: Use the ratio of points inside the circle to the total points generated to estimate Pi.
4. **Visualize Results**: Plot the points, distinguishing between those inside and outside the circle, and display the estimated value of Pi.

## Installation

To run this project, you need to have Python installed on your machine along with the following libraries:

- `matplotlib`
- `numpy`

You can install the required libraries using `pip`:

```bash
pip install matplotlib numpy
