import media
import fresh_tomatoes
my_father_and_mother = media.Movie("my_father_and_mother","http://t3.baidu.com/it/u=1468520311,48859012&fm=20","http://baishi.baidu.com/watch/9020637406734644711.html")

my_dear = media.Movie("my_dear","http://t1.baidu.com/it/u=209378971,2921209751&fm=20","http://baishi.baidu.com/watch/5940905633953268435.html")

movieList = [my_father_and_mother,my_dear]

fresh_tomatoes.open_movies_page(movieList)