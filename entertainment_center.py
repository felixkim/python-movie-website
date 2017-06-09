#media is a ADT file of what a movie object is
#fresh_tomatoes does the heavy lifting of constructing the webpage
import media
import fresh_tomatoes


#Movie objects initiated and defined in order to use in our webpage

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtube.com./watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

inception = media.Movie("Inception",
                        "The story of the greatest reverse heist ever",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

interstellar = media.Movie("Interstellar",
                           "A story of time, space, and adventure",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

lalaland = media.Movie("La La Land",
                       "What's more important, love or your dream",
                       "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8")


#List in order to display list of movie objects
movies = [toy_story, avatar, school_of_rock, inception, interstellar, lalaland]

#Constructs webpage, takes in argument of an container object
fresh_tomatoes.open_movies_page(movies)
