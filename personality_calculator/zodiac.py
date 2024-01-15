#!usr/bin/env Python3
#
# Author: August Frisk | <https://github.com/4N0NYM0U5MY7H>
# Assign: Lab 11
# Course: CSci 270 | Fall 2017
# Instructor: Dale Phillips | <https://github.com/phillipsd>
#
# Descriptions provided by Professor Dale Phillips.
"""This file contains the Chinese and Western zodiacs and their descriptions."""


RAT = "RAT: quick-witted, smart, charming, and persuasive"
OX = "OX: patient, kind, stubborn, and conservative"
TIGER = "TIGER: authoritative, emotional, courageous, and intense"
RABBIT = "RABBIT: popular, compassionate, and sincere"
DRAGON = "DRAGON: energetic, fearless, warm-hearted, and charismatic"
SNAKE = "SNAKE: charming, gregarious, introverted, generous, and smart"
HORSE = "HORSE: energetic, independent, impatient, and enjoy traveling"
GOAT = "GOAT: mild-mannered, shy, kind, and peace-loving"
MONKEY = "MONKEY: fun, energetic, and active"
ROOSTER = "ROOSTER: independent, practical, hard-working, and observant"
DOG = "DOG: patient, diligent, generous, faithful, and kind"
PIG = "PIG: loving, tolerant, honest, and appreciative of luxury"


AIRES = """AIRES: Element of Fire. Ruled by Mars. Luck brought by the color Red, the
number 5, and Rubies."""

TAURUS = """TAURUS: Element of Earth. Ruled by Venus. Luck brought by the color Pink, the
number 6, Emralds, and Jade."""

GEMINI = """GEMINI: Element of Air. Ruled by Mercury. Luck brought by the color Yellow, the
number 7, and Opals."""

CANCER = """CANCER: Element of Water. Ruled by the Moon. Luck brought by the color Green,
the number 2, and Pearls."""

LEO = """LEO: Element of Fire. Ruled by the Sun. Luck brought by the colors Red, Gold,
and Yellow, the number 19, and Gold."""

VIRGO = """VIRGO: Element of Earth. Ruled by Mercury. Luck brought by the color Grey, the
number 7, Sapphires, and Amber."""

LIBRA = """LIBRA: Element of Air. Ruled by Venus. Luck brought by the color Brown, the
number 3, Coral, and Amber."""

SCORPIO = """SCORPIO: Element of Water. Ruled by Pluto and Mars. Luck brought by the colors
Purple and Black, the number 4, Jasper, and Black Crystals."""

SAGITTARIUS = """SAGITTARIUS: Element of Fire. Ruled by Jupiter. Luck brought by the color Light
Blue, the number 6, and Amethysts."""

CAPRICORN = """CAPRICORN: Element of Earth. Ruled by Saturn. Luck brought by the colors Brown,
Black, and Dark Green, the number 4, and Black Jade."""

AQUARIUS = """AQUARIUS: Element of Air. Ruled by Uranus. Luck brought by the color Bronze,
the number 22, and Black Pearls."""

PISCES = """PISCES: Element of Water. Ruled by Neptune. Luck brought by the color White,
the number 11, and Ivory Stones."""


chinese_zodiac = {
    1: RAT,
    2: OX,
    3: TIGER,
    4: RABBIT,
    5: DRAGON,
    6: SNAKE,
    7: HORSE,
    8: GOAT,
    9: MONKEY,
    10: ROOSTER,
    11: DOG,
    12: PIG,
}

western_zodiac = {
    "aires": AIRES,
    "taurus": TAURUS,
    "gemini": GEMINI,
    "cancer": CANCER,
    "leo": LEO,
    "virgo": VIRGO,
    "libra": LIBRA,
    "scorpio": SCORPIO,
    "sagittarius": SAGITTARIUS,
    "capricorn": CAPRICORN,
    "aquarius": AQUARIUS,
    "pisces": PISCES,
}


def calculate_chiense_zodiac(birth_year):
    """Calculate the Chinese zodiac key based on the year of birth."""
    return ((birth_year - 4) % 12) + 1


def get_chinese_zodiac(birth_year):
    """Return the Chinese zodiac based on the year of birth."""
    return chinese_zodiac[calculate_chiense_zodiac(birth_year)]


def calculate_western_zodiac(birth_month, birth_day):
    """Calculate the Western zodiac key based on the month and day of birth.

    Aquarius (January 20-February 18)
    Pisces (February 19-March 20)
    Aries (March 21-April 19)
    Taurus (April 20-May 20)
    Gemini (May 21-June 20)
    Cancer (June 21-July 22)
    Leo (July 23-August 22)
    Virgo (August 23-September 22)
    Libra (September 23-October 22)
    Scorpio (October 23-November 21)
    Sagittarius (November 22-December 21)
    Capricorn (December 22-January 19)
    """
    if birth_month == 1:
        return "capricorn" if birth_day < 20 else "aquarius"

    if birth_month == 2:
        return "aquarius" if birth_day < 19 else "pisces"

    if birth_month == 3:
        return "pisces" if birth_day < 21 else "aries"

    if birth_month == 4:
        return "aries" if birth_day < 20 else "taurus"

    if birth_month == 5:
        return "taurus" if birth_day < 21 else "gemini"

    if birth_month == 6:
        return "gemini" if birth_day < 21 else "cancer"

    if birth_month == 7:
        return "cancer" if birth_day < 23 else "leo"

    if birth_month == 8:
        return "leo" if birth_day < 23 else "virgo"

    if birth_month == 9:
        return "virgo" if birth_day < 23 else "libra"

    if birth_month == 10:
        return "libra" if birth_day < 23 else "scorpio"

    if birth_month == 11:
        return "scorpio" if birth_day < 22 else "sagittarius"

    if birth_month == 12:
        return "sagittarius" if birth_day < 22 else "capricorn"


def get_western_zodiac(birth_month, birth_day):
    """Return the Western zodiac based on the month and day of birth."""
    return western_zodiac[calculate_western_zodiac(birth_month, birth_day)]
