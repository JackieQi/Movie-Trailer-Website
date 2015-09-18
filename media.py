#!/usr/bin/env python
import webbrowser

"""This file is used to define Movie class """

__author__ = "Jackie Qi"
__copyright__ = "Copyright 2015, Jackie Qi"
__credits__ = ["Udacity.com"]


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
