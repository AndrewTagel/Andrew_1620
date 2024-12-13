import csv


def validate_voter_id(user_id):
    """
    Check if the voter ID is valid (8 digits).

    Args:
        user_id (str): The user ID to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    return user_id.isdigit() and len(user_id) == 8


def id_used(user_id, votes_file):
    """
    Check if the voter ID has already been used.

    Args:
        user_id (str): The user ID to check.
        votes_file (str): Path to the votes CSV file.

    Returns:
        bool: True if the ID is already used, False otherwise.
    """
    with open(votes_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["ID"] == user_id:
                return True
    return False