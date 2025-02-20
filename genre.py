def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# Prompt the user to enter the musician's name
first_name = input("Enter the first name: ")
middle_name = input("Enter the middle name (leave blank if none): ")
last_name = input("Enter the last name: ")

# Prompt the user to select a genre
genres = ["Blues", "Pop", "Rock", "Hip Hop", "Jazz", "Electronic", "Folk"]
print("Select a genre:")
for i, genre in enumerate(genres, 1):
    print(f"{i}. {genre}")

genre_choice = int(input("Enter the number corresponding to the genre: "))
selected_genre = genres[genre_choice - 1]

musician = get_formatted_name(first_name, middle_name, last_name)
print(f"Musician: {musician}")
print(f"Genre: {selected_genre}")