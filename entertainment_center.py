#!/usr/bin/env python
import fresh_tomatoes
import media

"""This file is used to initialize movies and pass them to fresh_tomatoes.py \
to create html webpage."""

__author__ = "Jackie Qi"
__copyright__ = "Copyright 2015, Jackie Qi"
__credits__ = ["Udacity.com"]

# Initial several moview to display on webpage
avengers2 = media.Movie("Avengers: Age of Ultron",
                        "When Tony Stark and Bruce Banner try to jump-start a \
                        dormant peacekeeping program  called Ultron, things \
                        go horribly wrong and it's up to Earth's Mightiest \
                        Heroes to stop the villainous Ultron from enacting \
                        his terrible plans.",
                        "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",  # noqa
                        "https://www.youtube.com/watch?v=bMP-FLmiIM0",
                        "Joss Whedon",
                        ["Robert Downey Jr.", "Chris Evans", "Mark Ruffalo"])

san_andreas = media.Movie("San Andreas",
                          "In the aftermath of a massive earthquake in \
                        California, a rescue-chopper pilot makes a \
                        dangerous journey with his ex-wife across \
                        the state in order to rescue his daughter.",
                          "https://upload.wikimedia.org/wikipedia/en/3/38/San_Andreas_poster.jpg",  # noqa
                          "https://www.youtube.com/watch?v=yftHosO0eUo",
                           "Brad Peyton",
                          ["Dwayne Johnson", "Carla Gugino",
                           "Alexandra Daddario"])

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               "A military officer is brought into an alien war \
                            against an extraterrestrial enemy who can \
                            reset the day and know the future. When this \
                            officer is enabled with the same power, he \
                            teams up with a Special Forces warrior to \
                            try and end the war.",
                               "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=bydHcLDfWuY",
                               "Doug Liman",
                               ["Tom Cruise", "Emily Blunt", "Bill Paxton"])

transformers_age_of_extinction = media.Movie(
    "Transformers: Age of Extinction",
    "Autobots must escape sight from a bounty hunter who \
                        has taken control of the human serendipity",
    "https://upload.wikimedia.org/wikipedia/en/9/94/Transformers_Age_of_Extinction_Poster.jpeg",  # noqa
    "https://www.youtube.com/watch?v=DkIPIkPPbdo",
    "Michael Bay",
    ["Mark Wahlberg", "Nicola Peltz", "Jack Reynor"])

mission_impossible = media.Movie(
    "Mission: Impossible - Rogue Nation",
    "Ethan and team take on their most impossible mission \
                        yet, eradicating the Syndicate - an International \
                        rogue organization as highly skilled as they are, \
                        committed to destroying the IMF.",
    "https://upload.wikimedia.org/wikipedia/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=pXwaKB7YOjw",
    "Christopher McQuarrie",
    ["Tom Cruise", "Rebecca Ferguson", "Jeremy Renner"])

steve_jobs = media.Movie("Steve Jobs: The Man in the Machine",
                         "A look at the personal and private life of the late \
                        Apple CEO, Steve Jobs.",
                         "https://upload.wikimedia.org/wikipedia/en/d/d0/Steve_Jobs_The_man_in_the_Machine.jpg",  # noqa
                         "https://www.youtube.com/watch?v=SrlPyKxdMX4",
                         "Alex Gibney",
                         ["Steve Jobs"])
movies = [san_andreas, transformers_age_of_extinction,
          mission_impossible, steve_jobs, avengers2, edge_of_tomorrow]

# call open_movies_page function in fresh_tomatoes.py which will load webpage
fresh_tomatoes.open_movies_page(movies)
