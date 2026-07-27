
def slugify(text):
    # Convert the entire string to lowercase
    text = text.lower()

    # This list will store the final characters
    result = []

    # This flag keeps track of whether the last character added was a dash
    last_was_dash = False
