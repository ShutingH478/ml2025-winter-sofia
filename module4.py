# define a function to read N numbers and find the index of X
def find_index_of_x():
    # ask the user for a positive integer N
    N = int(input("Enter a positive integer N: "))
    
    # initialize an empty list to store the numbers
    numbers = []
    
    # loop to read N numbers from the user
    for i in range(N):
        number = int(input(f"Enter number {i + 1}: "))  # read each number
        numbers.append(number)  # add the number to the list
    
    # ask the user for the integer X
    X = int(input("Enter an integer X: "))
    
    # check if X is in the list and return the index or -1
    if X in numbers:
        return numbers.index(X) + 1  # return the index (1-based)
    else:
        return -1  # return -1 if X is not found
