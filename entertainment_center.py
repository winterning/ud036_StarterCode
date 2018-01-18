# -*- coding: utf-8 -*-
import media
import fresh_tomatoes
"""WILD CHILD movie :movie title,poster_image_url,trailer_youtube_url"""
movieOne = media.Movie("WILD CHILD",
                       "https://img1.doubanio.com/view/photo/s_ratio_poster/"
                       "public/p2506466229.jpg",
                       "https://www.youtube.com/watch?v=v2oC2vJailQ")

"""Dunkirk movie :movie title,poster_image_url,trailer_youtube_url"""
movieTwo = media.Movie("Dunkirk",
                       "https://img1.doubanio.com/view/photo/s_ratio_poster/"
                       "public/p2506139427.jpg",
                       "https://www.youtube.com/watch?v=F-eMt3SrfFU&t=46s")

"""ALGORITHM: The Hacker movie :movie title,poster_image_url,
trailer_youtube_url"""
movieThree = media.Movie("ALGORITHM: The Hacker",
                         "https://img3.doubanio.com/view/photo/s_ratio_poster/"
                         "public/p2507227732.jpg",
                         "https://www.youtube.com/watch?v=6qpudAhYhpc")

"""THE MARS UNDERGROUND movie :movie title,poster_image_url,
trailer_youtube_url"""
movieFour = media.Movie("THE MARS UNDERGROUND ",
                        "https://img1.doubanio.com/view/photo/s_ratio_poster/"
                        "public/p2507022339.jpg",
                        "https://www.youtube.com/watch?v=tcTZvNLL0-w")

"""Last Passenger movie :movie title,poster_image_url,trailer_youtube_url"""
movieFive = media.Movie("Last Passenger",
                        "https://img1.doubanio.com/view/photo/s_ratio_poster/"
                        "public/p2503997609.jpg",
                        "https://www.youtube.com/watch?v=QRriteWU9UI")

"""英伦对决 movie :movie title,poster_image_url,trailer_youtube_url"""
movieSix = media.Movie("英伦对决",
                       "https://img3.doubanio.com/view/photo/s_ratio_poster/"
                       "public/p2499135561.jpg",
                       "https://www.youtube.com/watch?v=r_rSAbYyIq0")

"""set the movies that will be passed to the media file"""
movieList = [movieOne, movieTwo, movieThree, movieFour, movieFive, movieSix]

"""open the html file in a webbrowser via the fresh_tomatoes.py file"""
fresh_tomatoes.open_movies_page(movieList)
