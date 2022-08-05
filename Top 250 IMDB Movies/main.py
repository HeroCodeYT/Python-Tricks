import imdb #pip install imdbpy
a=imdb.IMDb()
search= a.get_top250_movies()
for i in range(100):
    print(search[i])
         