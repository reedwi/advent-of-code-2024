from aoc_utils.open_data import open_dataset_lines as odl, open_dataset_unparsed as odu
from aoc_utils.types import ImportOption

option: ImportOption = ImportOption.FULL_UNPARSED

match option:
    case ImportOption.SAMPLE_LINES:
        data = odl("03/sample_dataset.txt")
    case ImportOption.SAMPLE_UNPARSED:
        data = odu("03/sample_dataset.txt")
    case ImportOption.FULL_LINES:
        data = odl("03/dataset.txt")
    case ImportOption.FULL_UNPARSED:
        data = odu("03/dataset.txt")


def part_1():
    result = 0
    mul = data.split("mul(")
    for possible in mul:
        try:
            val = possible.split(")")[0]
            left_num, right_num = map(int, val.split(","))
            result += left_num * right_num
        except:
            continue
    return result


def part_2():
    result = 0
    start = 0

    while True:
        mul_index = data.find("mul(", start)
        if mul_index == -1:
            break

        do_index = data.rfind("do()", 0, mul_index)
        dont_index = data.rfind("don't()", 0, mul_index)

        if do_index == -1 and dont_index == -1:
            multiply = True
        elif do_index > dont_index:
            multiply = True
        else:
            multiply = False

        if multiply:
            try:
                possible = data[mul_index + 4 :]
                val = possible.split(")")[0]
                left_num, right_num = map(int, val.split(","))
                result += left_num * right_num
            except:
                pass

        start = mul_index + 4
    return result


print(part_1())
print(part_2())
