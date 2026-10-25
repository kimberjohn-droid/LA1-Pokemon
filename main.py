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
