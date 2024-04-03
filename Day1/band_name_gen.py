def generate_band_name(city: str, pet: str) -> str:
    return f"Your band name could be {city} {pet}"


print("Welcome to band name generator!")
city_name = input("What is the name of the city you grew up in?: \n")
pet_name = input("What is the name of your pet?: \n")
print(generate_band_name(city_name, pet_name))
