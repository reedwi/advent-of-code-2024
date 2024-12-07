from aoc_utils.open_data import open_dataset_lines as odl, open_dataset_unparsed as odu
from aoc_utils.types import ImportOption

option: ImportOption = ImportOption.SAMPLE_LINES

match option:
    case ImportOption.SAMPLE_LINES:
        data = odl('06/sample_dataset.txt')
    case ImportOption.SAMPLE_UNPARSED:
        data = odu('06/sample_dataset.txt')
    case ImportOption.FULL_LINES:
        data = odl('06/dataset.txt')
    case ImportOption.FULL_UNPARSED:
        data = odu('06/dataset.txt')

def get_next_pos(current_pos, current_dir):
    match current_dir:
        case '^':
            next_pos = (current_pos[0], current_pos[1] - 1)
        case 'v':
            next_pos = (current_pos[0], current_pos[1] + 1)
        case '<':
            next_pos = (current_pos[0] - 1, current_pos[1])
        case '>':
            next_pos = (current_pos[0] + 1, current_pos[1])
    return next_pos

def part_1():
    for i, row in enumerate(data):
        start = row.find('^')
        if start != -1:
            starting_pos = (start, i)
            break
    
    visited_positions = set([starting_pos])
    current_pos = starting_pos
    current_dir = '^'

    next_dirs = {
        '^': '>',
        'v': '<',
        '<': '^',
        '>': 'v'
    }

    while True:
        next_pos = get_next_pos(current_pos, current_dir)

        if next_pos[1] < 0 or next_pos[1] >= len(data) or next_pos[0] < 0 or next_pos[0] >= len(data[next_pos[1]]):
            break
        while data[next_pos[1]][next_pos[0]] == '#':
            current_dir = next_dirs[current_dir]
            next_pos = get_next_pos(current_pos, current_dir)

        visited_positions.add(next_pos)
        current_pos = next_pos
    return len(visited_positions)

def part_2():
    pass


print(part_1())
print(part_2())
