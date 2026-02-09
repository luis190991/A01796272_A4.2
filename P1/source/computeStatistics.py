import sys
import time


def read_numbers(filename):
    numbers = []
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                print(f"Invalid data at line {line_number}: {line.strip()}")
    return numbers


def mean(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    return sorted_nums[mid]


def mode(numbers):
    freq = {}
    for n in numbers:
        freq[n] = freq.get(n, 0) + 1

    max_count = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_count]

    return modes[0]  # se regresa la primer moda


def variance(numbers, mean_value):
    total = 0
    for n in numbers:
        total += (n - mean_value) ** 2
    return total / len(numbers)


def std_dev(variance_value):
    return variance_value ** 0.5

def count(numbers):
    total = 0
    for _ in numbers:
        total += 1
    return total


def main():
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
    std_dev_value = std_dev(variance_value)

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

    with open("../results/StatisticsResults.txt", "w") as output:
        output.write(result)


if __name__ == "__main__":
    main()
