<picture>
  <source
    srcset=".github/mjc_logo_reverse.svg"
    media="(prefers-color-scheme: dark)"
  />
  <source
    srcset=".github/mjc_logo.svg"
    media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"
  />
  <img src=".github/mjc_logo.svg" alt="Modesto Junior College logo." height="80px" />
</picture>

# Final Project: personality_calculator
[![GitHub Discussions](https://img.shields.io/badge/Learn_More-informational?logo=github&style=for-the-badge)](https://github.com/4N0NYM0U5MY7H/undergraduate/discussions/1)
[![Maintainability](https://api.codeclimate.com/v1/badges/983d856ebcfda6c354d2/maintainability)](https://codeclimate.com/github/4N0NYM0U5MY7H/personality_calculator/maintainability)

A simple GUI application that calculates a user's Enneagram, zodiac signs, and bio-rhythm.
> **WARNING:** this repository is archived and is no longer maintained.
> 
> [![Last Updated](https://img.shields.io/badge/December_2017-critical?label=Last%20Updated)](#)
> [![Not Maintained](https://img.shields.io/badge/Not_Maintained-critical?label=Status)](#)

## About
A simple personality analysis and astrology tool implemented in Python. It features a graphical user interface (GUI) designed to collect user input and provide insights into their Enneagram type, Chinese zodiac, Western zodiac, and bio-rhythm based on their date of birth.

### Key Features
1. Graphical User Interface (GUI)
   * Offers a user-friendly GUI implemented using Python's Turtle module that facilitates the input of personal information, particularly the date of birth, for analysis.

2. Enneagram Type Calculation
   * Calculates and reveals the user's Enneagram type, providing insights into their core motivations, fears, and behaviors.

3. Zodiac Analysis
   * Determines the user's Chinese and Western zodiac sign based on their date of birth, providing astrological insights.

4. Bio-rhythm Calculations
   * Presents users with information about their physical, emotional, and intellectual cycles based on their date of birth.

5. Log File Storage
   * Logs user input and stores calculated results, including Enneagram type, zodiac signs, and bio-rhythm calculations, in the log file. This ensures a comprehensive record of both user-provided information and the outcomes of the various analyses for future reference or analysis.

6. Database Integration
   * Both user input and generated results are stored in a database within the application, allowing for organized and structured data management.

This comprehensive Python application provides users with a holistic analysis, including Enneagram type, personality traits, astrological information, and bio-rhythms. The calculations and their outcomes are stored in the log file, enhancing the overall functionality and user experience of the application.

## Installation
To install and run this project locally, you will need to have [Python 3.6+](https://www.python.org/) with [IDLE](https://docs.python.org/3/library/idle.html) or an alternative text editor install on your machine.
### Clone the repository
```bash
git clone https://github.com/4N0NYM0U5MY7H/personality_calculator.git
```
### Navigate to the directory
```bash
cd personality_calculator
```
### Run the program
```bash
python __main__.py
```

## Tools & Technologies
[![Python 3.6](https://img.shields.io/badge/Python-3.6-3776AB?logo=python&labelColor=141414&style=flat-square)](https://www.python.org/)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
