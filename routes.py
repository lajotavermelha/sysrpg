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

@app.route('/criarsessão')
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

@app.route('/api/criarpersonagem', methods=['POST', 'GET'])
def criarpersonagem():
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
        novo_personagem = Character(name=name,
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
        return jsonify({'message': 'personagem criado'}), 201
        
#TODO conserta esta porra
@app.route('/api/item', methods=['POST', 'GET'])
def item():
    if request.method == 'POST':
        name = request.form.get('name')
        descrição = request.form.get('descrição')
        item_type = request.form.get('item-type')
        attributes = request.form.get('atributos')
        print(item_type)
        novo_item = Item(name=name, description=descrição, item_type=item_type, attributes=attributes)
        db.session.add(novo_item)
        db.session.commit()
        return jsonify({'message': 'item criado'}), 201
    elif request.method =='GET':
        items = Item.query.all()
        return jsonify([{'name': i.name, 'description': i.description, 'item_type': i.item_type, 'attributes': i.attributes} for i in items])
