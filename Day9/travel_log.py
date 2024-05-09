"""
write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
Create a function that can add new countries to this list.

add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

Example Input
Brazil
5
["Sao Paulo", "Rio de Janeiro"]
Example Output
I've been to Brazil 5 times.
My favourite city was Sao Paulo.

"""

country = input("What new country have you been to?: ")  # Add country name
visits = int(input("How many times did you visit the places there?: "))  # Number of visits
list_of_cities = eval(input("List the cities you visited: "))  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# function that will allow new countries
def add_new_country(destination: str, number_of_visits: int, cities: list) -> None:
    # duplicate the log of an existing entry in the travel_log
    log = travel_log[1]
    # modify the duplicated log to reference the new country
    log["country"] = destination
    log["visits"] = number_of_visits
    log["cities"] = cities
    travel_log.append(log)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
