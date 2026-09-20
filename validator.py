import pandas as pd


def validate_timetable(data):
    required_columns = [
        "date",
        "start_time",
        "end_time",
        "room",
        "teacher",
        "subject",
        "class"
    ]

    for column in required_columns:
        if column not in data.columns:
            return False, "Missing column: " + column

    if data.empty:
        return False, "Timetable is empty"

    return True, "Timetable is valid"