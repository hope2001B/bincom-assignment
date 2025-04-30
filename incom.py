import os
import re


def create_name_file(full_name, filename="my_name.txt"):
    """Create a text file containing the full name."""
    with open(filename, 'w') as file:
        file.write(full_name)
    return filename


def extract_name_parts(filename):
    """Extract first, middle, and last names from the file using regex."""
    with open(filename, 'r') as file:
        full_name = file.read().strip()

    # Using regex to split the name parts
    # This pattern matches names with multiple middle names
    name_parts = re.findall(r'\b[A-Za-z]+\b', full_name)

    if len(name_parts) == 1:
        return {'first_name': name_parts[0], 'middle_name': '', 'last_name': ''}
    elif len(name_parts) == 2:
        return {'first_name': name_parts[0], 'middle_name': '', 'last_name': name_parts[1]}
    else:
        return {
            'first_name': name_parts[0],
            'middle_name': ' '.join(name_parts[1:-1]),
            'last_name': name_parts[-1]
        }b


def print_file_path():
    """Print the current file path using os module."""
    current_path = os.path.abspath(os.getcwd())
    return current_path


def custom_sort(names):
    """Implement a simple bubble sort algorithm."""
    # Make a copy to avoid modifying the original
    sorted_names = names.copy()
    n = len(sorted_names)

    # Bubble sort
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if sorted_names[j] > sorted_names[j + 1]:
                sorted_names[j], sorted_names[j + 1] = sorted_names[j + 1], sorted_names[j]
hee
    return sorted_names


