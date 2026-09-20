import sqlite3


def create_database():
    connection = sqlite3.connect("roomcheck.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS timetable (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            start_time TEXT,
            end_time TEXT,
            room TEXT,
            teacher TEXT,
            subject TEXT,
            class TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_timetable(data):
    connection = sqlite3.connect("roomcheck.db")

    data.to_sql(
        "timetable",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()