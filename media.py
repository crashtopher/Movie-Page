# Created by Chris Shaw on July 13, 2016

#This file creates class Movie with functions required to build webpage

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def show_trailer(self):
	 	webbrowser.open(self.trailer_youtube_url)

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_yourtube):
        # initialize instance of class Movie
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_yourtube

	
