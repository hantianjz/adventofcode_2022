import argparse
import pathlib


score = {"A": 1, "B": 2, "C": 3}
wmap = {"X": "A", "Y": "B", "Z": "C"}

game = {
    "A": {"A": 1, "B": 2, "C": 0},
    "B": {"A": 0, "B": 1, "C": 2},
    "C": {"A": 2, "B": 0, "C": 1},
}


res_game = {
    "A": {"X": "C", "Y": "A", "Z": "B"},
    "B": {"X": "A", "Y": "B", "Z": "C"},
    "C": {"X": "B", "Y": "C", "Z": "A"},
}


def get_hand(p1, res):
    return res_game[p1][res]


def get_score(p1, p2):
    return score[p2] + game[p1][p2] * 3


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    total_score = 0
    total_new_score = 0

    input_path = pathlib.Path(args.file)
    with open(input_path, mode="r") as ip:
        for line in ip:
            p = line.split()
            total_new_score += get_score(p[0], get_hand(p[0], p[1]))
            # p[1] = wmap[p[1]]
            # total_score += get_score(p[0], p[1])

    # print(total_score)
    print(total_new_score)


if __name__ == "__main__":
    main()
