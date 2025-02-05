import sqlite3

def init_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)")
    conn.commit()
    conn.close()

def save_note(content):
    """Saves a new note"""
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()

def update_note(note_id, content):
    """Updates an existing note"""
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET content=? WHERE id=?", (content, note_id))
    conn.commit()
    conn.close()

def delete_note(note_id):
    """Deletes a note from the database"""
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()

def get_notes():
    """Retrieve all saved notes"""
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, content FROM notes")
    notes = cursor.fetchall()
    conn.close()
    return notes

def get_note_by_id(note_id):
    """Retrieve a single note by ID"""
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM notes WHERE id=?", (note_id,))
    note = cursor.fetchone()
    conn.close()
    return note[0] if note else ""

# Initialize the database
init_db()
