# -*- coding: utf-8 -*-
import media
import fresh_tomatoes
movieOne = media.Movie("WILD CHILD",
                       "https://i.ytimg.com/vi/v2oC2vJailQ/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLBRKvnEOZVhlG9lF9-wYm6t0HEtDg",
                       "https://www.youtube.com/watch?v=v2oC2vJailQ")

movieTwo = media.Movie("Dunkirk",
                       "https://i.ytimg.com/vi/F-eMt3SrfFU/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLCSB1BwLMAt6XmH2oQjWN8IYOXfZw",
                       "https://www.youtube.com/watch?v=F-eMt3SrfFU&t=46s")

movieThree = media.Movie("ALGORITHM: The Hacker",
                       "https://i.ytimg.com/vi/6qpudAhYhpc/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLCnDfwpDHVk9JWmB6vNxGXoEjI4yQ",
                       "https://www.youtube.com/watch?v=6qpudAhYhpc")

movieFour = media.Movie("THE MARS UNDERGROUND ",
                       "https://i.ytimg.com/vi/tcTZvNLL0-w/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLBJVC2m8lPFJO0XwYHrfbW1a3UFDw",
                       "https://www.youtube.com/watch?v=tcTZvNLL0-w")

movieFive = media.Movie("Last Passenger",
                       "https://i.ytimg.com/vi/QRriteWU9UI/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLCtntMPABvSO4lk3HsbjzpAGRuPYQ",
                       "https://www.youtube.com/watch?v=QRriteWU9UI")

movieSix = media.Movie("英伦对决",
                       "https://i.ytimg.com/vi/r_rSAbYyIq0/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLC3m3cfQoxUpM82Ap4qt8ODVxJ2Pg",
                       "https://www.youtube.com/watch?v=r_rSAbYyIq0")

movieList = [movieOne,movieTwo,movieThree,movieFour,movieFive,movieSix]

fresh_tomatoes.open_movies_page(movieList)