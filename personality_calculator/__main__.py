#!usr/bin/env Python3
#
# Author: August Frisk | <https://github.com/4N0NYM0U5MY7H>
# Assign: Lab 11
# Course: CSci 270 | Fall 2017
# Instructor: Dale Phillips | <https://github.com/phillipsd>
#
"""Calculates a "unique personality" based on user input."""
from datetime import datetime
import os
import webbrowser

import database
import gui
import personality
import utils
import webpage
import zodiac


HTML = os.path.join(utils.PUBLIC, "index.html")
LOG = os.path.join(utils.LOGS, "personality.log")


if __name__ == "__main__":
    """Main entry point for the application."""

    html_file = HTML
    log_file = LOG

    # Initialize the database and GUI
    database.init_db()
    gui.init_gui()

    # Collect data from the user
    user_name = gui.get_user_name()
    birth_month = gui.get_birth_month()
    birth_day = gui.get_birth_day()
    birth_year = gui.get_birth_year()

    # Concatenate the date of birth into a single string
    date_of_birth = str(birth_month) + str(birth_day) + str(birth_year)

    # Enneagram is a personality typing system that assigns a number 1-9 to each
    # personality type.  The birth_sum function is used to calculate the
    # enneagram number for the user.
    enneagram = utils.birth_sum(date_of_birth)
    personality_type = personality.enneagram_type.get(enneagram)

    chinese_zodiac = zodiac.get_chinese_zodiac(birth_year)
    western_zodiac = zodiac.get_western_zodiac(birth_month, birth_day)

    # Calculate the bio-rhythm for the user
    days_since_birth = utils.calculate_days_since_birth(
        birth_year, birth_month, birth_day
    )
    bio_rhythm = utils.calculate_bio_rhythm(days_since_birth)

    physical = bio_rhythm[0]
    emotional = bio_rhythm[1]
    intellectual = bio_rhythm[2]

    output_string = (
        f"Hi {user_name}! You were born in the year of the {chinese_zodiac}.\n"
        + f"Under the sign of {western_zodiac}.\n"
        + f"You are a\n{personality_type}.\n"
        + f"You are {physical}% physical, {emotional}% emotional, and {intellectual}% intellectual."
    )

    # Write the output to the screen
    gui.write_to_screen(output_string)
    gui.close_window()

    print("writing to webpage...")
    webpage.write_html_file(
        html_file,
        user_name,
        personality_type,
        physical,
        emotional,
        intellectual,
        chinese_zodiac,
        western_zodiac,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )

    print(f"Opening {html_file} in a web browser...")
    webbrowser.open_new_tab(html_file)

    # Modify the variables to be written to the log and database
    birth_date = f"{birth_month}/{birth_day}/{birth_year}"
    chinese_zodiac_key = zodiac.calculate_chiense_zodiac(birth_year)
    western_zodiac_key = zodiac.calculate_western_zodiac(birth_month, birth_day)

    print("writing to log file...")
    log = open(log_file, "a")
    log.write(
        f"User: {user_name},"
        + f"DOB: {birth_date},"
        + f"Enneagram: {enneagram},"
        + f"Chinese: {chinese_zodiac_key},"
        + f"Western: {western_zodiac_key},"
        + f"Created at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        + "\n"
    )
    log.close()

    print("writing to database...")
    database.insert_entry(
        user_name=user_name,
        birth_date=birth_date,
        enneagram=enneagram,
        chinese_zodiac_key=chinese_zodiac_key,
        western_zodiac_key=western_zodiac_key,
        physical=physical,
        emotional=emotional,
        intellectual=intellectual,
    )
