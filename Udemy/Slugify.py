
def slugify(text):
    # Convert the entire string to lowercase
    text = text.lower()

    # This list will store the final characters
    result = []

    # This flag keeps track of whether the last character added was a dash
    last_was_dash = False
    # Go through every character in the string
    for char in text:

        # If the character is a letter or a digit, keep it
        if char.isalnum():
            result.append(char)
            last_was_dash = False

        # If the character is not a letter or digit
        # (space, punctuation, symbols, etc.)
        else:
            # Add only one dash for consecutive special characters
            if not last_was_dash:
                result.append("-")
                last_was_dash = True

    # Join the list into a string
    slug = "".join(result)

    # Remove dashes from the beginning and end
    slug = slug.strip("-")

    return slug


# -------------------- Test Cases --------------------

print(slugify("hey you are good"))
# Output: hey-you-are-good

print(slugify("Hello, World!"))
# Output: hello-world

print(slugify("Python & Django @ 2025"))
# Output: python-django-2025

print(slugify("   multiple    spaces   "))
# Output: multiple-spaces

print(slugify("This_is_a_test"))
# Output: this-is-a-test

print(slugify("C++ Programming Language"))
# Output: c-programming-language

print(slugify("100% Guaranteed!!!"))
# Output: 100-guaranteed

print(slugify("What's your name?"))
# Output: what-s-your-name

print(slugify("John.Doe@example.com"))
# Output: john-doe-example-com


print(slugify(""))
# Output: ""

print(slugify("----"))
# Output: ""

print(slugify("123456"))
# Output: 123456

print(slugify("Hello---World"))
# Output: hello-world


print(slugify("AI/ML\\Data Science"))
# Output: ai-ml-data-science
