# README.md

## Summary

This Python script performs linear regression on a dataset of Swedish insurance claims. The code reads data from a CSV file, splits it into training and testing sets, and adjusts the parameters of a linear model (weight `w` and bias `b`) using gradient descent. The script then outputs the final model parameters and plots the predictions alongside the actual data. To use this code, provide a CSV file containing the dataset, set the desired learning rate and number of iterations, and run the script.

## Skills Used

- Python programming
- Data manipulation with CSV files
- Basic linear regression concepts
- Gradient descent optimization
- Visualization with Matplotlib

## Features

- **Quick and easy to understand**: The code is straightforward, making it accessible for those learning linear regression and gradient descent optimization.
- **Visualization with Matplotlib**: The script generates a plot of the data points and the linear model, making it easy to visually assess the quality of the fit.
- **Training and testing split**: The code separates the dataset into training and testing sets to evaluate the performance of the model on unseen data.
- **Flexible learning rate and number of iterations**: The user can easily adjust the learning rate and number of iterations to fine-tune the model's performance.
- **Random initialization of model parameters**: The initial values for `w` and `b` are randomly chosen, demonstrating the ability of gradient descent to find an optimal solution starting from arbitrary initial conditions.
