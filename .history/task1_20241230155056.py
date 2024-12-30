import requests
import json


def fetch_pokemon_data(pokemon_name): 
    url = 'https://pokeapi.co/api/v2/pokemon'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        print("Unable to locate data for {pokemon_name}")
        return None

def calculate_average_weight(pokemon_list):
    total_weight = 0
    count = 0

    for pokemon in pokemon_list:
        data = fetch_pokemon_data(pokemon)

        if data:
            total_weight += data['weight']
            count += 1

    if count > 0:
        return total_weight / count
    else:
        return 0 

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

for pokemon in pokemon_names:
    data = fetch_pokemon_data(pokemon)

    if data:
        pokemon_name = data['name']
        abilities = [ability['ablity']['name'] for ability in data['abilities']]

        print(f'Pokemon Name: {pokemon_name}')
        print('Abilities:')
        for ability in abilities:
            print(f' {ability}')
        print()

average_weight = calculate_average_weight(pokemon_names)
print(f'Average Weight of our Pokemon: {average_weight} hectograms')