def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
firt_name = input("John:")
middle_name = input("K:")
last_name = input ("Doe:")
musician = get_formatted_name('jimi', '', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')  
print(musician)