import os
import requests
import json

# Verifica y crea la carpeta 'pokedex' si no existe
if not os.path.exists('pokedex'):
    os.makedirs('pokedex')

def obtener_datos_pokemon(nombre_pokemon):
    """
    Obtiene los datos de un Pokémon de la API de PokeAPI.

    Args:
        nombre_pokemon (str): El nombre del Pokémon a buscar.

    Returns:
        dict: Un diccionario con la información del Pokémon, o None si no se encontró.
    """
    # Construye la URL de la API de PokeAPI con el nombre del Pokémon
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}'

    # Realiza una solicitud GET a la API de PokeAPI
    response = requests.get(url)

    # Verifica si el Pokémon existe (código de respuesta 404 indica que no existe)
    if response.status_code == 404:
        return None

    # Analiza la respuesta JSON de la API
    data = response.json()

    # Extrae la información relevante del Pokémon
    pokemon_info = {
        'Nombre': data['name'],
        'Peso': data['weight'],
        'Tamaño': data['height'],
        'Movimientos': [move['move']['name'] for move in data['moves']],
        'Habilidades': [ability['ability']['name'] for ability in data['abilities']],
        'Tipos': [t['type']['name'] for t in data['types']],
        'Imagen': data['sprites']['front_default']
    }

    return pokemon_info

def guardar_en_json(data, nombre_pokemon):
    """
    Guarda los datos de un Pokémon en un archivo JSON en la carpeta 'pokedex'.

    Args:
        data (dict): Un diccionario con la información del Pokémon.
        nombre_pokemon (str): El nombre del Pokémon.

    Returns:
        None
    """
    # Guarda los datos del Pokémon en un archivo JSON en la carpeta 'pokedex'
    with open(f'pokedex/{nombre_pokemon.lower()}.json', 'w') as archivo_json:
        json.dump(data, archivo_json, indent=4)

def main():
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")

    # Obtiene información del Pokémon
    pokemon_info = obtener_datos_pokemon(nombre_pokemon)

    if pokemon_info is None:
        print(f"No se encontró un Pokémon con el nombre {nombre_pokemon}.")
    else:
        # Muestra información del Pokémon en la consola
        print("Información del Pokémon:")
        for clave, valor in pokemon_info.items():
            print(f"{clave}: {valor}")

        # Guarda los datos en un archivo JSON
        guardar_en_json(pokemon_info, nombre_pokemon)
        print(f"Los datos se han guardado en pokedex/{nombre_pokemon.lower()}.json")

if __name__ == "__main__":
    main()
