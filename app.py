import streamlit as st
import pandas as pd

from validator import validate_timetable
from conflict_detector import find_conflicts
from database import create_database, save_timetable
from room_suggestions import suggest_rooms


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="RoomCheck",
    page_icon="🏫",
    layout="wide"
)


# --------------------------------------------------
# SIMPLE PAGE STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>

    .block-container {
        padding-top: 2rem;
        padding-left: 4rem;
        padding-right: 4rem;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🏫 RoomCheck")

st.markdown(
    '<div class="subtitle">Smarter Timetables. Better Rooms.</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# UPLOAD TIMETABLE
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("📤 Upload Timetable")

    st.write(
        "Upload your Excel timetable to detect conflicts "
        "and find available rooms."
    )

    uploaded_file = st.file_uploader(
        "Choose your Excel timetable",
        type=["xlsx"]
    )


# --------------------------------------------------
# BUILDING DETAILS
# --------------------------------------------------

with col2:

    st.subheader("🏢 Building Details")

    building_name = st.text_input(
        "Building Name"
    )

    total_rooms = st.number_input(
        "Total Number of Rooms",
        min_value=1,
        step=1
    )


# --------------------------------------------------
# DATE AND TIME
# --------------------------------------------------

st.subheader("📅 Check Room Availability")

date_col, start_col, end_col = st.columns(3)


with date_col:

    selected_date = st.date_input(
        "Date"
    )


with start_col:

    start_time = st.time_input(
        "Start Time"
    )


with end_col:

    end_time = st.time_input(
        "End Time"
    )


# --------------------------------------------------
# CHECK TIMETABLE
# --------------------------------------------------

if st.button(
    "🔍 Check Timetable",
    use_container_width=True
):

    # Check file

    if uploaded_file is None:

        st.warning(
            "Please upload an Excel timetable first."
        )

    # Check building name

    elif not building_name.strip():

        st.warning(
            "Please enter the building name."
        )

    # Check room count

    elif total_rooms < 1:

        st.warning(
            "Please enter a valid number of rooms."
        )

    # Check time

    elif start_time >= end_time:

        st.error(
            "End time must be later than start time."
        )

    else:

        # --------------------------------------------------
        # READ EXCEL
        # --------------------------------------------------

        data = pd.read_excel(
            uploaded_file
        )


        # --------------------------------------------------
        # VALIDATE TIMETABLE
        # --------------------------------------------------

        valid, message = validate_timetable(
            data
        )


        if not valid:

            st.error(message)

        else:

            # --------------------------------------------------
            # DATABASE
            # --------------------------------------------------

            create_database()

            save_timetable(
                data
            )


            # --------------------------------------------------
            # FIND CONFLICTS
            # --------------------------------------------------

            conflicts = find_conflicts(
                data
            )


            # --------------------------------------------------
            # GET ROOMS FROM EXCEL
            # --------------------------------------------------

            rooms = (
                data["room"]
                .dropna()
                .astype(str)
                .str.strip()
                .unique()
                .tolist()
            )


            # --------------------------------------------------
            # FIND AVAILABLE ROOMS
            # --------------------------------------------------

            available_rooms = suggest_rooms(
                data,
                selected_date,
                start_time,
                end_time,
                rooms
            )


            # --------------------------------------------------
            # SUCCESS MESSAGE
            # --------------------------------------------------

            st.success(
                "Timetable analyzed successfully!"
            )


            # --------------------------------------------------
            # SUMMARY
            # --------------------------------------------------

            st.subheader(
                "📊 Timetable Summary"
            )

            summary1, summary2, summary3, summary4 = st.columns(4)


            with summary1:

                st.metric(
                    "📚 Total Classes",
                    len(data)
                )


            with summary2:

                st.metric(
                    "🏢 Rooms Found",
                    len(rooms)
                )


            with summary3:

                st.metric(
                    "✅ Available Rooms",
                    len(available_rooms)
                )


            with summary4:

                st.metric(
                    "⚠️ Conflicts",
                    len(conflicts)
                )


            # --------------------------------------------------
            # SELECTED DATE AND TIME
            # --------------------------------------------------

            st.subheader(
                "🕐 Room Availability"
            )

            st.write(
                "📅 Date:",
                selected_date.strftime("%d %B %Y")
            )

            st.write(
                "⏰ Time:",
                start_time.strftime("%H:%M"),
                "–",
                end_time.strftime("%H:%M")
            )


            # --------------------------------------------------
            # ROOMS
            # --------------------------------------------------

            st.subheader(
                "🏢 Rooms"
            )


            room_columns = st.columns(3)


            for index, room in enumerate(rooms):

                with room_columns[index % 3]:

                    if room in available_rooms:

                        st.success(
                            f"**{room}**\n\n"
                            "✅ Available"
                        )

                    else:

                        st.error(
                            f"**{room}**\n\n"
                            "❌ Occupied"
                        )


            # --------------------------------------------------
            # SUGGESTED ROOMS
            # --------------------------------------------------

            st.subheader(
                "💡 Suggested Rooms"
            )


            if available_rooms:

                suggestion_columns = st.columns(4)


                for index, room in enumerate(
                    available_rooms
                ):

                    with suggestion_columns[
                        index % 4
                    ]:

                        st.success(
                            f"→ **{room}**"
                        )


            else:

                st.warning(
                    "No rooms are available for this time."
                )