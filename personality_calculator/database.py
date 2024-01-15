#!usr/bin/env Python3
#
# Author: August Frisk | <https://github.com/4N0NYM0U5MY7H>
# Assign: Lab 11
# Course: CSci 270 | Fall 2017
# Instructor: Dale Phillips | <https://github.com/phillipsd>
#
"""This file contains the database functions for the personality calculator.""" ""
from contextlib import closing
import os
import sqlite3

from utils import DATA

DATABASE = os.path.join(DATA, "personality.db")
SCHEMA = os.path.join(DATA, "schema.sql")


def connect_db():
    """Connects to the application database."""
    return sqlite3.connect(DATABASE)


def init_db():
    """Initializes the application database."""
    with closing(connect_db()) as database:
        with open(SCHEMA, mode="r") as schema:
            database.cursor().executescript(schema.read())
        database.commit()


def insert_entry(**kwargs):
    """Inserts an entry into the database."""
    with closing(connect_db()) as database:
        database_cursor = database.cursor()
        database_cursor.execute(
            "INSERT INTO users(user_name, date_of_birth, enneagram, "
            + "chinese_zodiac, western_zodiac, physical, emotional, "
            + "intellectual) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (
                kwargs.get("user_name"),
                kwargs.get("birth_date"),
                kwargs.get("enneagram"),
                kwargs.get("chinese_zodiac_key"),
                kwargs.get("western_zodiac_key"),
                kwargs.get("physical"),
                kwargs.get("emotional"),
                kwargs.get("intellectual"),
            ),
        )
        database.commit()
