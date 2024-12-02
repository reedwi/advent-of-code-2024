from aoc_utils.open_data import open_dataset_lines as odl, open_dataset_unparsed as odu
from aoc_utils.types import ImportOption

option: ImportOption = ImportOption.FULL_LINES

match option:
    case ImportOption.SAMPLE_LINES:
        data = odl("02/sample_dataset.txt")
    case ImportOption.SAMPLE_UNPARSED:
        data = odu("02/sample_dataset.txt")
    case ImportOption.FULL_LINES:
        data = odl("02/dataset.txt")
    case ImportOption.FULL_UNPARSED:
        data = odu("02/dataset.txt")

final_data = []
for line in data:
    final_data.append([int(value) for value in line.split()])


def part_1():
    safe_reports = 0
    for report in final_data:
        if report[1] > report[0]:
            increase = True
        else:
            increase = False

        report_len = len(report)
        for i, val in enumerate(report):
            if i == report_len - 1:
                safe_reports += 1
                break
            dif = report[i + 1] - val
            positive = True if dif > 0 else False
            if abs(dif) > 3 or abs(dif) < 1:
                break

            if increase and not positive:
                break

            if not increase and positive:
                break
    return safe_reports


def part_2():
    def safe(report):
        pos = set({1, 2, 3})
        neg = set({-1, -2, -3})
        report_len = len(report)
        for i, val in enumerate(report):
            if i == report_len - 1:
                break
            dif = report[i + 1] - val
            pos.add(dif)
            neg.add(dif)
        return len(pos) == 3 or len(neg) == 3

    safe_reports = 0
    for report in final_data:
        is_safe = safe(report)
        if is_safe:
            safe_reports += 1
            continue

        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]
            is_safe = safe(modified_report)
            if is_safe:
                safe_reports += 1
                break

    return safe_reports


print(part_1())
print(part_2())
