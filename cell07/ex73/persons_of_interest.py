def famous_births(historical_figures):
    """
    Sorts and displays historical figures by birth date.

    Args:
        historical_figures (dict): A dictionary of historical figures with name and date of birth.
    """
    sorted_figures = sorted(historical_figures.items(), key=lambda item: item[1]["date_of_birth"])

    for key, figure_data in sorted_figures:
        print(f"{figure_data['name']} is a great scientist born in {figure_data['date_of_birth']}.")

if __name__ == "__main__":
    women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
    }
    famous_births(women_scientists)