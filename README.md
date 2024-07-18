I am in the process of creating a meditation timer application. Apart of this application requires a databse to store user information and other application details like sessions and sounds. I created the database using python and SQLite3. 

[Software Demo Video](https://youtu.be/7TQRV6ZMye4)

# Relational Database

For the relational database I decided to use SQLite3. This database platform is fairly light weight and easy to use. I had never used SQLlite before but was very familar with SQL. 

The relational database (MeditationTimer.db) for the meditation timer app consists of three main tables: Sessions (stores details like session name, start time, and duration), Sounds (holds information about sounds available for meditation), and SessionSounds (facilitates a many-to-many relationship between sessions and sounds). This structure allows users to manage and associate multiple sounds with each meditation session effectively.

# Development Environment

Python was used for backend logic and SQLite3 for database operations. SQLiteStudio was utilized for designing and managing the SQLite database (MeditationTimer.db).

The programming language used for developing the meditation timer app was Python. Python's standard library, particularly sqlite3, was utilized for database operations with SQLite. Additionally, no specific additional libraries used for this project beyond the standard libraries provided by Python.

# Useful Websites

- [wikipedia](https://en.wikipedia.org/wiki/Relational_database)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python](https://docs.python.org/3/library/sqlite3.html)
- [tutorialspoint point](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

# Future Work

- Address any inconsistencies or errors in database operations.
- Implement error handling and user feedback mechanisms.
- Introduce advanced timer functionalities like interval timers or customizable session settings.
