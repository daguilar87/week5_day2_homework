import requests 

def pokeapi(name):
        url =f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
        x = requests.get(url)
        data = x.json()
        
        poke = {
                'name' : data['name'],
                'ability' : data['abilities'][0]['ability']['name'],
                'sprites' : data['sprites']['front_shiny'],
                'hp' : data['stats'][0]['base_stat'],
                'attack' : data['stats'][1]['base_stat'],
                'defense' : data['stats'][2]['base_stat']}
        
        
    
        return poke

