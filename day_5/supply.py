import argparse
import pathlib


def add_to_stacks(stacks, line):
    si = 0
    while line:
        if len(stacks) <= si:
            stacks.append([])
        if line[0] == "[":
            stacks[si].insert(0, line[:3])
        line = line[4:]
        si += 1


def parse_move(line):
    p = line.split()
    return int(p[1]), int(p[3]) - 1, int(p[5]) - 1


def move(stacks, cnt, frm, to):
    for _ in range(cnt):
        stacks[to].append(stacks[frm].pop())


def main():

    stacks = []

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    input_path = pathlib.Path(args.file)
    with open(input_path, mode="r") as ip:
        while True:
            line = ip.readline().removesuffix("\n")
            if not line:
                break
            add_to_stacks(stacks, line)

        while True:
            line = ip.readline().removesuffix("\n")
            if not line:
                break
            move(stacks, *parse_move(line))

    res = "".join([s[-1] for s in stacks])
    res = res.replace("[", "").replace("]", "")
    print(res)


if __name__ == "__main__":
    main()
