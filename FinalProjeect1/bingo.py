import random
import csv

def generate_bingo_card(options):
    """Generate a 5x5 bingo card"""
    if len(options) < 25:
        raise ValueError("The list must contain at least 25 items to generate a bingo card.")

    selected_items = random.sample(options, 25)
    bingo_card = [selected_items[i:i+5] for i in range(0, 25, 5)]
    return bingo_card

def save_bingo_card(file_path, bingo_card):
    """Save a bingo card to a csv file"""
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(bingo_card)