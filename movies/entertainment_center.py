"""This module opens the fresh_tomatoes.html in a web browser"""
import media
import my_movies

#creating instances of the Movie class

#INTERSTELLAR
interstellar = media.Movie("Interstellar",
                           "In the future, Earth is slowly becoming uninhabitable. Ex-NASA pilot Cooper, along with a team of researchers, is sent on a planet exploration mission to report which planet can sustain life.",
                           media.Movie.MOVIE_GENRE[0] + "  |  " + media.Movie.MOVIE_GENRE[4],
                           "http://static.tvtropes.org/pmwiki/pub/images/interstellar_film_poster_1146.jpg",
                           "https://www.youtube.com/watch?v=ePbKGoIGAXY",
                           media.Movie.VALID_RATINGS[2],
                           8.6,
                           "71%",
                           ["Matthew McConaughey", "Anna Hathaway", "Jessica Chastain", "Matt Damon"],
                           "Christopher Nolan",
                           [
                            "In 2001, Kubrick saw a future that was out of our hands. For Nolan, our reliance on one another is all we have got.",
                            "Brainy, barmy and beautiful to behold, this is Stephen Hawkings Star Trek: a mind-bending opera of space and time with a soul wrapped up in all the science.",
                            "As visually and conceptually audacious as anything Nolan has yet done, the directors ninth feature also proves more emotionally accessible than his coolly cerebral thrillers and Batman movies."
                           ],
                           ["Peter Travers, Rolling Stone", "James Dyer, Empire", "Scott Foundas, Variety"])

#AVATAR
avatar = media.Movie("Avatar",
                     "Jake, a paraplegic marine, replaces his brother on the Na'vi inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own but he must decide where his loyalties lie.",
                     media.Movie.MOVIE_GENRE[0] + "  |  " + media.Movie.MOVIE_GENRE[3] + "  |  " + media.Movie.MOVIE_GENRE[4] + "  |  " +
                     media.Movie.MOVIE_GENRE[5],
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     media.Movie.VALID_RATINGS[2],
                     7.8,
                     "83%",
                     ["Zoe Saldana", "Sam Worthington", "Sigourney Weaver", "Stephen King", "Michelle Rodriguez"],
                     "James Cameron",
                     ["Worth watching for fans, completists and anyone who missed it on the big screen first time around - but it wont win over any haters.",
                      "What if the director of the highest-grossing movie ever made (Titanic) spent a rumored $500 million on a spectacular futuristic sci-fi epic and no one other than hardcore fanboys went to see it?",
                      "Fifteen years in the making, James Camerons latest creation is an eye-popping spectacle of conflict between idyllic aliens and greedy humans saturated with environmental and spiritual themes."],
                     ["Nick de Semlyen, Empire", "Sandie Angulo Chen, Common Sense Media", "Adam R. Holz, Plugged In"])

#THE AVENGERS
the_avengers = media.Movie("The Avengers",
                       "S.H.I.E.L.D. leader Nick Fury is compelled to launch the 'Avengers Initiative' when Loki poses a threat to planet Earth. Will Nick Fury's squad of superheroes prove themselves equal to the task?",
                       media.Movie.MOVIE_GENRE[0] + "  |  " + media.Movie.MOVIE_GENRE[3] + "  |  " + media.Movie.MOVIE_GENRE[4] + "  |  " +
                       media.Movie.MOVIE_GENRE[5],
                       "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                       media.Movie.VALID_RATINGS[2],
                       8.1,
                       "92%",
                       ["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Chris Hemsworth", "Mark Ruffalo", "Nick Fury"],
                       "Joss Whedon",
                       ["If twos company and threes a crowd, whats four? Or six? In this case, its Marvels newest superhero movie.",
                        "Quick-witted and nuanced, this movie takes the best of the genre -- iconic heroes fighting for truth and justice -- and dishes it out in a fanboy-pleasing, edge-of-your seat way.",
                        "A joyous blend of heroism and humour that raises the stakes even as it maintains a firm grip on what makes the individual heroes tick."],
                       ["Paul Asay, Plugged In", "S. Jhoanna Robledo, Common Sense Media", "Empire"])

