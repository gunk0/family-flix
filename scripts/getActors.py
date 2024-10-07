from imdb import Cinemagoer
import webbrowser
from collections import Counter
# import string
# import time
ia = Cinemagoer()

htmlFile = '/Users/adam/Documents/GitHub/family-flix/homeMov.html'
movieList = []
movieText = 'id="movieName"'
movieCount = 1

yearText = 'Directed by'
yearDict = {}
# yearCount = 0

seqText = 'seq"'
seqDict = {}

linesToReplace = []
replaceWith = []
actorNamesArray = []
line_list = ''


with open(htmlFile, 'r') as file:
    line_list = file.readlines()

    for item in line_list:

        if movieText in item:
            movieName = item.replace('id="movieName" class="text"><b','')
            movieName = movieName.replace('</b></div>\n','')
            indexVal = (movieName.index('>'))+1
            movieName = movieName[indexVal:]
            movieList.append(movieName) 

            seqIndex = item.index('seq="')
            seqID = item[seqIndex+5:seqIndex+9]
            seqKey = {movieName:seqID}
            seqDict.update(seqKey)

        if yearText in item:
            # yearCount += 1
            yearIndex = item.index('(')
            yearItem = item[yearIndex+1:yearIndex+5]
            yearKey = {movieName:yearItem}
            yearDict.update(yearKey)



for movie in movieList:
    castDict = {}
    year = yearDict.pop(movie)
    searchedMovie = ia.search_movie(movie)
    movieFound = False
    for i in searchedMovie[0:3]:
        if movieFound == False:
            movieCode = i.movieID
            movieData = ia.get_movie(movieCode)
            actorNames = ''
            try:
                if i['year'] == int(year):
                    try:
                        topFiveCast = movieData.data['cast'][0:5]
                        count = 0

                        for actor in topFiveCast:
                            actorNamesArray.append(actor)
                            if count == 0:
                                actorNames = 'a-'+str(actor).replace(' ','_')
                            else:
                                actorNames = actorNames+', '+'a-'+str(actor).replace(' ','_')
                            count += 1
                        movieDict = {movie:actorNames}
                        castDict.update(movieDict)
                        seq = seqDict.pop(movie)
                        # print(seq)
                        seqSearch = 'seq="'+seq+'" id="mov"'

                        # print(line_list)
                        for line in line_list:
                            # print(line)
                            if seqSearch in line:
                                seqIndex = line.index('>') - 1
                                # print(seqIndex)
                                newline = line[:seqIndex]+' '+actorNames+'">\n'
                                # print(newline)
                                linesToReplace.append(line)
                                replaceWith.append(newline)

                        movieFound = True

                    except:
                        print(f'no cast info for {movie}')
                else:
                    break
            except:
                print(f'no year info for {movie}')

        else:
            break

        print(castDict)


htmlText = ''

with open(htmlFile, 'r') as fin:
    html = fin.readlines()
    print(linesToReplace)
    print(replaceWith)
    for line in html:
        countX = 0
        for x in linesToReplace:
            # print(x)
            if linesToReplace[countX] in line:
                swapLine = line.replace(linesToReplace[countX],replaceWith[countX])
                # print(f'replacing: {linesToReplace[countX]} with: {replaceWith[countX]}')
                htmlText = htmlText+swapLine
                # print(swapLine)
            countX += 1
        if line in linesToReplace:
            print('')
        else:
            htmlText = htmlText+line


with open(htmlFile, 'w') as fout:
    # print(htmlText)
    fout.write(htmlText)


actorDict = Counter(actorNamesArray)
for key, value in actorDict.items():
    if value >= 3:
        print(key, value)

dictfile = '/Users/adam/Documents/GitHub/family-flix/scripts/dictFile.txt'
with open(dictfile, 'w') as dout:
    dout.write(str(actorDict))


print('done')