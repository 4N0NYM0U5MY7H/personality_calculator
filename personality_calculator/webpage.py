#!usr/bin/env Python3
#
# Author: August Frisk | <https://github.com/4N0NYM0U5MY7H>
# Assign: Lab 11
# Course: CSci 270 | Fall 2017
# Instructor: Dale Phillips | <https://github.com/phillipsd>
#
"""This file contains the contents to generate the webpage for the personality calculator."""


HTML = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="author" content="August Frisk">
    <meta name="description" content="Personality Calculator">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Personality Calculator</title>
    <link rel="stylesheet" href="../static/main.css">
  </head>
  <body class="is-preload">
    <div id="wrapper">
      <header id="header" class="alt">
        <span class="logo"><img src="https://flaticons.net/icon.php?slug_category=brand-identity&slug_icon=readernaut" alt=""></span>

        <!-- USER NAME -->
        <h1>{}</h1>

        <p>Here is what makes you special!</p>
      </header>
      <div id="main">
        <section class="main">
          <div class="personality">
            <div class="content">
              <header class="major">
                <h2>Personality Type</h2>
              </header>

              <!-- PERSONALITY TYPE -->
              <p>{}</p>

            </div>
            <span class="image"><img src="https://images.pexels.com/photos/3078831/pexels-photo-3078831.jpeg?cs=srgb&dl=pexels-nadi-lindsay-3078831.jpg&fm=jpg" alt=""></span>
          </div>
        </section>
        <section class="main special">
          <header class="major">
            <h2>Bio-Rhythm</h2>
          </header>
          <ul class="bio-rhythm">
            <li>
              <span class="icon solid major style1 fa-running"></span>
              <h3>Physical</h3>

              <!-- PHYSICAL BIO-RHYTHM -->
              <p>{}</p>

            </li>
            <li>
              <span class="icon solid major style2 fa-theater-masks"></span>
              <h3>Emotional</h3>

              <!-- EMOTIONAL BIO-RHYTHM -->
              <p>{}</p>

            </li>
            <li>
              <span class="icon solid major style3 fa-book-reader"></span>
              <h3>Intellectual</h3>

              <!-- INTELLECTUAL BIO-RHYTHM -->
              <p>{}</p>

            </li>
          </ul>
        </section>
        <section class="main special">
          <div class="content">
            <header class="major">
              <h2>Chinese Zodiac</h2>
            </header>

            <!-- CHINESE ZODIAC -->
            <p>{}</p>

          </div>
          <div class="content">
            <header class="major">
              <h2>Western Zodiac</h2>
            </header>

            <!-- WESTERN ZODIAC -->
            <p>{}</p>

          </div>
        </section>
      </div>
      <footer id="footer">
        <div class="copyright">
          <p>&copy; 2017 August Frisk. Created with 
            <i class="fab fa-python"></i>
            <i class="fab fa-html5"></i>
            <i class="fab fa-css3-alt"></i>
          <p>Special thanks to <a href="https://html5up.net">HTML5 UP</a> for the template.</p>

          <!-- TIME STAMP -->
          <p>This page was generated on {}.</p>

        </div>
      </footer>
  </body>
</html>
"""


def write_html_file(filename, *args):
    """Writes the HTML file for the personality calculator.

    Arguments:
        user_name -- user's name
        personality_type -- user's personality type
        physical -- user's physical bio-rhythm
        emotional -- user's emotional bio-rhythm
        intellectual -- user's intellectual bio-rhythm
        chinese_zodiac -- user's Chinese zodiac
        western_zodiac -- user's Western zodiac
        time_stamp -- time the page was generated
    """
    with open(filename, "w") as html_file:
        html_file.write(HTML.format(*args))
