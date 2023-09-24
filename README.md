# M4Python
Pokedex

# Pokédex en Python

Este proyecto es una Pokédex simple construida en Python que utiliza la API de PokeAPI para obtener información sobre Pokémon. Permite a los usuarios buscar Pokémon por nombre y muestra sus datos, incluyendo nombre, peso, tamaño, movimientos, habilidades, tipos e imagen. Además, guarda los datos de cada Pokémon en archivos JSON en una carpeta llamada "pokedex".

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instalada la librería `requests`. Puedes instalarla usando pip:
pip install requests

Uso
Clona este repositorio en tu máquina local o descarga los archivos.
Ejecuta el programa principal pokedex.py usando Python:
python pokedex.py
El programa te pedirá que introduzcas el nombre de un Pokémon. Puedes escribir el nombre de cualquier Pokémon, como "Pikachu" o "Charizard".
El programa buscará el Pokémon en la API de PokeAPI y mostrará sus datos en la consola, así como guardará los datos en un archivo JSON en la carpeta "pokedex" si el Pokémon existe. Si el Pokémon no existe, mostrará un mensaje de error.

Estructura de Archivos
pokedex.py: El programa principal que permite buscar y mostrar datos de Pokémon.
pokedex/: Una carpeta que almacena archivos JSON con información de Pokémon.

Contribuciones
Este proyecto utiliza la API de PokeAPI (https://pokeapi.co/).
