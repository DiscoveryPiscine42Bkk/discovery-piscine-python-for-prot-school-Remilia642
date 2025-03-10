def find_the_redheads(family_members):
    """
    Finds the first names of red-haired family members using filter.

    Args:
        family_members (dict): A dictionary where keys are first names and values are hair colors.

    Returns:
        list: A list of first names of red-haired individuals.
    """
    redheads = list(filter(lambda name: family_members[name] == "red", family_members))
    return redheads

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))
