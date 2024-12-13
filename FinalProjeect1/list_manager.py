import csv

def load_options(csv_file):
    """Load options from a csv file"""
    try:
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]
    except FileNotFoundError:
        # Return an empty list if the file doesn't exist
        return []

def save_options(csv_file, options):
    """Save options to csv file"""
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for option in options:
            writer.writerow([option])

def add_item(options, item):
    """Add an item to the options list"""
    if item not in options:
        options.append(item)
    else:
        raise ValueError(f"'{item}' is already in the list.")