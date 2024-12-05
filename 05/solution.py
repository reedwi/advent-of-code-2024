from collections import defaultdict

from aoc_utils.open_data import open_dataset_lines as odl, open_dataset_unparsed as odu
from aoc_utils.types import ImportOption

option: ImportOption = ImportOption.FULL_LINES

match option:
    case ImportOption.SAMPLE_LINES:
        data = odl('05/sample_dataset.txt')
    case ImportOption.SAMPLE_UNPARSED:
        data = odu('05/sample_dataset.txt')
    case ImportOption.FULL_LINES:
        data = odl('05/dataset.txt')
    case ImportOption.FULL_UNPARSED:
        data = odu('05/dataset.txt')


def part_1():
    page_rules = defaultdict(list[int])
    middle_values = 0
    for row in data:
        if not row:
            break
        page_rules[int(row.split('|')[0])].append(int(row.split('|')[1]))
        page_rules[int(row.split('|')[0])].sort()
    
    for row in data:
        if '|' in row or not row:
            continue
        ordering = [int(num) for num in row.split(',')] 
        rev_order = ordering[::-1]
        good = True
        for i, num in enumerate(rev_order):
            if not good:
                break
            if num not in page_rules:
                continue

            for order_num in rev_order[i+1:]:
                if order_num in page_rules[num]:
                    good = False
                    break
        if good:
            middle_values += ordering[len(ordering) // 2]

    return middle_values
                


def part_2():
    pass


print(part_1())
print(part_2())
