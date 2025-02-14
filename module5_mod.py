class NumberProcessor:
    def __init__(self):
        self.numbers = []  # Initializes an empty list for storing numbers

    def add_number(self, number):
        self.numbers.append(number)

    def search_number(self, x):
        # Returns index (1-based) if found, otherwise -1
        for idx, num in enumerate(self.numbers, start=1):
            if num == x:
                return idx
        return -1
