# users.py

from database import fetchall, fetchone, execute

def create_user(data):
    cur = execute("""CALL InsertUser(%s, %s, %s, %s)""",
                  (data["username"], data["password"], data["email"]))
    row = cur.fetchone()
    data["userid"] = row["userid"]
    return data

def get_all_users():
    rv = fetchall(""" SELECT * FROM User""")
    return rv

def get_user_by_id(user_id):
    rv = fetchone("""SELECT * FROM User where userid = %s""", (user_id,))
    return rv

def update_user(user_id, data):
    cur = execute("""CALL UpdateUser(%s, %s, %s)""",
                  (user_id, data["username"], data["password"], data["email"]))
    row = cur.fetchone()
    data["userid"] = row["userid"]
    return data

def delete_user(user_id):
    cur = execute("""CALL DeleteUser(%s)""", (user_id,))
    row = cur.fetchone()
    if row is None:
        return True
    return False
