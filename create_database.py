import sqlite3  # Import the SQLite library for database operations

def create_database():
    # Connect to the SQLite database 'MeditationTimer.db'
    # If the database does not exist, it will be created
    conn = sqlite3.connect('MeditationTimer.db')
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands

    # SQL command to create the Sessions table if it does not already exist
    create_sessions_table = """
    CREATE TABLE IF NOT EXISTS Sessions (
        session_id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique ID for each session
        start_time DATETIME,  # Start time of the meditation session
        end_time DATETIME,  # End time of the meditation session
        duration_minutes INTEGER,  # Duration of the session in minutes
        notes TEXT  # Optional notes about the session
    )
    """

    # SQL command to create the Sounds table if it does not already exist
    create_sounds_table = """
    CREATE TABLE IF NOT EXISTS Sounds (
        sound_id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique ID for each sound
        name TEXT,  # Name of the sound
        duration_minutes INTEGER,  # Duration of the sound in minutes
        category TEXT  # Category of the sound (e.g., music, nature)
    )
    """

    # SQL command to create the SessionSounds table for many-to-many relationships
    # between sessions and sounds, if it does not already exist
    create_session_sounds_table = """
    CREATE TABLE IF NOT EXISTS SessionSounds (
        session_sound_id INTEGER PRIMARY KEY AUTOINCREMENT,  # Unique ID for each session-sound relationship
        session_id INTEGER,  # ID of the session
        sound_id INTEGER,  # ID of the sound
        FOREIGN KEY(session_id) REFERENCES Sessions(session_id),  # Foreign key linking to the Sessions table
        FOREIGN KEY(sound_id) REFERENCES Sounds(sound_id)  # Foreign key linking to the Sounds table
    )
    """

    # Execute the SQL commands to create the tables
    cursor.execute(create_sessions_table)
    cursor.execute(create_sounds_table)
    cursor.execute(create_session_sounds_table)

    # Commit the changes to the database
    conn.commit()
    # Close the database connection
    conn.close()

# Call create_database() function to create or update the database schema
create_database()
