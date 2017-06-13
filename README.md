# Fresh Tomatoes Movie Trailer Website 

This website was done as the first of 6 projects from the [Udacity Full Stack Nanodegree course](https://in.udacity.com/course/full-stack-web-developer-nanodegree--nd004/).
The user can view movie trailers and look for additional information on the website.

## Table of Contents
1. [Installation](#installation)
2. [Screenshots](#screenshots) 
3. [Description](#description)
5. [License](#license)

### Installation
The source code for this project is written in [Python](https://www.python.org/downloads/) programming language. 
For direct download of version 3.6.1 [click here](https://www.python.org/ftp/python/3.6.1/python-3.6.1.exe) and for version 2.7.13 [click here](https://www.python.org/ftp/python/2.7.13/python-2.7.13.msi).

The source code was checked against bugs and quality using **Pylint** checker and [PEP8 online check](http://pep8online.com).
To install Pylint:
```
pip install pylint
```

To check Python file using Pylint:
```
pylint fileName.py
```
### Screenshots

![](https://github.com/MANOJPATRA1991/fresh_tomatoes/blob/master/Screenshots/Screenshot%20(6).png?raw=true)
![](https://github.com/MANOJPATRA1991/fresh_tomatoes/blob/master/Screenshots/Screenshot%20(7).png?raw=true)
![](https://github.com/MANOJPATRA1991/fresh_tomatoes/blob/master/Screenshots/Screenshot%20(10).png?raw=true)

### Description
Inside the **fresh_tomatoes** directory, we have a **movies** folder which contains **entertainment_center.py**, **media.py** and **my_movies.py** files.

**my_movies.py** writes html, css and javascript required to run the website to the **fresh_tomatoes.html** file.

**media.py** contains the Movie class with the help of which instances of type Movie can be created.

**entertainment_center.py** is the file where we create Movie instances and that when executed runs the program and opens the website on a web browser.

To run the program, open **entertainment_center.py** with **IDLE(Python 3.6)** and then **Run -> Run Module** or press **F5** for instant execution.

#### The Movie Class
```
class Movie(object):
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    MOVIE_GENRE = ["Science Fiction", "Crime", "Thriller",
                   "Fantasy", "Drama", "Action"]

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
        """This function opens a web browser to play
        the trailer for a Movie class instance"""
        webbrowser.open(self.trailer_youtube_url)
```
### Creating an instance of the Movie class:
```
# INTERSTELLAR
interstellar = media.Movie(
    "Interstellar",
    "In the future, Earth is slowly becoming uninhabitable. Ex"
    "Ex-NASA pilot Cooper, along with a team of researchers, "
    "is sent on a planet exploration mission to report which "
    "planet can sustain life.",
    media.Movie.MOVIE_GENRE[0] + "  |  " + media.Movie.MOVIE_GENRE[4],
    "http://static.tvtropes.org/pmwiki/pub/images/" +
    "interstellar_film_poster_1146.jpg",
    "https://www.youtube.com/watch?v=ePbKGoIGAXY",
    media.Movie.VALID_RATINGS[2],
    8.6,
    "71%",
    [
        "Matthew McConaughey",
        "Anna Hathaway",
        "Jessica Chastain",
        "Matt Damon"],
    "Christopher Nolan",
    [
        "In 2001, Kubrick saw a future that was out of our hands. "
        "For Nolan, our reliance on one another is all we have got.",
        "Brainy, barmy and beautiful to behold, this is Stephen "
        "Hawkings Star Trek: a mind-bending opera of space and "
        "time with a soul wrapped up in all the science.",
        "As visually and conceptually audacious as anything Nolan "
        "has yet done, the directors ninth feature also proves "
        "more emotionally accessible than his coolly cerebral "
        "thrillers and Batman movies."
    ],
    [
        "Peter Travers, Rolling Stone",
        "James Dyer, Empire",
        "Scott Foundas, Variety"
    ])
```

### License
The content of this repository is licensed under [MIT](https://choosealicense.com/licenses/mit/).


