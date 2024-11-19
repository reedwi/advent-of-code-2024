from aoc_utils.open_data import open_dataset_lines as odl, open_dataset_unparsed as odu
from aoc_utils.types import ImportOption

option: ImportOption = ImportOption.SAMPLE_LINES

match option:
    case ImportOption.SAMPLE_LINES:
        data = odl('22/sample_dataset.txt')
    case ImportOption.SAMPLE_UNPARSED:
        data = odu('22/sample_dataset.txt')
    case ImportOption.FULL_LINES:
        data = odl('22/dataset.txt')
    case ImportOption.FULL_UNPARSED:
        data = odu('22/dataset.txt')

def part_1():
    pass

def part_2():
    pass


print(part_1())
print(part_2())
