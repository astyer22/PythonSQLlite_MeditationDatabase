import sqlite3  # Import the SQLite library for database operations
from datetime import datetime  # Import the datetime module for handling date and time

# Function to establish a connection to the SQLite database
def connect_db():
    return sqlite3.connect('MeditationTimer.db')

# Function to insert a new session into the Sessions table
def insert_session(start_time, end_time, duration_minutes, notes):
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute("""
    INSERT INTO Sessions (start_time, end_time, duration_minutes, notes)
    VALUES (?, ?, ?, ?)
    """, (start_time, end_time, duration_minutes, notes))  # Insert session data
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the database connection

# Function to retrieve all sessions from the Sessions table
def get_sessions():
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute("""
    SELECT * FROM Sessions
    """)  # Select all records from the Sessions table
    sessions = cursor.fetchall()  # Fetch all results
    conn.close()  # Close the database connection
    return sessions  # Return the list of sessions

# Function to update an existing session in the Sessions table
def update_session(session_id, start_time, end_time, duration_minutes, notes):
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute("""
    UPDATE Sessions
    SET start_time = ?, end_time = ?, duration_minutes = ?, notes = ?
    WHERE session_id = ?
    """, (start_time, end_time, duration_minutes, notes, session_id))  # Update session data
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the database connection

# Function to delete a session from the Sessions table
def delete_session(session_id):
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute("""
    DELETE FROM Sessions WHERE session_id = ?
    """, (session_id,))  # Delete session by session_id
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the database connection

# Function to insert a new sound into the Sounds table
def insert_sound(name, duration_minutes, category):
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute("""
    INSERT INTO Sounds (name, duration_minutes, category)
    VALUES (?, ?, ?)
    """, (name, duration_minutes, category))  # Insert sound data
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the database connection

# Function to retrieve all sounds from the Sounds table
def get_sounds():
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute("""
    SELECT * FROM Sounds
    """)  # Select all records from the Sounds table
    sounds = cursor.fetchall()  # Fetch all results
    conn.close()  # Close the database connection
    return sounds  # Return the list of sounds

# Function to update an existing sound in the Sounds table
def update_sound(sound_id, name, duration_minutes, category):
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute("""
    UPDATE Sounds
    SET name = ?, duration_minutes = ?, category = ?
    WHERE sound_id = ?
    """, (name, duration_minutes, category, sound_id))  # Update sound data
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the database connection

# Function to delete a sound from the Sounds table
def delete_sound(sound_id):
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute("""
    DELETE FROM Sounds WHERE sound_id = ?
    """, (sound_id,))  # Delete sound by sound_id
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the database connection

# Function to link a session with a sound in the SessionSounds table
def link_session_sound(session_id, sound_id):
    conn = connect_db()  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    cursor.execute("""
    INSERT INTO SessionSounds (session_id, sound_id)
    VALUES (?, ?)
    """, (session_id, sound_id))  # Insert the session-sound relationship
    conn.commit()  # Commit the changes to the database
    conn.close()  # Close the database connection
