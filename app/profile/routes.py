from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required

from ..models import Pokemon
import requests, json
# from ..routes import pokeapi
from .forms import Pokeform, PokeData
from..services import pokeapi

profile = Blueprint('profile', __name__, template_folder='profile_templates')


@profile.route('/find', methods=['GET', 'POST'])
@login_required
def findPokes():
    form = Pokeform()
    if request.method=='POST':
            pname= form.name.data
            print('POST')
            check = Pokemon.query.filter_by(name=pname).first()
            if check:
                print('check')
                return render_template('find.html', check=check, form=form)
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
                return render_template('find.html', check=check, form=form)

    return render_template('find.html', form=form)


# @app.route('/poke',methods=['GET','POST'])
# def pokePage():
#     x = Pokeform()
#     if request.method=='POST':
#         name= x.name.data
#         w = pokeapi(name)
#         return render_template('poke.html', x=x, w=w)
    

   
#     return render_template('poke.html', x=x)


