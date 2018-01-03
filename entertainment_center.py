import media
import fresh_tomatoes
movieOne = media.Movie("All NEW Ranked Changes, Skins & Events EXPLAINED",
                                   "https://i.ytimg.com/vi/Bkd0jWUHIpI/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLB0IbW3eMEVbflb4pBNvSuJWlf0dw",
                                   "https://www.youtube.com/watch?v=Bkd0jWUHIpI")

movieTwo = media.Movie("How PROS Counter Bastion Cheese Comp!",
                       "https://i.ytimg.com/vi/-i14IPf67UY/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLCH9mJJ9HJwXh7kgAb3pyqsNVRwBg",
                       "https://www.youtube.com/watch?v=-i14IPf67UY&t=3s")

movieThree = media.Movie("Dunkirk - Trailer 1",
                       "https://i.ytimg.com/vi/F-eMt3SrfFU/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLCSB1BwLMAt6XmH2oQjWN8IYOXfZw",
                       "https://www.youtube.com/watch?v=F-eMt3SrfFU&t=37s")

movieFour = media.Movie("Jeff Kaplan trolls entire overwatch stream",
                       "https://i.ytimg.com/vi/SjDtOMAULLg/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLCFD8WZYjvcrQkR-Sxt88pxrJAPJA",
                       "https://www.youtube.com/watch?v=SjDtOMAULLg")

movieFive = media.Movie("Streamers vs Pros",
                       "https://i.ytimg.com/vi/Kk54eP4OTNw/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLBOWbcBKMzRNM59GJgDpyTEVYXCOw",
                       "https://www.youtube.com/watch?v=Kk54eP4OTNw")

movieSix = media.Movie("Greatest Team Kills",
                       "https://i.ytimg.com/vi/NFKZGWUOreY/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFDyq4qpAwsIARUAAIZCGAFwAQ==&rs=AOn4CLBxhG0OppAD9_GTHSeitpZwERyV2Q",
                       "https://www.youtube.com/watch?v=NFKZGWUOreY")

movieList = [movieOne,movieTwo,movieThree,movieFour,movieFive,movieSix]

fresh_tomatoes.open_movies_page(movieList)