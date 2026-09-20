def find_conflicts(data):
    conflicts = []

    for i in range(len(data)):
        for j in range(i + 1, len(data)):

            same_date = data.iloc[i]["date"] == data.iloc[j]["date"]
            same_time = (
                data.iloc[i]["start_time"] < data.iloc[j]["end_time"]
                and
                data.iloc[j]["start_time"] < data.iloc[i]["end_time"]
            )

            if same_date and same_time:

                same_room = data.iloc[i]["room"] == data.iloc[j]["room"]
                same_teacher = data.iloc[i]["teacher"] == data.iloc[j]["teacher"]

                if same_room:
                    conflicts.append(
                        "Room conflict: "
                        + str(data.iloc[i]["room"])
                        + " on "
                        + str(data.iloc[i]["date"])
                    )

                if same_teacher:
                    conflicts.append(
                        "Teacher conflict: "
                        + str(data.iloc[i]["teacher"])
                        + " on "
                        + str(data.iloc[i]["date"])
                    )

    return conflicts