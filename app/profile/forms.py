from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Pokeform(FlaskForm):
    name = StringField('Pokemon Name')
    submit = SubmitField()

class PokeData():
    name= StringField('Pokemon Name',validators=[DataRequired()])
    ability = StringField('ability')
    img_url = StringField('img_url')
    hp = StringField('hp')
    defense = StringField('defense')
    attack = StringField('attack')

