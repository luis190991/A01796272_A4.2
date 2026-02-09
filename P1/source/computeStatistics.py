"""
Compute descriptive statistics from a file of numbers.

This program reads numeric values from a file and calculates
mean, median, mode, variance, and standard deviation using
basic algorithms only.
"""
# pylint: disable=invalid-name
import sys
import time


def read_numbers(filename):
    """Read numbers from a file and ignore invalid data."""
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Invalid data at line {line_number}: {line.strip()}")
    return numbers


def count(numbers):
    """Count how many numbers are in the list."""
    total = 0
    for _ in numbers:
        total += 1
    return total


def mean(numbers):
    """Calculate the mean of a list of numbers."""
    total = 0
    for n in numbers:
        total += n
    return total / count(numbers)


def median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_nums = sorted(numbers)
    n = count(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]


def mode(numbers):
    """Calculate the mode of a list of numbers."""
    freq = {}
    for n in numbers:
        freq[n] = freq.get(n, 0) + 1

    max_count = 0
    mode_value = None
    for number, times in freq.items():
        if times > max_count:
            max_count = times
            mode_value = number

    return mode_value


def variance(numbers, mean_value):
    """Calculate the variance of a list of numbers."""
    total = 0
    for n in numbers:
        total += (n - mean_value) ** 2
    return total / count(numbers)


def standard_deviation(variance_value):
    """Calculate the standard deviation."""
    return variance_value ** 0.5


def main():
    """Main program execution."""
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    filename = sys.argv[1]

    numbers = read_numbers(filename)

    if not numbers:
        print("No valid numbers found.")
        sys.exit(1)

    count_value = count(numbers)
    mean_value = mean(numbers)
    median_value = median(numbers)
    mode_value = mode(numbers)
    variance_value = variance(numbers, mean_value)
    std_dev_value = standard_deviation(variance_value)

    elapsed_time = time.time() - start_time

    result = (
        f"Count: {count_value}\n"
        f"Mean: {mean_value}\n"
        f"Median: {median_value}\n"
        f"Mode: {mode_value}\n"
        f"Variance: {variance_value}\n"
        f"Standard Deviation: {std_dev_value}\n"
        f"Elapsed Time: {elapsed_time:.6f} seconds\n"
    )

    print(result)

    with open("../results/StatisticsResults.txt", "a", encoding="utf-8") as output:
        output.write(
            "\n"
            "==============================\n"
            f"Archivo de entrada: {filename}\n"
            "------------------------------\n"
            f"{result}\n"
        )



if __name__ == "__main__":
    main()
