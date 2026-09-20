# 🏫 RoomCheck

### Smarter Timetables. Better Rooms.

RoomCheck is a Python and Streamlit-based timetable analysis application that helps identify classroom conflicts and find available rooms for a selected date and time.

---

## 📌 Problem Statement

Managing classroom timetables manually can make it difficult to identify room clashes and quickly find available classrooms.

RoomCheck provides a simple way to upload a timetable, analyze classroom usage, detect conflicts, and suggest available rooms.

---

## 💡 Solution

RoomCheck reads timetable data from an Excel file and analyzes:

- Classroom availability
- Room conflicts
- Teacher conflicts
- Overlapping classes
- Alternative available rooms

The results are displayed through a simple Streamlit dashboard.

---

## ✨ Features

- 📤 Upload Excel timetable
- ✅ Validate timetable structure
- 🏢 Detect occupied and available rooms
- ⚠️ Detect room conflicts
- 👨‍🏫 Detect teacher conflicts
- 💡 Suggest available rooms
- 📊 Display timetable summary
- 📅 Check availability for a selected date
- 🕐 Check availability for a selected time range
- 🗄️ Store timetable data using SQLite
- 🧪 Automated testing using pytest

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Streamlit**
- **SQLite**
- **OpenPyXL**
- **Pytest**

---

## 📁 Project Structure

```text
RoomCheck/
│
├── data/
│   └── timetable.xlsx
│
├── tests/
│   ├── test_conflict_detector.py
│   ├── test_edge_cases.py
│   ├── test_room_suggestions.py
│   └── test_validator.py
│
├── app.py
├── validator.py
├── conflict_detector.py
├── database.py
├── room_suggestions.py
├── requirements.txt
├── .gitignore
└── README.md