def binary_search(sorted_list, target):
    """Implement binary search algorithm."""
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if sorted_list[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif sorted_list[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Element was not present
    return -1


def extract_baby_names(filename):
    """Extract baby names from a file using regex."""
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Pattern to find names (assuming names are capitalized words)
        name_pattern = r'\b[A-Z][a-z]+\b'
        baby_names = re.findall(name_pattern, content)

        return baby_names
    except FileNotFoundError:
        return []


# Main execution
if __name__ == "__main__":
    # Your full name
    full_name = "Hope Busola Oyelade"

    # Task 1: Create file with name and extract parts
    filename = create_name_file(full_name)
    name_parts = extract_name_parts(filename)
    print(f"Full name: {full_name}")
    print(f"First name: {name_parts['first_name']}")
    print(f"Middle name: {name_parts['middle_name']}")
    print(f"Last name: {name_parts['last_name']}")

    # Task 2: Print file path
    current_path = print_file_path()
    print(f"\nCurrent file path: {current_path}")

    # Task 3: Extract baby names, sort them, and perform binary search
    # For demonstration, let's create a sample file with baby names
    sample_baby_names = """
    Common baby names include:
    Emma Noah Olivia Liam Ava Elijah Sophia William Isabella James
    Charlotte Benjamin Amelia Lucas Mia Mason Harper Ethan Evelyn
    """

    baby_names_file = "baby_names.txt"
    with open(baby_names_file, 'w') as file:
        file.write(sample_baby_names)

    # Extract baby names
    baby_names = extract_baby_names(baby_names_file)
    print(f"\nExtracted baby names: {baby_names}")

    # Sort the names
    sorted_names = custom_sort(baby_names)
    print(f"\nSorted baby names: {sorted_names}")

    # Perform binary search for a name
    search_name = "Emma"
    position = binary_search(sorted_names, search_name)
    if position != -1:
        print(f"\nFound '{search_name}' at position {position} in the sorted list.")
    else:
        print(f"\n'{search_name}' not found in the list.")

    # Search for your first name
    your_first_name = name_parts['first_name']
    position = binary_search(sorted_names, your_first_name)
    if position != -1:
        print(f"Found '{your_first_name}' at position {position} in the sorted list.")
    else:
        print(f"'{your_first_name}' not found in the sorted baby names list.")

import os
import re


def create_name_file(full_name, filename="my_name.txt"):
    """Create a text file containing the full name."""
    with open(filename, 'w') as file:
        file.write(full_name)
    return filename


def extract_name_parts(filename):
    """Extract first, middle, and last names from the file using regex."""
    with open(filename, 'r') as file:
        full_name = file.read().strip()

    # Using regex to split the name parts
    # This pattern matches names with multiple middle names
    name_parts = re.findall(r'\b[A-Za-z]+\b', full_name)

    if len(name_parts) == 1:
        return {'first_name': name_parts[0], 'middle_name': '', 'last_name': ''}
    elif len(name_parts) == 2:
        return {'first_name': name_parts[0], 'middle_name': '', 'last_name': name_parts[1]}
    else:
        return {
            'first_name': name_parts[0],
            'middle_name': ' '.join(name_parts[1:-1]),
            'last_name': name_parts[-1]
        }


def print_file_path():
    """Print the current file path using os module."""
    current_path = os.path.abspath(os.getcwd())
    return current_path


def custom_sort(names):
    """Implement a simple bubble sort algorithm."""
    # Make a copy to avoid modifying the original
    sorted_names = names.copy()
    n = len(sorted_names)

    # Bubble sort
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if sorted_names[j] > sorted_names[j + 1]:
                sorted_names[j], sorted_names[j + 1] = sorted_names[j + 1], sorted_names[j]

    return sorted_names


def binary_search(sorted_list, target):
    """Implement binary search algorithm."""
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if target is present at mid
        if sorted_list[mid] == target:
            return mid

        # If target is greater, ignore left half
        elif sorted_list[mid] < target:
            left = mid + 1

        # If target is smaller, ignore right half
        else:
            right = mid - 1

    # Element was not present
    return -1


def extract_baby_names(filename):
    """Extract baby names from a file using regex."""
    try:
        with open(filename, 'r') as file:
            content = file.read()

        # Pattern to find names (assuming names are capitalized words)
        name_pattern = r'\b[A-Z][a-z]+\b'
        baby_names = re.findall(name_pattern, content)

        return baby_names
    except FileNotFoundError:
        return []


# Main execution
if __name__ == "__main__":
    # Your name is already set here
    full_name = "Hope Busola Oyelade"

    # Task 1: Create file with name and extract parts
    filename = create_name_file(full_name)
    name_parts = extract_name_parts(filename)
    print(f"Full name: {full_name}")
    print(f"First name: {name_parts['first_name']}")
    print(f"Middle name: {name_parts['middle_name']}")
    print(f"Last name: {name_parts['last_name']}")

    # Task 2: Print file path
    current_path = print_file_path()
    print(f"\nCurrent file path: {current_path}")

    # Task 3: Extract baby names, sort them, and perform binary search
    # For demonstration, let's create a sample file with baby names including your first name
    sample_baby_names = """
    Common baby names include:
    Emma Noah Olivia Hope Ava Elijah Sophia William Isabella James
    Charlotte Benjamin Amelia Lucas Mia Mason Harper Ethan Evelyn Busola
    """

    baby_names_file = "baby_names.txt"
    with open(baby_names_file, 'w') as file:
        file.write(sample_baby_names)

    # Extract baby names
    baby_names = extract_baby_names(baby_names_file)
    print(f"\nExtracted baby names: {baby_names}")

    # Sort the names 
    sorted_names = custom_sort(baby_names)
    print(f"\nSorted baby names: {sorted_names}")

    # Perform binary search for your first name
    first_name = name_parts['first_name']
    position = binary_search(sorted_names, first_name)
    if position != -1:
        print(f"\nFound '{first_name}' at position {position} in the sorted list.")
    else:
        print(f"\n'{first_name}' not found in the list.")

    # Also search for your middle name
    middle_name = name_parts['middle_name']
    position = binary_search(sorted_names, middle_name)
    if position != -1:
        print(f"Found '{middle_name}' at position {position} in the sorted list.")
    else:
        print(f"'{middle_name}' not found in the sorted baby names list.")

