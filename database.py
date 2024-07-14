import sqlite3
from datetime import datetime

def connect_db ():
    return sqlite3.connect('MeditationTimer.db')

def insert_session (start_time, end_time, duration_minutes, notes):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Sessions (start_time, end_time, duration_minutes, notes)
    VALUES (?, ?, ?, ?)
    """, (start_time, end_time, duration_minutes, notes))
    conn.commit()
    conn.close()

def get_sessions():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM Sessions
    """)
    sessions = cursor.fetchall()
    conn.close()
    return sessions

def update_session(session_id, start_time, end_time, duration_minutes, notes):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE Sessions
    SET start_time = ?, end_time = ?, duration_minutes = ?, notes = ?
    WHERE session_id = ?
    """, (start_time, end_time, duration_minutes, notes, session_id))
    conn.commit()
    conn.close()

def delete_session(session_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM Sessions WHERE session_id = ?
    """, (session_id,))
    conn.commit()
    conn.close()

def insert_sound(name, duration_sounds, category):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Sounds (name, duration_seconds, category)
    VALUES (?, ?, ?)
    """, (name, duration_sounds, category))
    conn.commit()
    conn.close()

def get_sounds():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM Sounds
    """)
    sounds = cursor.fetchall()
    conn.close()
    return sounds

def update_sound(sound_id, name, duration_seconds, category):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE Sounds
     SET name = ?, duration_seconds = ?, category = ?
    WHERE sound_id = ?
    """, (name, duration_seconds, category, sound_id))
    conn.commit()
    conn.close()

def delete_sound(sound_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM Sounds WHERE sound_id = ?
    """, (sound_id,))
    conn.commit()
    conn.close()

def link_session_sound(session_id, sound_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO SessionSounds (session_id, sound_id)
    VALUES (?, ?)
    """, (session_id, sound_id))
    conn.commit()
    conn.close()