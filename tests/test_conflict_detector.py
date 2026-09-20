import pandas as pd

from conflict_detector import find_conflicts


def create_test_data():
    data = pd.DataFrame({
        "date": [
            "2026-09-22",
            "2026-09-22",
            "2026-09-22",
            "2026-09-23"
        ],
        "start_time": [
            "10:00",
            "10:30",
            "11:00",
            "10:00"
        ],
        "end_time": [
            "11:00",
            "11:30",
            "12:00",
            "11:00"
        ],
        "room": [
            "A101",
            "A101",
            "A102",
            "A101"
        ],
        "teacher": [
            "Sharma",
            "Sharma",
            "Patil",
            "Sharma"
        ],
        "subject": [
            "Computer Networks",
            "Artificial Intelligence",
            "Data Structures",
            "Database"
        ],
        "class": [
            "TY CSE",
            "TY CSE",
            "TY CSE",
            "TY CSE"
        ]
    })

    return data


def test_room_conflict_is_detected():

    data = create_test_data()

    conflicts = find_conflicts(data)

    assert any(
        "Room conflict: A101" in conflict
        for conflict in conflicts
    )


def test_teacher_conflict_is_detected():

    data = create_test_data()

    conflicts = find_conflicts(data)

    assert any(
        "Teacher conflict: Sharma" in conflict
        for conflict in conflicts
    )


def test_different_date_is_not_a_conflict():

    data = create_test_data()

    conflicts = find_conflicts(data)

    date_conflicts = [
        conflict
        for conflict in conflicts
        if "2026-09-23" in conflict
    ]

    assert len(date_conflicts) == 0


def test_different_rooms_without_teacher_conflict():

    data = pd.DataFrame({
        "date": [
            "2026-09-22",
            "2026-09-22"
        ],
        "start_time": [
            "10:00",
            "10:00"
        ],
        "end_time": [
            "11:00",
            "11:00"
        ],
        "room": [
            "A101",
            "A102"
        ],
        "teacher": [
            "Sharma",
            "Patil"
        ],
        "subject": [
            "Computer Networks",
            "Artificial Intelligence"
        ],
        "class": [
            "TY CSE",
            "TY CSE"
        ]
    })

    conflicts = find_conflicts(data)

    assert len(conflicts) == 0


def test_non_overlapping_classes_are_not_conflicts():

    data = pd.DataFrame({
        "date": [
            "2026-09-22",
            "2026-09-22"
        ],
        "start_time": [
            "10:00",
            "11:00"
        ],
        "end_time": [
            "11:00",
            "12:00"
        ],
        "room": [
            "A101",
            "A101"
        ],
        "teacher": [
            "Sharma",
            "Sharma"
        ],
        "subject": [
            "Computer Networks",
            "Artificial Intelligence"
        ],
        "class": [
            "TY CSE",
            "TY CSE"
        ]
    })

    conflicts = find_conflicts(data)

    assert len(conflicts) == 0