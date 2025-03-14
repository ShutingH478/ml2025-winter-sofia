import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    # Step 1: Read the number of training samples (N)
    N = int(input("Enter the number of training samples N: "))

    # Step 2: Read the training samples
    X_train = []
    y_train = []
    for i in range(N):
        x = float(input(f"Enter x value for training sample {i+1}: "))
        y = int(input(f"Enter y value for training sample {i+1}: "))
        X_train.append([x])  # X is a 2D array (even for 1 feature)
        y_train.append(y)
    
    X_train = np.array(X_train)
    y_train = np.array(y_train)

    # Step 3: Read the number of test samples (M)
    M = int(input("Enter the number of test samples M: "))

    # Step 4: Read the test samples
    X_test = []
    y_test = []
    for i in range(M):
        x = float(input(f"Enter x value for test sample {i+1}: "))
        y = int(input(f"Enter y value for test sample {i+1}: "))
        X_test.append([x])  # X is a 2D array (even for 1 feature)
        y_test.append(y)
    
    X_test = np.array(X_test)
    y_test = np.array(y_test)

    # Step 5: Perform GridSearchCV to find the best k
    param_grid = {'n_neighbors': list(range(1, 11))}  # k values from 1 to 10
    knn = KNeighborsClassifier()

    grid_search = GridSearchCV(estimator=knn, param_grid=param_grid, cv=5)
    grid_search.fit(X_train, y_train)

    # Step 6: Get the best k and test accuracy
    best_k = grid_search.best_params_['n_neighbors']
    print(f"The best value of k is: {best_k}")

    # Step 7: Evaluate the classifier with the best k on the test set
    best_knn = grid_search.best_estimator_
    y_pred = best_knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"The test accuracy for k={best_k} is: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    main()
