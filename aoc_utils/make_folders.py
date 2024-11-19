import os

for i in range(1,26):
    if len(str(i)) == 1:
        dir_name = f'0{i}'
    else:
        dir_name = str(i)
    os.mkdir(dir_name)

    dataset = open(f'{dir_name}/dataset.txt', 'x')
    problem = open(f'{dir_name}/problem.txt', 'x')
    sample_dataset = open(f'{dir_name}/sample_dataset.txt', 'x')
    init = open(f'{dir_name}/__init__.py', 'x')

    lines = [
        "from aoc_utils.open_data import open_dataset_lines as odl, open_dataset_unparsed as odu",
        "from aoc_utils.types import ImportOption",
        "",
        "option: ImportOption = ImportOption.SAMPLE_LINES",
        "",
        "match option:",
        "    case ImportOption.SAMPLE_LINES:",
        f"        data = odl('{dir_name}/sample_dataset.txt')",
        "    case ImportOption.SAMPLE_UNPARSED:",
        f"        data = odu('{dir_name}/sample_dataset.txt')",
        "    case ImportOption.FULL_LINES:",
        f"        data = odl('{dir_name}/dataset.txt')",
        "    case ImportOption.FULL_UNPARSED:",
        f"        data = odu('{dir_name}/dataset.txt')",
        "",
        "def part_1():",
        "    pass",
        "",
        "def part_2():",
        "    pass",
        "",
        "",
        "print(part_1())",
        "print(part_2())"
    ]
    with open(f'{dir_name}/solution.py', 'x') as file:
        for line in lines:
            file.write(line + '\n')
    
