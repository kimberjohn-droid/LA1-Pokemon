import requests
import random

pokemon_list = ["pikachu", "bulbasaur", "charmander", "squirtle", "eevee"]

pokemon_name = random.choice(pokemon_list)

try:
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    )

    if response.status_code == 200:
        data = response.json()

        name = data["name"]
        height = data["height"]
        weight = data["weight"]
        abilities = data["abilities"]

        print("Guess the Pokemon!")
        print("Height:", height / 10, "meters")
        print("Weight:", weight / 10, "kg")
        print("Abilities:")

        for ability in abilities:
            print("-", ability["ability"]["name"])

        for attempt in range(3):
            guess = input("Enter your guess: ").lower().strip()

            if guess not in pokemon_list:
                print("Invalid Pokemon name. Try again!")
            elif guess == name:
                print("Correct! You guessed", name.capitalize())
                break
            else:
                print("Wrong guess!")

        else:
            print("The Pokemon was", name.capitalize())

    else:
        print("Could not get Pokemon data.")

except requests.exceptions.RequestException:
    print("Network error. Check your internet connection.")
