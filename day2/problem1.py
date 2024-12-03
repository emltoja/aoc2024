from pathlib import Path
import numpy as np

INPUT_PATH = Path(__file__).parent / "input.txt"


def main():
    with open(INPUT_PATH, "r") as file:
        data = file.read()
    reports = list(
        map(lambda x: np.array([int(a) for a in x.split()]), data.splitlines())
    )
    diffs = list(map(lambda x: np.diff(x), reports))
    diffs_signs = list(map(lambda x: np.sign(x), diffs))
    first_assertion = list(
        map(
            lambda x: (np.all(x == 1) or np.all(x == -1)),
            diffs_signs,
        )
    )
    second_assertion = list(
        map(lambda x: np.all(np.abs(x) >= 1) and np.all(np.abs(x) <= 3), diffs)
    )
    result = [a and b for a, b in zip(first_assertion, second_assertion)]
    print(sum(result))


if __name__ == "__main__":
    main()
