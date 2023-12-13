from flask import Flask, request, jsonify
from notes import get_all_notes, get_note_by_id, create_note, update_note, delete_note
from category import get_all_categories, get_category_by_id, create_category, update_category, delete_category
from flask_mysqldb import MySQL
from database import set_database

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "July82001Cl@ro"
app.config["MYSQL_DB"] = "notes"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_AUTOCOMMIT"] = True 

mysql = MySQL(app)
set_database(mysql)

# Notes

@app.route("/notes", methods=["GET", "POST"])
def notes_endpoint():
    if request.method == "POST":
        data = request.get_json()
        result = create_note_procedure(data)
    else:
        result = get_all_notes()
    return jsonify(result)

@app.route("/notes/<id>", methods=["GET", "PUT", "DELETE"])
def notes_by_id_endpoint(id):
    if request.method == "PUT":
        data = request.get_json()
        result = update_note_procedure(id, data)
    elif request.method == "DELETE":
        result = get_note_by_id(id)
        if result is not None:
            result = delete_note_procedure(id)
        else:
            result = {"error": "Note not found"}
    else:
        result = get_note_by_id(id)
    return jsonify(result)

# Categories

@app.route("/category", methods=["GET", "POST"])
def categories_endpoint():
    if request.method == "POST":
        data = request.get_json()
        result = create_category_procedure(data)
    else:
        result = get_all_categories()
    return jsonify(result)

@app.route("/category/<id>", methods=["GET", "PUT", "DELETE"])
def categories_by_id_endpoint(id):
    if request.method == "PUT":
        data = request.get_json()   
        result = update_category_procedure(id, data)
    elif request.method == "DELETE":
        success = delete_category_procedure(id)
        if success:
            return "<p>You just deleted category with ID {}</p>".format(id)
        else:
            return "<p> Category with ID {} not found</p>".format(id)
    else:
        result = get_category_by_id(id)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
