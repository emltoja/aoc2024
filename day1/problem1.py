from pathlib import Path

INPUT_PATH = Path(__file__).parent / "input.txt"


def main():
    with open(INPUT_PATH, "r") as file:
        data = file.read().splitlines()
    first_col = sorted(list(map(lambda x: int(str(x).split()[0]), data)))
    second_col = sorted(list(map(lambda x: int(str(x).split()[1]), data)))

    print(sum([abs(x - y) for x, y in zip(first_col, second_col)]))


if __name__ == "__main__":
    main()
