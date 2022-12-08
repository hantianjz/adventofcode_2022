import argparse
import pathlib


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    max_cal = 0

    input_path = pathlib.Path(args.file)
    with open(input_path, mode="r") as ip:
        curr_cal = 0
        cals = []
        while True:
            line = ip.readline()
            if line.strip():
                curr_cal += int(line.strip())
            elif line == "\n":
                cals.append(curr_cal)
                if curr_cal > max_cal:
                    max_cal = curr_cal
                curr_cal = 0
            else:
                break

    print(max_cal)
    cals.sort(reverse=True)
    print(cals[:3])
    print(sum(cals[:3]))


if __name__ == "__main__":
    main()
