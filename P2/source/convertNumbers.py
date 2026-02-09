"""
Convert integers from a file to binary and hexadecimal representations.

Reads a text file from the command line, converts each valid integer to
binary and hexadecimal using basic algorithms (no bin/hex), prints results
to screen, and writes them to ConvertionResults.txt.
"""

# pylint: disable=invalid-name

import sys
import time


def read_integers(filename):
    """Read integers from a file and ignore invalid data."""
    numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            raw = line.strip()

            if raw == "":
                print(f"Invalid data at line {line_number}: (empty)")
                continue

            try:
                numbers.append(int(raw))
            except ValueError:
                print(f"Invalid data at line {line_number}: {raw}")

    return numbers


def to_binary(value):
    """Convert an integer to its binary representation using basic algorithms."""
    if value == 0:
        return "0"

    sign = ""
    n = value
    if n < 0:
        sign = "-"
        n = -n

    digits = []
    while n > 0:
        digits.append(str(n % 2))
        n //= 2

    digits.reverse()
    return sign + "".join(digits)


def to_hex(value):
    """Convert an integer to its hexadecimal representation using basic algorithms."""
    if value == 0:
        return "0"

    sign = ""
    n = value
    if n < 0:
        sign = "-"
        n = -n

    hex_map = "0123456789ABCDEF"
    digits = []
    while n > 0:
        digits.append(hex_map[n % 16])
        n //= 16

    digits.reverse()
    return sign + "".join(digits)


def main():
    """Main program execution."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    filename = sys.argv[1]

    numbers = read_integers(filename)

    if not numbers:
        print("No valid integers found.")
        sys.exit(1)

    lines = []
    header = "Number -> Binary | Hexadecimal"
    lines.append(header)
    lines.append("-" * len(header))

    for number in numbers:
        binary_value = to_binary(number)
        hex_value = to_hex(number)
        lines.append(f"{number} -> {binary_value} | {hex_value}")

    elapsed = time.time() - start_time
    lines.append("")
    lines.append(f"Elapsed Time: {elapsed:.6f} seconds")

    result = "\n".join(lines)

    print(result)

    with open("../results/ConvertionResults.txt", "w", encoding="utf-8") as out:
        out.write(result + "\n")


if __name__ == "__main__":
    main()
