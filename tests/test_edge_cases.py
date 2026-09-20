import pandas as pd

from validator import validate_timetable


def test_empty_timetable():

    data = pd.DataFrame(columns=[
        "date",
        "start_time",
        "end_time",
        "room",
        "teacher",
        "subject",
        "class"
    ])

    valid, message = validate_timetable(data)

    assert valid is False
    assert message == "Timetable is empty"


def test_missing_room_column():

    data = pd.DataFrame({
        "date": ["2026-09-22"],
        "start_time": ["10:00"],
        "end_time": ["11:00"],
        "teacher": ["Sharma"],
        "subject": ["Computer Networks"],
        "class": ["TY CSE"]
    })

    valid, message = validate_timetable(data)

    assert valid is False
    assert "Missing column: room" in message


def test_missing_teacher_column():

    data = pd.DataFrame({
        "date": ["2026-09-22"],
        "start_time": ["10:00"],
        "end_time": ["11:00"],
        "room": ["A101"],
        "subject": ["Computer Networks"],
        "class": ["TY CSE"]
    })

    valid, message = validate_timetable(data)

    assert valid is False
    assert "Missing column: teacher" in message


def test_valid_timetable():

    data = pd.DataFrame({
        "date": ["2026-09-22"],
        "start_time": ["10:00"],
        "end_time": ["11:00"],
        "room": ["A101"],
        "teacher": ["Sharma"],
        "subject": ["Computer Networks"],
        "class": ["TY CSE"]
    })

    valid, message = validate_timetable(data)

    assert valid is True
    assert message == "Timetable is valid"