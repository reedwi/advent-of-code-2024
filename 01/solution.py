from collections import defaultdict

from aoc_utils.open_data import open_dataset_lines as odl, open_dataset_unparsed as odu
from aoc_utils.types import ImportOption

option: ImportOption = ImportOption.FULL_LINES

match option:
    case ImportOption.SAMPLE_LINES:
        data = odl("01/sample_dataset.txt")
    case ImportOption.SAMPLE_UNPARSED:
        data = odu("01/sample_dataset.txt")
    case ImportOption.FULL_LINES:
        data = odl("01/dataset.txt")
    case ImportOption.FULL_UNPARSED:
        data = odu("01/dataset.txt")

left_data, right_data = [], []
for line in data:
    left, right = line.split()
    left_data.append(int(left))
    right_data.append(int(right))


def part_1():
    left_data.sort()
    right_data.sort()
    distance = 0
    for i in range(len(left_data)):
        distance += abs(left_data[i] - right_data[i])
    return distance


def part_2():
    right_map = defaultdict(int)
    right_data.sort()
    score = 0
    for val in right_data:
        right_map[val] += 1

    for val in left_data:
        if val in right_map:
            score += val * right_map[val]
    return score


print(part_1())
print(part_2())
