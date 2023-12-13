# notes.py

from database import fetchall, fetchone, execute

def create_note(data):
    # Placeholder for creating a new note in the database
    cur = execute("""CALL InsertNote(%s, %s, %s, %s)""",
                  (data["userid"], data["categoryID"], data["title"], data["content"]))
    row = cur.fetchone()
    data["noteID"] = row["noteID"]
    return data

def get_all_notes():
    # Placeholder for retrieving all notes from the database
    rv = fetchall(""" SELECT * FROM AllNotesView """)
    return rv

def get_note_by_id(note_id):
    # Placeholder for retrieving a specific note by ID from the database
    rv = fetchone("""SELECT * FROM AllNotesView WHERE noteID = %s""", (note_id,))
    return rv

def update_note(note_id, data):
    # Placeholder for updating a note in the database
    cur = execute("""CALL UpdateNote(%s, %s, %s)""",
                  (note_id, data["title"], data["content"]))
    row = cur.fetchone()
    data["noteID"] = row["noteID"]
    return data

def delete_note(note_id):
    # Placeholder for deleting a note from the database
    cur = execute("""CALL DeleteNote(%s)""", (note_id,))
    row = cur.fetchone()
    if row is None:
        return True
    return False
