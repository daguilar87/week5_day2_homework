from app import app

from flask import render_template, request, url_for, redirect
from .forms import Pokeform
import requests, json
from flask_login import current_user, login_user, logout_user
from .models import User

def pokeapi(name):
        url =f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
        x = requests.get(url)
        data = x.json()
        
        poke = {
                'name' : data['name'],
                'ability' : data['abilities'][0]['ability']['name'],
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
        return render_template('find.html', x=x, w=w)
    

   
    return render_template('poke.html', x=x)

    # for p in p_list:
    #     check = Pokemon.query.filter_by(name=p).first()
    #     if check:
    #         return render_template('find.html', check=check, w=w)
    #     else:
    #         poke = pokeapi(p)
    #         ability = poke['ability']
    #         sprites = poke['sprites']
    #         hp = poke['hp']
    #         defense = poke['defense']
    #         attack = poke['attack']

    #         new = Pokemon(p, ability, sprites, hp, defense, attack)
    #         new.saveFind()
    # return render_template('find.html', new=new, w=w)
