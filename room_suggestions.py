
import pandas as pd


def suggest_rooms(data, date, start_time, end_time, rooms):

    available_rooms = []

    selected_date = pd.to_datetime(date).date()
    selected_start = pd.to_datetime(str(start_time)).time()
    selected_end = pd.to_datetime(str(end_time)).time()

    for room in rooms:

        room_is_busy = False

        for i in range(len(data)):

            row_date = pd.to_datetime(
                data.iloc[i]["date"]
            ).date()

            row_start = pd.to_datetime(
                str(data.iloc[i]["start_time"])
            ).time()

            row_end = pd.to_datetime(
                str(data.iloc[i]["end_time"])
            ).time()

            row_room = str(
                data.iloc[i]["room"]
            ).strip()

            same_date = row_date == selected_date
            same_room = row_room == room

            overlapping_time = (
                row_start < selected_end
                and
                selected_start < row_end
            )

            if same_date and same_room and overlapping_time:

                room_is_busy = True
                break

        if not room_is_busy:

            available_rooms.append(room)

    return available_rooms

