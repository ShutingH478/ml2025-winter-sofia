from module5_mod import NumberProcessor

def main():
    try:
        N = int(input("Enter a positive integer N: "))
        if N <= 0:
            print("N must be a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    processor = NumberProcessor()
    for i in range(N):
        while True:
            try:
                num = int(input(f"Enter number {i+1}: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
        processor.add_number(num)

    try:
        X = int(input("Enter an integer X to search: "))
    except ValueError:
        print("Invalid input! Please enter an integer for X.")
        return

    result = processor.search_number(X)
    print(result)

if __name__ == "__main__":
    main()
