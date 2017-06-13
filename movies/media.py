"""This module defines a Movies class that can be used to create instances of type Movies"""
import webbrowser

class Movie(object):
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    MOVIE_GENRE = ["Science Fiction", "Crime", "Thriller", "Fantasy", "Drama", "Action"]
    
    def __init__(self, movie_title, movie_storyline, movie_genre, poster_image,
                 trailer_youtube, mpaa_rating, imdb, rotten_tomatoes,
                 cast, director, reviews, reviewers):
        """
        Initializes Movie class instance with following instance variables:

            title
            storyline
            genre
            poster_image_url
            trailer_youtube_url
            mpaa_rating
            imdb
            rotten_tomatoes
            cast
            director
            reviews
            reviewers
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.genre = movie_genre
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.mpaa_rating = mpaa_rating
        self.imdb = imdb
        self.rotten_tomatoes = rotten_tomatoes
        self.cast = cast
        self.director = director
        self.reviews = reviews
        self.reviewers = reviewers

    def show_trailer(self):
        """This function opens a web browser to play the trailer for a Movie class instance"""
        webbrowser.open(self.trailer_youtube_url)
