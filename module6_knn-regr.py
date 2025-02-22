import numpy as np  # import the numpy library for numerical operations

# define a function to perform k-NN regression
def knn_regression(points, x_input, k):
    # convert the list of points to a numpy array for easier manipulation
    points_array = np.array(points)
    # separate the x and y values from the points
    x_values = points_array[:, 0]  # get all x values
    y_values = points_array[:, 1]  # get all y values
    
    # calculate the distances from the input x to all x values
    distances = np.abs(x_values - x_input)  # absolute differences
    # get the indices of the k nearest neighbors
    k_indices = np.argsort(distances)[:k]  # sort and take the first k indices
    # calculate the average of the y values of the k nearest neighbors
    y_output = np.mean(y_values[k_indices])  # mean of the selected y values
    
    return y_output  # return the predicted y value

# main function to test the knn_regression function
def main_knn_regression():
    # test the knn_regression function
    # use case 1: 3 points and k=2
    points1 = [(1.0, 2.0), (2.0, 3.0), (3.0, 5.0)]  # define points
    x_input1 = 2.5  # input x value
    k1 = 2  # number of neighbors
    result1 = knn_regression(points1, x_input1, k1)  # call the function
    print(f"Predicted Y for input {x_input1} is: {result1}")  # output the result

    # use case 2: 4 points and k=3
    points2 = [(1.0, 2.0), (2.0, 3.0), (3.0, 5.0), (4.0, 7.0)]  # define points
    x_input2 = 3.5  # input x value
    k2 = 3  # number of neighbors
    result2 = knn_regression(points2, x_input2, k2)  # call the function
    print(f"Predicted Y for input {x_input2} is: {result2}")  # output the result
