#!usr/bin/env Python3
#
# Author: August Frisk | <https://github.com/4N0NYM0U5MY7H>
# Assign: Lab 11
# Course: CSci 270 | Fall 2017
# Instructor: Dale Phillips | <https://github.com/phillipsd>
#
from datetime import date
import math
import os


HERE = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(os.path.join(HERE, "data")):
    os.makedirs(os.path.join(HERE, "data"))

if not os.path.exists(os.path.join(HERE, "logs")):
    os.makedirs(os.path.join(HERE, "logs"))

if not os.path.exists(os.path.join(HERE, "public")):
    os.makedirs(os.path.join(HERE, "public"))

DATA = os.path.join(HERE, "data")
LOGS = os.path.join(HERE, "logs")
PUBLIC = os.path.join(HERE, "public")


def sum_digits(number):
    """Returns the sum of the digits in a number."""
    return sum([int(digit) for digit in str(number)])


def birth_sum(date_of_birth):
    """Returns single digit sum of the digits in the user's date of birth."""
    number = sum_digits(date_of_birth)
    while number > 9:
        number = sum_digits(number)

    return number


def calculate_bio_rhythm(days_since_birth):
    """Calculates the bio-rhythm for a given number of days since birth.

    The bio-rhythm is calculated using the formulas:

        Physical: f(t) = sin(2 * pi * t / 23)
        Emotional: f(t) = sin(2 * pi * t / 28)
        Intellectual: f(t) = sin(2 * pi * t / 33)

    Where t is the number of days since birth.

    https://en.wikipedia.org/wiki/Biorhythm_(pseudoscience)#Calculation
    """

    two_pi_time = 2 * math.pi * days_since_birth

    physical = math.sin(two_pi_time / 23) * 100
    emotional = math.sin(two_pi_time / 28) * 100
    intellectual = math.sin(two_pi_time / 33) * 100

    return int(round(physical)), int(round(emotional)), int(round(intellectual))


def calculate_days_since_birth(birth_year, birth_month, birth_day):
    """Calculates the number of days since the user's date of birth."""
    birth_date = date(birth_year, birth_month, birth_day)
    today = date.today()
    return (today - birth_date).days
