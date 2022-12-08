import argparse
import pathlib


def cover(s1, s2):
    s1a, s1b = s1.split("-")
    s2a, s2b = s2.split("-")

    s1a = int(s1a)
    s1b = int(s1b)
    s2a = int(s2a)
    s2b = int(s2b)

    if s1a <= s2a and s2b <= s1b:
        return True
    elif s2a <= s1a and s1b <= s2b:
        return True
    elif s1b > s2a and s1a <= s2b:
        return True
    elif s2b > s1a and s2a <= s1b:
        return True
    return False


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    total_score = 0

    input_path = pathlib.Path(args.file)
    with open(input_path, mode="r") as ip:
        for line in ip:
            s1, s2 = line.split(",")
            if cover(s1, s2):
                total_score += 1
    print(total_score)


if __name__ == "__main__":
    main()
