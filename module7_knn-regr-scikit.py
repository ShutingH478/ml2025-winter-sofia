import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    try:
        # Input and validation for the number of training points
        N = int(input("Enter the number of training points (positive integer): "))
        if N <= 0:
            print("Error: N must be a positive integer.")
            return
        
        # Input and validation for the value of k
        k = int(input("Enter the value of k for k-NN (positive integer): "))
        if k <= 0:
            print("Error: k must be a positive integer.")
            return
        
        if k > N:
            print("Error: k cannot be greater than the number of training points (N).")
            return

        # Initializing lists to store the points
        x_list = []
        y_list = []
        
        # Collecting N (x, y) points from the user
        for i in range(N):
            x_val = float(input(f"Enter x value for point {i+1}: "))
            y_val = float(input(f"Enter y value for point {i+1}: "))
            x_list.append(x_val)
            y_list.append(y_val)

        # Converting lists to numpy arrays
        # X_train needs to be a 2D array for scikit-learn, so we reshape it accordingly.
        X_train = np.array(x_list).reshape(-1, 1)
        y_train = np.array(y_list)

        # Compute and display the variance of the labels in the training dataset
        variance = np.var(y_train)
        print("\nVariance of labels in the training dataset:", variance)

        # Ask the user for an input X to predict the corresponding Y using k-NN regression
        X_input = float(input("\nEnter a value for X to predict Y: "))
        X_input_array = np.array([[X_input]])

        # Use scikit-learn's k-NN Regressor for prediction
        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_input_array)
        
        print("\nPredicted Y value:", y_pred[0])
    
    except ValueError:
        print("Error: Please ensure that you enter valid numbers.")
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
