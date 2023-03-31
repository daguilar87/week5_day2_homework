from app import app

from flask import render_template, request, url_for, redirect, flash
from .forms import Pokeform
import requests, json
from flask_login import current_user, login_user, logout_user, login_required
from .models import User, Pokemon, catch
from .services import pokeapi
from sqlalchemy import desc

# def pokeapi(name):
#         url =f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
#         x = requests.get(url)
#         data = x.json()
        
#         poke = {
#                 'name' : data['name'],
#                 'ability' : data['abilities'][0]['ability']['name'],
#                 'sprites' : data['sprites']['front_shiny'],
#                 'hp_base_experience' : data['stats'][0]['base_stat'],
#                 'attack_base_state' : data['stats'][1]['base_stat'],
#                 'defense_base_stat' : data['stats'][2]['base_stat']}
        
        
    
#         return poke

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/poke',methods=['GET','POST'])
@login_required
def pokePage():

    form = Pokeform()
    if request.method=='POST':
            pname= form.name.data
            print('POST')
            check = Pokemon.query.filter_by(name=pname).first()
            if check:
                print('check')
                return render_template('poke.html', check=check, form=form, u=current_user)
            else:
                print('else')
                poke = pokeapi(pname)
                ability = poke['ability']
                sprites = poke['sprites']
                hp = poke['hp']
                defense = poke['defense']
                attack = poke['attack']

                check = Pokemon(pname, ability, sprites, hp, defense, attack)
                check.saveFind()
                print('bottom')
                return render_template('poke.html', check=check, form=form, u=current_user)

    return render_template('poke.html', form=form, u=current_user)

@app.route('/posts/like/<int:pokemon_id>')
@login_required
def catchP(pokemon_id):
    poke= Pokemon.query.get(pokemon_id)
    my_p = current_user.caught.all()
    print(my_p)
    if poke in my_p or len(my_p) > 4:
        flash(f"You've already caught that pokemon!", category='warning')
    else:
        current_user.addCatch(poke)
        flash(f"Succesfully caught!", category='success')
    return redirect(url_for('feed') )

@app.route('/pokemon/feed')
@login_required
def feed():
    t_list= current_user.caught.all()

    return render_template('feed.html',  t=t_list)


@app.route('/remove/<int:pokemon_id>')
@login_required
def releaseP(pokemon_id):
    poke= Pokemon.query.get(pokemon_id)
    my_p = current_user.caught.all()
    if poke in my_p:
        current_user.unCatch(poke)
        flash(f"Succesfully caught!", category='success')
    return redirect(url_for('feed', poke= poke) )


