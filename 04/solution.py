from collections import defaultdict

from aoc_utils.open_data import open_dataset_lines as odl, open_dataset_unparsed as odu
from aoc_utils.types import ImportOption

option: ImportOption = ImportOption.FULL_LINES

match option:
    case ImportOption.SAMPLE_LINES:
        data = odl("04/sample_dataset.txt")
    case ImportOption.SAMPLE_UNPARSED:
        data = odu("04/sample_dataset.txt")
    case ImportOption.FULL_LINES:
        data = odl("04/dataset.txt")
    case ImportOption.FULL_UNPARSED:
        data = odu("04/dataset.txt")


def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))


def part_1():
    def find_xmas(line: str):
        return line.count("XMAS")

    total_count = 0

    rows = groups(data, lambda x, y: y)
    cols = groups(data, lambda x, y: x)
    f_diag = groups(data, lambda x, y: x + y)
    b_diag = groups(data, lambda x, y: x - y)

    for direction in [rows, cols, f_diag, b_diag]:
        for line in direction:
            total_count += find_xmas("".join(line))
            total_count += find_xmas("".join(line[::-1]))

    return total_count


def part_2():
    total_count = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if data[i][j] != "A":
                continue
            a = data[i][j]
            tl = data[i - 1][j - 1]
            tr = data[i - 1][j + 1]
            bl = data[i + 1][j - 1]
            br = data[i + 1][j + 1]
            if tl + a + br in ["SAM", "MAS"] and bl + a + tr in ["SAM", "MAS"]:
                total_count += 1

    return total_count


print(part_1())
print(part_2())
