# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Mean function
def mean(arr):
    return sum(arr) / len(arr)

# Updated best_fit function using mean
def best_fit(x, y):
    x = np.array(x)
    y = np.array(y)
    print(f"the xs are : {x}, and ys are {y}")

    n = len(x)
    
    # Calculate means
    mean_x = mean(x)
    mean_y = mean(y)
    
    # Calculate the necessary sums
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi ** 2 for xi in x)
    
    # Calculate slope (m)
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    
    # Calculate intercept (b)
    b = mean_y - m * mean_x
    
    return m, b

# Main function to visualize the projection
def projection_life():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 21, 32, 50, 55, 88, 77, 88, 99, 87]

    data = np.array([x, y]).T
    data2 = pd.DataFrame(data, columns=['x', 'y'])

    # Print the correlation matrix
    print("Correlation Matrix:")
    print(data2.corr())

    # Create the plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data Points')

    # Set labels and title
    ax.set_ylabel('Life expectancy')
    ax.set_xlabel('Gross domestic product')
    ax.set_title('1900')

    # Calculate the best fit line
    m, b = best_fit(x, y)
    reg_line = [(m * xs) + b for xs in x]

    # Plot the regression line
    ax.plot(x, reg_line, label="Regression Line", color="r")

    # Show the plot
    plt.legend()
    plt.show()

def main():
    projection_life()

if __name__ == "__main__":
    main()

# %%
