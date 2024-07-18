# app.py

# Import necessary functions from the database module
from database import (
    insert_session, get_sessions, update_session, delete_session,
    insert_sound, get_sounds, update_sound, delete_sound,
    link_session_sound
)
from datetime import datetime, timedelta  # Import datetime and timedelta for handling date and time

def main():
    # Create a new session
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Get the current date and time as the start time
    end_time = (datetime.now() + timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')  # Set the end time to 30 minutes from now
    insert_session(start_time, end_time, 30, 'Getting over wedding cold feet.')  # Insert the new session into the database

    # Retrieve and print all sessions
    sessions = get_sessions()  # Get all sessions from the database
    print("Sessions:")  # Print a header for the sessions
    for session in sessions:
        print(session)  # Print each session

    # Create a new sound
    insert_sound('Death of a Bachelor', 90, 'Panic at the Disco')  # Insert a new sound into the database

    # Retrieve and print all sounds
    sounds = get_sounds()  # Get all sounds from the database
    print("Sounds:")  # Print a header for the sounds
    for sound in sounds:
        print(sound)  # Print each sound

    # Link a session with a sound
    if sessions and sounds:  # Check if there are any sessions and sounds available
        link_session_sound(sessions[0][0], sounds[0][0])  # Link the first session with the first sound

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
