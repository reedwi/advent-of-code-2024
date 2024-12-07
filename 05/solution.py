from collections import defaultdict
from itertools import permutations

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
    # Build adjacency list representation of the graph
    graph = defaultdict(set)
    nodes = set()
    
    # Parse rules into graph
    for row in data:
        if not row:
            break
        before, after = map(int, row.split('|'))
        graph[before].add(after)
        nodes.add(before)
        nodes.add(after)
    
    def topological_sort(numbers):
        # Create subgraph for just the numbers we care about
        local_graph = defaultdict(set)
        for n1 in numbers:
            for n2 in graph[n1]:
                if n2 in numbers:
                    local_graph[n1].add(n2)
        
        in_degree = defaultdict(int)
        for n in numbers:
            for neighbor in local_graph[n]:
                in_degree[neighbor] += 1
        
        queue = [n for n in numbers if in_degree[n] == 0]
        result = []
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            
            for neighbor in local_graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == len(numbers) else None
    
    middle_sum = 0
    for row in data:
        if '|' in row or not row:
            continue
        numbers = [int(n) for n in row.split(',')]
        
        current_valid = True
        for i, n1 in enumerate(numbers):
            for n2 in numbers[i+1:]:
                if n2 in graph[n1]:
                    current_valid = False
                    break
            if not current_valid:
                break
        print('here')
        if not current_valid:
            sorted_nums = topological_sort(numbers)
            if sorted_nums:
                middle_sum += sorted_nums[len(sorted_nums) // 2]
    
    return middle_sum



print(part_1())
print(part_2())
