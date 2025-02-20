def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

first_name = input("Please enter your first name:")
middle_name = input("Please enter your middle name:")
last_name = input("Please enter your last name:")
print(get_formatted_name(first_name, middle_name, last_name))