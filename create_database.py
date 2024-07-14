import sqlite3

def create_database():
    conn = sqlite3.connect('MeditationTimer.db')
    cursor = conn.cursor()

#create Sessions table
    create_sessions_table = """
    CREATE TABLE IF NOT EXISTS Sessions (
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_time DATETIME,
        end_time DATETIME,
        duration_minutes INTEGER,
        notes TEXT
    )
    """
#
    create_sounds_table = """
    CREATE TABLE IF NOT EXISTS Sounds (
        sound_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        duration_seconds INTEGER,
        category TEXT
    )
    """

    create_session_sounds_table = """
    CREATE TABLE IF NOT EXISTS SessionSounds (
        session_id INTEGER,
        sound_id INTEGER,
        FOREIGN KEY(session_id) REFERENCES Sessions(session_id),
        FOREIGN KEY(sound_id) REFERENCES Sounds(sound_id),
        PRIMARY KEY(session_id, sound_id)
    )
    """

    cursor.execute(create_sessions_table)
    cursor.execute(create_sounds_table)
    cursor.execute(create_session_sounds_table)

    conn.commit()
    conn.close()

# Call create_database() function to create or update the database schema
create_database()

