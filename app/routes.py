from app import app

from flask import render_template, request, url_for, redirect
from .forms import Pokeform
import requests, json
from flask_login import current_user, login_user, logout_user
from .models import User

def pokeapi(name):
        url =f'https://pokeapi.co/api/v2/pokemon/{name}'
        x = requests.get(url)
        data = x.json()
        
        poke = {
                'ability' : data['abilities'][0]['ability']['name'],
                'name' : data['name'],
                'sprites' : data['sprites']['front_shiny'],
                'hp_base_experience' : data['stats'][0]['base_stat'],
                'attack_base_state' : data['stats'][1]['base_stat'],
                'defense_base_stat' : data['stats'][2]['base_stat']}
        
        
    
        return poke

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/poke',methods=['GET','POST'])
def pokePage():
    x = Pokeform()
    if request.method=='POST':
        name= x.name.data
        w = pokeapi(name)
        return render_template('poke.html', x=x, w=w)
    

   
    return render_template('poke.html', x=x)