#DOCTOR STRANGE
doctor_strange = media.Movie("Doctor Strange",
                             "While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts.",
                             media.Movie.MOVIE_GENRE[0] + "  |  " + media.Movie.MOVIE_GENRE[3] + "  |  " + media.Movie.MOVIE_GENRE[4] + "  |  " +
                             media.Movie.MOVIE_GENRE[5],
                             "https://upload.wikimedia.org/wikipedia/en/thumb/c/c7/Doctor_Strange_poster.jpg/220px-Doctor_Strange_poster.jpg",
                             "https://www.youtube.com/watch?v=MWRUNTLisPo",
                             media.Movie.VALID_RATINGS[2],
                             7.6,
                             "90%",
                             ["Tilda Swinton", "Benedict Cumberbatch", "Chiwetel Ejiofor", "Rachel McAdams", "Mads Mikkelsen"],
                             "Scott Derrickson",
                             ["Marvels 14th Cinematic Universe movie has all the usual action and explosions, but it also has a different type of main character -- one whos magical and appealingly flawed but willing to change.",
                              "A bizarre and beautiful detour on the Marvel journey, which culminates in a mind-bending, expectation-inverting final act. Not to be watched under the influence.",
                              "Aesthetically, Doctor Strange is a good movie, one of the strongest in the Marvel canon thus far. But is it a good movie? A movie suitable for you or your family? That depends."],
                             ["Jeffrey M. Anderson, Common Sense Media", "James Dyer, Empire", "Paul Asay, Plugged In"])

#THE DARK KNIGHT
the_dark_knight = media.Movie("The Dark Knight",
                              "The Joker, a psychopath, terrorises Gotham so he can prove that even the most incorruptible people can become evil. However, Batman, Gordon and Dent stand against him.",
                              media.Movie.MOVIE_GENRE[1] + "  |  " + media.Movie.MOVIE_GENRE[2] + "  |  " + media.Movie.MOVIE_GENRE[4] + "  |  " +
                              media.Movie.MOVIE_GENRE[5],
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                              media.Movie.VALID_RATINGS[2],
                              9.0,
                              "94%",
                              ["Christian Bale", "Heath Ledger", "Gary Oldman", "Michael Caine", "Morgan Freeman"],
                              "Christopher Nolan",
                              ["Heads up: a thunderbolt is about to rip into the blanket of bland we call summer movies.",
                               "Ledgers performance is monumental, but The Dark Knight lives up to it. Nolan cements his position as Hollywoods premier purveyor of blockbuster smarts  and the Batbike is kinda cool, too.",
                               "This sequel to Batman Begins is mesmerizing and thought-provoking. But it shouldnt have been named after the good guy. This is the Jokers court, and hes not looking for a laugh."],
                              ["Peter Travers, Rolling Stone", "Mark Dinning, Empire", "Paul Asay, Plugged In"])

#NIGHTCRAWLER
nightcrawler = media.Movie("Nightcrawler",
                           "Lou Bloom wants to set a score with his rival Joe Loder even as he tries to shoot sensational stories of the rich neighbourhood of the city. His quest gets a new direction after he meets Nina Romina.",
                           media.Movie.MOVIE_GENRE[1] + "  |  " + media.Movie.MOVIE_GENRE[2] + "  |  " + media.Movie.MOVIE_GENRE[4],
                           "https://resizing.flixster.com/V49PiBgbepPpFjn3J_b4ikNd6wA=/206x305/v1.bTsxMTE4OTQ3MztqOzE3NDA5OzEyMDA7ODAwOzEyMDA",
                           "https://www.youtube.com/watch?v=X8kYDQan8bw",
                           media.Movie.VALID_RATINGS[3],
                           7.9,
                           "95%",
                           ["Jake Gyllenhaal", "Rene Russo", "Riz Ahmed", "Bill Paxton", "Jonathan Coyne"],
                           "Dan Gilroy",
                           ["Sharp, dark, satirical and bone-rattlingly thrilling, with a career-peak turn from Jake Gyllenhaal. Its this years Drive.",
                            "Nightcrawler curves and hisses its way into your head with demonic skill.",
                            "The result is a very good movie and a milestone in Gyllenhaals career but one in which the pieces dont quite fit together."],
                           ["Dan Jolin, Empire", "Peter Travers, Rolling Stone", "Christopher Orr, The Atlantic"])
                              

movies = [interstellar, avatar, the_avengers, doctor_strange, the_dark_knight, nightcrawler]

my_movies.open_movies_page(movies)

