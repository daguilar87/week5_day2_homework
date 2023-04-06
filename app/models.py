from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

catch = db.Table(
    'catch',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), nullable=False, unique=True)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    caught = db.relationship('Pokemon',
            secondary = 'catch',
            backref= 'caught',
            lazy = 'dynamic'
            )

    def __init__(self, username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.wins = 0
        self.losses = 0
        

    def saveUser(self):
        db.session.add(self)
        db.session.commit()
    
    def unCatch(self, poke):
        self.caught.remove(poke)
        db.session.commit()
    
    def addCatch(self, poke):
        if poke not in self.caught:
            self.caught.append(poke)
            db.session.commit()
            return True
        else:
            return False
    
    def win(self):
        self.wins += 1
        db.session.commit()

    def lose(self):
        self.losses += 1
        db.session.commit()
    

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ability = db.Column(db.String)
    sprites = db.Column(db.String)
    hp = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    
    def __init__(self, name, ability, sprites, hp, defense, attack):
        self.name = name
        self.ability = ability
        self.sprites = sprites
        self.hp = hp
        self.defense = defense
        self.attack = attack
        

    def saveFind(self):
        db.session.add(self)
        db.session.commit()
