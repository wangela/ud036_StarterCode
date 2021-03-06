import fresh_tomatoes
import media

# Populate the movies database. Order doesn't matter as these will get sorted alphabetically by title when displayed.
toy_story = media.Movie("Toy Story", 
    "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.", 
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
    81, "https://youtu.be/KYz2wyBy3kc")
moana = media.Movie("Moana", 
    "When a terrible curse reaches Moana's island, she seeks out demigod Maui to set things right.", 
    "https://vignette1.wikia.nocookie.net/disney/images/2/2e/Moana_poster_3.jpg", 
    107, "https://youtu.be/LKFuXETZUsI")
divergent = media.Movie("Divergent", 
    "In a world divided by factions based on virtues, Tris learns she's Divergent and won't fit in.", 
    "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg", 
    139, "https://youtu.be/sutgWjz10sM")
wonder_woman = media.Movie("Wonder Woman", 
    "Before she was Wonder Woman, she was Diana, princess of the Amazons, trained warrior.", 
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg", 
    141, "https://youtu.be/336qJITnDi0")
ghostbusters = media.Movie("Ghostbusters (2016)", 
    "Following a ghost invasion of Manhattan, four women band together to stop the otherworldly threat.", 
    "https://upload.wikimedia.org/wikipedia/en/3/32/Ghostbusters_2016_film_poster.png", 
    116, "https://youtu.be/w3ugHP-yZXw")
matrix = media.Movie("The Matrix", 
    "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.", 
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg", 
    136, "https://youtu.be/tGgCqGm_6Hs")

# Populate the shows database. Order doesn't matter as these will get sorted alphabetically by title when displayed.
atypical = media.Series("Atypical", 
    "Sam, an 18-year-old on the autism spectrum, decides it's time to find a girlfriend, a journey that sets Sam's mom on her own life-changing path as her son seeks more independence.", 
    "https://upload.wikimedia.org/wikipedia/en/d/d2/Atypical_p%C3%B3ster.jpg", 
    1, "http://i1.wp.com/atypicalfamilia.com/wp-content/uploads/2017/08/20806582_1557297210998166_988248710_o.jpg")
got = media.Series("Game of Thrones", 
    "Nine noble families fight for control over the mythical lands of Westeros.", 
    "http://vignette3.wikia.nocookie.net/gameofthrones/images/2/2c/Season_1_Poster.jpg", 
    7, "https://static.gamespot.com/uploads/scale_super/1544/15443861/3051694-game-of-thrones-characters_091710.jpg")
insecure = media.Series("Insecure", 
    "The awkward experiences and racy tribulations of a modern-day African-American woman.", 
    "http://www.what-song.com/images/posters/tv_show100171/Insecure-200.jpg", 
    2, "https://cdn.newsbusters.org/images/insecure_0.jpg")
offspring = media.Series("Offspring", 
    "The story of the impossible loves of 30-something obstetrician Nina Proudman and her fabulously messy family.", 
    "https://images-na.ssl-images-amazon.com/images/I/51D5tSl3lIL.jpg", 
    7, "https://art-s.nflximg.net/f9cf0/416a359f844dc7c34ae549151392e2eba14f9cf0.jpg")

movies = [ghostbusters, moana, divergent, toy_story, matrix, wonder_woman]
shows = [atypical, got, insecure, offspring]

## def print_seasons(tv_list):
##    for show in tv_list:
##        print(show.title + ": " + str(show.season_count) + " seasons")
##        
## print_seasons(shows)
         
fresh_tomatoes.open_movies_page(movies, shows)

# print(media.Movie.VALID_RATINGS)


