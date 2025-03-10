def array_of_names(persons):
    """
    Builds an array of full names from a dictionary of first and last names.

    Args:
        persons (dict): A dictionary where keys are first names and values are last names.

    Returns:
        list: A list of full names with capitalized first letters.
    """
    full_names = []
    for first_name, last_name in persons.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        full_names.append(full_name)
    return full_names

if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))