from imdb import Cinemagoer
import webbrowser
# import string
# import time
ia = Cinemagoer()

htmlFile = '/Users/adam/Documents/GitHub/family-flix/homeMov.html'
movieList = []
movieText = 'id="movieName"'
castDict = {}

with open(htmlFile, 'r') as file:
    line_list = file.readlines()
    for item in line_list:
        if movieText in item:
            # movieName = item.replace(" ","")
            movieName = item.replace('<div id="movieName" class="text"><b>','')
            movieName = movieName.replace('</b></div>\n','')
            if movieName[:24] == '                        ':
                movieName = movieName[24:]
            elif movieName[:20] == '                    ':
                movieName = movieName[20:]
            else:
                print('neither')
            movieList.append(movieName) 
movieCount = len(movieList)
for movie in movieList:
    # print(movie)
    searchedMovie = ia.search_movie(movie)
    for i in searchedMovie[0:1]:
        movieCode = i.movieID
        movieData = ia.get_movie(movieCode)
        actorNames = ''
        try:
            topFiveCast = movieData.data['cast'][0:5]
            count = 0
            for actor in topFiveCast:
                if count == 0:
                    actorNames = str(actor).replace(' ','_')
                else:
                    actorNames = actorNames+', '+str(actor).replace(' ','_')
                count += 1
            movieDict = {movie:actorNames}
            castDict.update(movieDict)
            # print(castDict)
            movieCount -= 1

        except:
            print(f'no cast info for {movie}')
            movieCount -= 1

    print(movieCount)

print(castDict)