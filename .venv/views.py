# views.py

from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from your_flask_app import app, mysql  # Replace "your_flask_app" with your actual Flask app name
from users import get_all_users, get_user_by_id, create_user, update_user, delete_user
from notes import get_all_notes, get_note_by_id, create_note, update_note, delete_note
from categories import get_all_categories, get_category_by_id, create_category, update_category, delete_category

@app.route('/')
def home():
    return render_template('index.html')

# Users

@app.route('/users', methods=['GET', 'POST'])
def users_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        result = create_user(data)
    else:
        result = get_all_users()
    return jsonify(result)

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def users_by_id_endpoint(id):
    if request.method == 'PUT':
        data = request.get_json()
        result = update_user(id, data)
    elif request.method == 'DELETE':
        result = get_user_by_id(id)
        if result is not None:
            result = delete_user(id)
        else:
            result = False
    else:
        result = get_user_by_id(id)
    return jsonify(result)

# Notes

@app.route('/notes', methods=['GET', 'POST'])
def notes_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        result = create_note(data)
    else:
        result = get_all_notes()
    return jsonify(result)

@app.route('/notes/<id>', methods=['GET', 'PUT', 'DELETE'])
def notes_by_id_endpoint(id):
    if request.method == 'PUT':
        data = request.get_json()
        result = update_note(id, data)
    elif request.method == 'DELETE':
        result = get_note_by_id(id)
        if result is not None:
            result = delete_note(id)
        else:
            result = False
    else:
        result = get_note_by_id(id)
    return jsonify(result)

# Categories

@app.route('/categories', methods=['GET', 'POST'])
def categories_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        result = create_category(data)
    else:
        result = get_all_categories()
    return jsonify(result)

@app.route('/categories/<id>', methods=['GET', 'PUT', 'DELETE'])
def categories_by_id_endpoint(id):
    if request.method == 'PUT':
        data = request.get_json()
        result = update_category(id, data)
    elif request.method == 'DELETE':
        result = get_category_by_id(id)
        if result is not None:
            result = delete_category(id)
        else:
            result = False
    else:
        result = get_category_by_id(id)
    return jsonify(result)
