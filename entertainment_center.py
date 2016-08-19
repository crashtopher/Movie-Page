# Created by Chris Shaw July 13, 2016
# This file contains the implimentations of class Movie required
# to create the "Fresh Tomatoes" webpage

# Importing apropriate files to create webpage
import media
import fresh_tomatoes

# Implimentations of class Movie
dead_poets = media.Movie("Dead Poets Society",
						"an english professor teaches his students what it means to be free",
						"https://upload.wikimedia.org/wikipedia/en/4/49/Dead_poets_society.jpg",
						"https://www.youtube.com/watch?v=wrBk780aOis")

beauty_and_the_beast = media.Movie("Beauty and the Beast",
					 			   "A whimsical reading girl falls in love with a beastly prince",
					 			   "https://upload.wikimedia.org/wikipedia/en/7/7c/Beautybeastposter.jpg",
					 			   "https://www.youtube.com/watch?v=tRlzmyveDHE")

donnie_darko = media.Movie("Donnie Darko", 
						   "A highschool boy is plaugued by his own psychosis",
						   "https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",
						   "https://www.youtube.com/watch?v=qdKbNuhXWvQ")

the_village = media.Movie("The Village",
						  "A town ruled by fear is saved by love",
						  "https://upload.wikimedia.org/wikipedia/en/a/a0/The_Village_movie.jpg",
						  "https://www.youtube.com/watch?v=lwq4oTboRi4")

prestige = media.Movie("The Prestige", 
					   "Two magicians duke it out for prominance",
					   "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
					   "https://www.youtube.com/watch?v=o4gHCmTQDVI")

prisoner_of_azkaban = media.Movie("Harry Potter and the Prisoner of Azkaban",
								  "A Wizard runs from an escaped criminal",
								  "http://harrypotterfanzone.com/wp-content/2015/07/prisoner-of-azkaban-theatrical-poster-3.jpg", # N0QA
								  "https://www.youtube.com/watch?v=lAxgztbYDbs")

# Storing movies in a list to be implimented by "fresh_tomatoes.py"
movies = [dead_poets, beauty_and_the_beast, donnie_darko,
		 the_village, prestige, prisoner_of_azkaban]
		 
# function creates or overrides html file and opens it in a new tab if possible
fresh_tomatoes.open_movies_page(movies)

