from collections import Counter
from pathlib import Path

INPUT_PATH = Path(__file__).parent / "input.txt"


def main():
    with open(INPUT_PATH, "r") as file:
        data = file.read().splitlines()
    first_col = sorted(list(map(lambda x: int(str(x).split()[0]), data)))
    second_col = sorted(list(map(lambda x: int(str(x).split()[1]), data)))

    occurences = Counter(second_col)
    print(sum([x * occurences[x] for x in first_col]))


if __name__ == "__main__":
    main()
