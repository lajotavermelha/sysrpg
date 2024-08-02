from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Character(db.Model):
    __tablename__ = 'characters'
    character_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String(100), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    class_ = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, default=1)
    strenght = db.Column(db.Integer, default=10)
    dexterity = db.Column(db.Integer, default=10)
    constituition =db.Column(db.Integer, default=10)
    intelligence = db.Column(db.Integer, default=10)
    wisdom = db.Column(db.Integer, default=10)
    charisma = db.Column(db.Integer, default=10)   
    background = db.Column(db.Text)
    inventory = db.Column(db.JSON, default=[])
    abilities = db.Column(db.JSON, default=[])
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
class Campaing(db.Model):
    __tablename__ = 'campaigns'
    campaigns_id = db.Column(db.Integer, primary_key=True)
    gm_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class CampaingCharacter(db.Model):
    __tablename__ = 'campaign_characters'
    campaign_character_id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaings.campaing_id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.character_id'))
    joined_at = db.Column(db.Integer, db.ForeignKey('campaings.campaign_id'))
    
class Session(db.Model):
    __tablename__ = 'sessions'
    session_id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id'))
    session_date = db.Column(db.Integer, db.ForeignKey('campaigns.campaign_id'))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Items(db.Model):
    __tablename__ = 'items'
    item_id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    item_type = db.Column(db.String(50), nullable=False)
    attributes = db.Column(db.JSON, default={})
    created_at = db.Colum(db.DateTime, default=datetime.utcnow)
    
class CharacterItem(db.Model):
    __tablename__ = 'character_items'
    character_item_id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.character_id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.item_id'))
    quantity = db.Column(db.Integer, default=1)
    acquired_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Ability(db.Model):
    __tablename__ = 'abilities'
    ability_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    ability_type = db.Column(db.String(50), nullable=False)
    effect = db.Column(db.Column(db.JSON, default={}))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class CharacterAbility(db.Model):
    __tablename__ = 'character_abilities'
    character_ability_id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.character_id'))
    ability_id = db.Column(db.Integer, db.ForeignKey('abilities.ability_id'))
    acquired_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Map(db.Model):
    __tablename__ = 'maps'
    map_id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaig.campaign_id'))
    name = db.Column(db.String(100))
    description = db.Column(db.text)
    map_data = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
class Combat(db.Model):
    __tablename__ = 'combat'
    combat_id = db.Column(db.Integer, prima
                          
                          )