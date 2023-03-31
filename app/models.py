from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

catch = db.Table(
    'catch',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id'), nullable=False)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
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
        

    def saveUser(self):
        db.session.add(self)
        db.session.commit()
    
    def unCatch(self, poke):
        self.caught.remove(poke)
        db.session.commit()
    
    def addCatch(self, poke):
        self.caught.append(poke)
        db.session.commit()
    

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ability = db.Column(db.String)
    sprites = db.Column(db.String)
    hp = db.Column(db.String)
    defense = db.Column(db.String)
    attack = db.Column(db.String)
    # date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
                                #  notice          ^^^^^ --> lowercase?  yep.  User.id

    
    # def __init__(self, pname, user_id ):
    #     self.pname = pname
    #     self.user_id = user_id
    
    def __init__(self, name, ability, sprites, hp, defense, attack):
        self.name = name
        self.ability = ability
        self.sprites = sprites
        self.hp = hp
        self.defense = defense
        self.attack = attack
        # self.user_id = user_id

    def saveFind(self):
        db.session.add(self)
        db.session.commit()

    # def deletePoke(self):
    #     db.session.delete(self)
    #     db.session.commit()