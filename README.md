#  RoomCheck

### Smarter Timetables. Better Rooms.

RoomCheck is a Python and Streamlit-based timetable analysis application that helps identify classroom conflicts and find available rooms for a selected date and time.

---

##  Problem Statement

Managing classroom timetables manually can make it difficult to identify room clashes and quickly find available classrooms.

RoomCheck provides a simple way to upload a timetable, analyze classroom usage, detect conflicts, and suggest available rooms.

---

## Solution

RoomCheck reads timetable data from an Excel file and analyzes:

* Classroom availability
* Room conflicts
* Teacher conflicts
* Overlapping classes
* Alternative available rooms

The results are displayed through a simple Streamlit dashboard.

---

##  Features

* Upload Excel timetable
* Validate timetable structure
*  Detect occupied and available rooms
* Detect room conflicts
*  Detect teacher conflicts
*  Suggest available rooms
*  Display timetable summary
* Check availability for a selected date
*  Check availability for a selected time range
*  Store timetable data using SQLite
*  Automated testing using pytest

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Streamlit**
* **SQLite**
* **OpenPyXL**
* **Pytest**

---

## Project Structure

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
```

> `roomcheck.db` is created locally when the application runs and is excluded from GitHub using `.gitignore`.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/manaalmulla06/RoomCheck.git
```

### 2. Open the project folder

```bash
cd RoomCheck
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run:

```bash
streamlit run app.py
```

The RoomCheck application will open in your browser.

---

## Running Tests

Run all automated tests using:

```bash
python -m pytest
```

The project currently contains **15 automated tests** covering:

* Timetable validation
* Edge cases
* Room suggestions
* Room conflicts
* Teacher conflicts
* Non-overlapping classes

---

## How RoomCheck Works

```text
Excel Timetable
       ↓
Upload File
       ↓
Validate Timetable
       ↓
Read Room & Schedule Data
       ↓
Detect Conflicts
       ↓
Check Selected Date & Time
       ↓
Find Available Rooms
       ↓
Suggest Available Rooms
       ↓
Display Results
```

---

## 📄 Required Excel Columns

The uploaded Excel timetable must contain the following columns:

| Column       | Description             |
| ------------ | ----------------------- |
| `date`       | Class date              |
| `start_time` | Class start time        |
| `end_time`   | Class end time          |
| `room`       | Classroom or laboratory |
| `teacher`    | Faculty/teacher name    |
| `subject`    | Subject name            |
| `class`      | Class or division       |

### Example

| date       | start_time | end_time | room | teacher | subject           | class  |
| ---------- | ---------- | -------- | ---- | ------- | ----------------- | ------ |
| 2026-09-22 | 10:00      | 11:00    | A101 | Sharma  | Computer Networks | TY CSE |

---

## Conflict Detection

RoomCheck identifies conflicts when two classes:

1. Occur on the same date
2. Have overlapping time periods
3. Use the same room

It also identifies teacher conflicts when the same teacher is assigned to overlapping classes.

---

## Room Suggestions

For a selected date and time range, RoomCheck checks the rooms found in the uploaded timetable.

A room is suggested when it does not have an overlapping class during the selected period.

The application obtains room information dynamically from the uploaded timetable rather than using a fixed list of rooms.

---

## Data Handling

RoomCheck stores timetable information locally using SQLite.
The local database file `roomcheck.db` is excluded from version control using `.gitignore`.

---

## Future Scope

Possible future improvements include:

* User authentication
* Multiple building support
* Timetable editing
* Admin dashboard
* Database-based timetable management
* Automatic timetable generation
* Email or notification support
* Deployment as a web application

---

##Project Status

**Completed Prototype**

The current version includes:

* Excel timetable processing
* Data validation
* Room conflict detection
* Teacher conflict detection
* Room availability checking
* Room suggestions
* Streamlit dashboard
* SQLite storage
* Automated tests

---

## Project

**RoomCheck — Smarter Timetables. Better Rooms.**
