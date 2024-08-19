from flask import request, jsonify, render_template, redirect, url_for, flash, session
from main import app, db
from models import *
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user

@app.route('/')
def barra():
    return redirect(url_for('login'))

@app.route('/index')
@login_required
def indexPage():
    return render_template('index.html')
@app.route('/register')
def registerPage():
    return render_template('register.html')

@app.route('/criarpersonagem')
def criarpersonagemPage():
    return render_template('criarpersonagem.html')

@app.route('/criarsessao')
def criarsessãoPage():
    return render_template('criarsessão.html')
@app.route('/criarsessão/npc')
def criarnpcPage():
    return render_template('npc.html')

@app.route('/criarsessão/Item')
def criarItemPage():
    return render_template('item.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('indexPage'))
        else:
            flash('Ususario ou senha invalidos')
    return render_template('login.html')

    return jsonify({'message': 'user created'}), 201
@app.route('/api/register', methods=['POST'])
def register():
    username = request.form['username']
    password_hash = generate_password_hash(request.form['password'])
    email = request.form['email']
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        flash('Ususario ja existe')
        return redirect(url_for('login'))
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        flash('Email ja em uso')
        return redirect(url_for('login'))
    novo_user = User(username=username, password_hash=password_hash, email=email)
    db.session.add(novo_user)
    db.session.commit()
    return redirect(url_for('login'))

@app.route('/api/characters', methods=['POST'])
def create_character():
    """Create a new character."""
    data = request.get_json()
    character = Character(
        name=data['name'],
        race=data['race'],
        classe=data['classe'],
        strength=data['strength'],
        dexterity=data['dexterity'],
        constitution=data['constitution'],
        intelligence=data['intelligence'],
        wisdom=data['wisdom'],
        charisma=data['charisma'],
        background=data['background'],
        inventory=data['inventory'],
        abilities=data['abilities']
    )
    db.session.add(character)
    db.session.commit()
    return jsonify({'message': 'Character created'}), 201

@app.route('/api/npc', methods=['POST', 'GET'])
def criarnpc():
    if request.method == 'POST':
        name = request.form['name']
        race = request.form['race']
        classe = request.form['classe']
        strength = request.form['força']
        dexterity = request.form['destreza']
        constitution = request.form['constituição']
        intelligence = request.form['inteligencia']
        wisdom = request.form['sabedoria']
        charisma = request.form['carisma']
        background = request.form['background']
        inventory = request.form['inventario']
        abilities = request.form['habilidade']
        novo_personagem = NPC(name=name,
                                    race=race,
                                    classe=classe,
                                    strength=strength,
                                    dexterity=dexterity,
                                    constitution=constitution,
                                    intelligence=intelligence,
                                    wisdom=wisdom,
                                    charisma=charisma,
                                    background=background,
                                    inventory=inventory,
                                    abilities=abilities
                                    )
        db.session.add(novo_personagem)
        db.session.commit()
        return redirect(url_for('criarsessãoPage'))
    elif request.method == 'GET':
        npcs = NPC.query.all()
        return jsonify([{'npc_id': n.npc_id,
                         'name': n.name,
                         'race': n.race,
                         'classe': n.classe,
                         'strength': n.strength,
                         'dexterity': n.dexterity,
                         'constitution': n.constitution,
                         'intelligence': n.intelligence,
                         'wisdom': n.wisdom,
                         'charisma': n.charisma,
                         'background': n.background,
                         'inventory': n.inventory,
                         'abilities': n.abilities
                         } for n in npcs])

@app.route('/api/npc/<int:npc_id>', methods=['DELETE'])
def delete_npc(npc_id):
    npc = NPC.query.get(npc_id)
    print(npc_id)
    if request.method == 'DELETE':
        db.session.delete(npc)
        db.session.commit()
        return jsonify({'message': 'NPC deleted'})

@app.route('/api/item', methods=['POST', 'GET'])
def item():
    if request.method == 'POST':
        name = request.form.get('name')
        descrição = request.form.get('descrição')
        item_type = request.form.get('item_type')
        attributes = request.form.get('atributos')
        novo_item = Item(name=name, description=descrição, item_type=item_type, attributes=attributes)
        db.session.add(novo_item)
        db.session.commit()
        return redirect(url_for('criarsessãoPage'))
    elif request.method =='GET':
        items = Item.query.all()
        return jsonify([{'item_id': i.item_id, 'name': i.name, 'description': i.description, 'item_type': i.item_type, 'attributes': i.attributes} for i in items])

@app.route('/api/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    print(item_id)
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'NPC deleted'})