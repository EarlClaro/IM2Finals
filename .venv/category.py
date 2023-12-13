from database import fetchall, fetchone, execute

def create_category(data):
    # Create a new category in the database
    cur = execute("""INSERT INTO Category (name) VALUES (%s)""", (data["name"],))
    return fetchone("SELECT LAST_INSERT_ID() as categoryID")

def get_all_categories():
    # Retrieve all categories from the database
    return fetchall("""SELECT * FROM Category""")

def get_category_by_id(category_id):
    # Retrieve a specific category by ID from the database
    return fetchone("""SELECT * FROM Category WHERE categoryID = %s""", (category_id,))

def update_category(category_id, data):
    # Update a category in the database
    execute("""UPDATE Category SET name = %s WHERE categoryID = %s""",
            (data["name"], category_id))
    return {"categoryID": category_id, "name": data["name"]}

def delete_category(category_id):
    # Delete a category from the database
    cur = execute("""DELETE FROM Category WHERE categoryID = %s""", (category_id,))
    return cur.rowcount > 0
