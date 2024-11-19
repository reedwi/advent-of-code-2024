def open_dataset_lines(file_path) -> list:
    with open(file_path, 'r') as file:
        data = [line.strip() for line in file]
    return data

def open_dataset_unparsed(file_path) -> list:
    with open(file_path, 'r') as file:
        data = file.read().strip()
    return data