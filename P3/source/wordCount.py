"""
Count distinct words in a file and report their frequencies.

This program reads a text file from the command line, identifies distinct
words (split by spaces), counts how many times each word appears using
basic algorithms (no special libraries), prints results to screen, and
writes them to WordCountResults.txt.
"""

# pylint: disable=invalid-name

import sys
import time


def normalize_word(word):
    """Normalize a word: lowercase and trim common punctuation."""
    w = word.strip().lower()

    punctuation = ".,;:!?\"'()[]{}<>"

    while w and w[0] in punctuation:
        w = w[1:]

    while w and w[-1] in punctuation:
        w = w[:-1]

    return w


def count_words_from_file(filename):
    """Read a file and count frequencies of normalized words."""
    freq = {}

    with open(filename, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line.strip() == "":
                print(f"Invalid data at line {line_number}: (empty line)")
                continue

            parts = line.split()
            for part in parts:
                word = normalize_word(part)
                if word == "":
                    continue

                freq[word] = freq.get(word, 0) + 1

    return freq


def main():
    """Main program execution."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    start_time = time.time()
    filename = sys.argv[1]

    freq = count_words_from_file(filename)

    if not freq:
        print("No valid words found.")
        sys.exit(1)

    words_sorted = sorted(freq.keys())

    lines = []
    header = "Word -> Count"
    lines.append(header)
    lines.append("-" * len(header))

    for word in words_sorted:
        lines.append(f"{word} -> {freq[word]}")

    elapsed = time.time() - start_time
    lines.append("")
    lines.append(f"Elapsed Time: {elapsed:.6f} seconds")

    result = "\n".join(lines)

    print(result)

    with open("../results/WordCountResults.txt", "a", encoding="utf-8") as output:
        output.write(
            "\n"
            "==============================\n"
            f"Archivo de entrada: {filename}\n"
            "------------------------------\n"
            f"{result}\n"
        )


if __name__ == "__main__":
    main()
