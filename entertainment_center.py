# -*- coding: utf-8 -*-
import media
import fresh_tomatoes
movieOne = media.Movie("WILD CHILD",
                       "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2506466229.jpg",
                       "https://www.youtube.com/watch?v=v2oC2vJailQ")

movieTwo = media.Movie("Dunkirk",
                       "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2506139427.jpg",
                       "https://www.youtube.com/watch?v=F-eMt3SrfFU&t=46s")

movieThree = media.Movie("ALGORITHM: The Hacker",
                       "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2507227732.jpg",
                       "https://www.youtube.com/watch?v=6qpudAhYhpc")

movieFour = media.Movie("THE MARS UNDERGROUND ",
                       "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2507022339.jpg",
                       "https://www.youtube.com/watch?v=tcTZvNLL0-w")

movieFive = media.Movie("Last Passenger",
                       "https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2503997609.jpg",
                       "https://www.youtube.com/watch?v=QRriteWU9UI")

movieSix = media.Movie("英伦对决",
                       "https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2499135561.jpg",
                       "https://www.youtube.com/watch?v=r_rSAbYyIq0")

movieList = [movieOne,movieTwo,movieThree,movieFour,movieFive,movieSix]

fresh_tomatoes.open_movies_page(movieList)