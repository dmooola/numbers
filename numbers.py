import os

def read_file(file_name):
    if not os.path.exists(file_name):
        print("Error: File does not exist.")
        return None

    with open(file_name, 'r') as file:
        numbers = [float(line.strip()) for line in file]

    return numbers

def calculate_statistics(numbers):
    if numbers is None:
        return None

    num_count = len(numbers)
    if num_count == 0:
        return None

    total_sum = sum(numbers)
    mean = total_sum / num_count
    numbers.sort()
    median = numbers[num_count // 2] if num_count % 2 != 0 else (numbers[num_count // 2 - 1] + numbers[num_count // 2]) / 2

    smallest = min(numbers)
    largest = max(numbers)

    return num_count, total_sum, mean, median, smallest, largest

def main():
    while True:
        file_name = input("Enter the file name (e.g., data1.txt or data2.txt): ")
        numbers = read_file(file_name)
        if numbers is not None:
            break

    statistics = calculate_statistics(numbers)
    if statistics is not None:
        num_count, total_sum, mean, median, smallest, largest = statistics
        print("Number of numbers read from the file:", num_count)
        print("Sum of all numbers:", total_sum)
        print("Mean of all numbers:", mean)
        print("Median of all numbers:", median)
        print("Smallest number:", smallest)
        print("Largest number:", largest)

if __name__ == "__main__":
    main()
fp = open ("data.txt", "w")
