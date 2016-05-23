import webbrowser
import os
import re
import fresh_tomatoes

#parent class containing arguments for movies
class movie():
    def __init__(self,movie_title,trailer_youtube_url,movie_poster):

        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = movie_poster

#child class
class media(movie):
    """class containing movies"""
    def __init__(self,movie_title,trailer_youtube_url,movie_poster):
        movie.__init__(self,movie_title,trailer_youtube_url,movie_poster)



#movie and its attributes
Fast_and_The_Furious_7 = media("Fast and The Furious 7",
                               "https://www.youtube.com/watch?v=Skpu5HaVkOc",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Furious_7_poster.jpg/220px-Furious_7_poster.jpg")

The_Revenant = media("The Revenant",
                     "https://youtu.be/LoebZZ8K5N0",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/The_Revenant_2015_film_poster.jpg/220px-The_Revenant_2015_film_poster.jpg")

Deadpool = media("Deadpool",
                 "https://www.youtube.com/watch?v=9vN6DHB6bJc",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Deadpool_poster.jpg/220px-Deadpool_poster.jpg")

Captain_America_Civil_War = media("Captain America: Civil War",
                                    "https://youtu.be/xnv__ogkt0M",
                                    "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/Captain_America_Civil_War_poster.jpg/220px-Captain_America_Civil_War_poster.jpg")

Ant_Man = media("Ant Man",
            "https://youtu.be/pWdKf3MneyI",
            "https://upload.wikimedia.org/wikipedia/en/thumb/7/75/Ant-Man_poster.jpg/220px-Ant-Man_poster.jpg")

Jason_bourne = media("Jason Bourne",
                     "https://youtu.be/F4gJsKZvqE4",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/4/49/Jason-bourne-poster.jpg/220px-Jason-bourne-poster.jpg")

#list of movies
movies = [Fast_and_The_Furious_7, The_Revenant, Deadpool,Captain_America_Civil_War, Ant_Man, Jason_bourne]

#function that opens webpage in browser with info
fresh_tomatoes.open_movies_page(movies)
