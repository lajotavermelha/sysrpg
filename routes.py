from flask import request, jsonify, render_template, redirect, url_for, flash, session
from main import app, db
from models import *
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user, current_user

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

@app.route('/api/register', methods=['POST'])
def register():
    username = request.form['username']
    password_hash = generate_password_hash(request.form['password'])
    email = request.form['email']
    novo_user = User(username=username, password_hash=password_hash, email=email)
    db.session.add(novo_user)
    db.session.commit()
    return redirect(url_for('login')), 201
    return jsonify({'message': 'usuario criado'}), 201

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
        
