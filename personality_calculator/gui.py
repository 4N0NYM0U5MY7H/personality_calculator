#!usr/bin/env Python3
#
# Author: August Frisk | <https://github.com/4N0NYM0U5MY7H>
# Assign: Lab 11
# Course: CSci 270 | Fall 2017
# Instructor: Dale Phillips | <https://github.com/phillipsd>
#
"""This file contains the gui functions for the personality calculator."""
import os
import turtle

HERE = os.path.dirname(os.path.abspath(__file__))
STATIC = os.path.join(HERE, "static")
IMAGE = os.path.join(STATIC, "final.gif")


def init_gui():
    """Initialize the GUI."""
    turtle.bgcolor("#102129")
    turtle.bgpic(IMAGE)
    turtle.setup(width=1280, height=800)
    turtle.color("White")
    turtle.penup()
    turtle.goto(0, -150)


def get_user_name():
    """Prompt the user to enter their name."""
    return turtle.textinput("Name", "Enter your name")


def get_birth_month():
    """Prompt the user to enter their birth month."""
    return int(
        turtle.numinput(
            "Month of birth", "Enter your birth month", 1, minval=1, maxval=12
        )
    )


def get_birth_day():
    """Prompt the user to enter their birth day."""
    return int(
        turtle.numinput("Day of birth", "Enter your birth day", 1, minval=1, maxval=31)
    )


def get_birth_year():
    """Prompt the user to enter their birth year."""
    return int(
        turtle.numinput(
            "Year of birth", "Enter your birth year", 1997, minval=1900, maxval=2017
        )
    )


def write_to_screen(output):
    """Write the output to the screen."""
    turtle.write(output, move=False, align="center", font=("Arial", 10, "normal"))


def close_window():
    """Close the GUI window."""
    turtle.bye()
