import pandas as pd

from room_suggestions import suggest_rooms


def create_test_data():
    data = pd.DataFrame({
        "date": [
            "2026-09-22",
            "2026-09-22",
            "2026-09-23"
        ],
        "start_time": [
            "10:00",
            "11:00",
            "10:00"
        ],
        "end_time": [
            "11:00",
            "12:00",
            "11:00"
        ],
        "room": [
            "A101",
            "A102",
            "A101"
        ],
        "teacher": [
            "Sharma",
            "Patil",
            "Joshi"
        ],
        "subject": [
            "Computer Networks",
            "Artificial Intelligence",
            "Data Structures"
        ],
        "class": [
            "TY CSE",
            "TY CSE",
            "TY CSE"
        ]
    })

    return data


def test_available_room_is_suggested():

    data = create_test_data()

    rooms = [
        "A101",
        "A102",
        "A103"
    ]

    available = suggest_rooms(
        data,
        "2026-09-22",
        "10:00",
        "11:00",
        rooms
    )

    assert "A103" in available


def test_occupied_room_is_not_suggested():

    data = create_test_data()

    rooms = [
        "A101",
        "A102",
        "A103"
    ]

    available = suggest_rooms(
        data,
        "2026-09-22",
        "10:00",
        "11:00",
        rooms
    )

    assert "A101" not in available


def test_room_available_on_different_time():

    data = create_test_data()

    rooms = [
        "A101",
        "A102",
        "A103"
    ]

    available = suggest_rooms(
        data,
        "2026-09-22",
        "12:00",
        "13:00",
        rooms
    )

    assert "A101" in available
    assert "A102" in available
    assert "A103" in available