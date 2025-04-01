import sqlite3

DB_PATH = "cafes.db"

def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row 
    return conn

def get_all_cafes():
    conn = get_db_connection()
    cafes = conn.execute("SELECT * FROM cafe").fetchall()
    conn.close()
    return [dict(cafe) for cafe in cafes]  

def add_cafe(name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price):
    """Insert a new cafe into the database."""
    try:
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO cafe
            (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price),
        )
        conn.commit()
        conn.close()
        return {"message": "Cafe added successfully!"}
    except Exception as e:
        return {"error": f"An error occurred while adding the cafe: {str(e)}"}

def delete_cafe(cafe_id):
    try:
        conn = get_db_connection()
        conn.execute("DELETE FROM cafe WHERE id = ?", (cafe_id,))
        conn.commit()
        conn.close()
        return {"message": f"Cafe with ID {cafe_id} deleted successfully!"}
    except Exception as e:
        return {"error": f"An error occurred while deleting the cafe: {str(e)}"}
