import sys
import time


def read_integers(filename):
    numbers = []
    with open(filename, "r") as file:
        for line_number, line in enumerate(file, start=1):
            raw = line.strip()
            if raw == "":
                print(f"Invalid data at line {line_number}: (empty)")
                continue
            try:
                # Requerimiento menciona "numbers" como tipo pero para conversión base 2/16 lo mejor es entero
                n = int(raw)
                numbers.append(n)
            except ValueError:
                print(f"Invalid data at line {line_number}: {raw}")
    return numbers


def to_binary(n):
    if n == 0:
        return "0"

    sign = ""
    if n < 0:
        sign = "-"
        n = -n

    digits = []
    while n > 0:
        digits.append(str(n % 2))
        n //= 2

    digits.reverse()
    return sign + "".join(digits)


def to_hex(n):
    if n == 0:
        return "0"

    sign = ""
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

    for n in numbers:
        b = to_binary(n)
        h = to_hex(n)
        lines.append(f"{n} -> {b} | {h}")

    elapsed = time.time() - start_time
    lines.append("")
    lines.append(f"Elapsed Time: {elapsed:.6f} seconds")

    result = "\n".join(lines)

    print(result)

    with open("../results/ConvertionResults.txt", "w") as out:
        out.write(result + "\n")


if __name__ == "__main__":
    main()
