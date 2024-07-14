# app.py
from database import (
    insert_session, get_sessions, update_session, delete_session,
    insert_sound, get_sounds, update_sound, delete_sound,
    link_session_sound
)
from datetime import datetime, timedelta

def main():
    # Create a new session
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    end_time = (datetime.now() + timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
    insert_session(start_time, end_time, 30, 'Gettting over wedding coldfeet .')

    # Retrieve and print all sessions
    sessions = get_sessions()
    print("Sessions:")
    for session in sessions:
        print(session)

    # Create a new sound
    insert_sound('Dealth of a Bachelor', 90, 'Panic at the disco')

    # Retrieve and print all sounds
    sounds = get_sounds()
    print("Sounds:")
    for sound in sounds:
        print(sound)

    # Link a session with a sound
    if sessions and sounds:
        link_session_sound(sessions[0][0], sounds[0][0])

if __name__ == "__main__":
    main()
