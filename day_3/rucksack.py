import argparse
import pathlib


def find_dup(r1, r2):
    r1i = 0
    r2i = 0

    dup_str = ""
    while r1i < len(r1) and r2i < len(r2):
        if r1[r1i] == r2[r2i]:
            dup_str += r1[r1i]
            r2i += 1
            r1i += 1
        elif r1[r1i] > r2[r2i]:
            r2i += 1
        elif r1[r1i] < r2[r2i]:
            r1i += 1
    return dup_str


def score(p):
    if 0 < ord(p) - ord("a") < 26:
        return ord(p) - ord("a") + 1
    else:
        return ord(p) - ord("A") + 27


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    total_score = 0

    input_path = pathlib.Path(args.file)
    with open(input_path, mode="r") as ip:
        while True:
            l1 = ip.readline().strip()
            l2 = ip.readline().strip()
            l3 = ip.readline().strip()
            if not (l1 or l2 or l3):
                break
            p1 = find_dup(sorted(l1), sorted(l2))
            p = find_dup(p1, sorted(l3))
            print(f"{p}")
            total_score += score(p[0])
    print(total_score)


if __name__ == "__main__":
    main()
