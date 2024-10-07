from imdb import Cinemagoer
import webbrowser
import string
import time
ia = Cinemagoer()

def plus(string):
    return string.replace(" ", "+")
def jpg(string):
    return string.replace(" ", "-")

# user input
def startSearch():
    # Using the Search movie method
    prompt = input("What movie would you like templated?: ")
    items = ia.search_movie(prompt)
    count = 0
    searched8 = []
    searchCode = []
    print("\n")
    for i in items[0:8]:
        # print(i.data)
        count += 1
        try:
            searchCode.append(f"{i.movieID}")
            print(f"{count}: {i} ({i.data['year']})")
        except:
            searched8.append(f"{i}")
            searchCode.append(f"{i.movieID}")
            print(f"{count}: {i}")

    print("\n")
    selected = input("which of these movies are you templating? ")
    startTemplate(searchCode[int(selected)-1])




def startTemplate(movieID):
    print("\n")
    print("starting template")
    movie = ia.get_movie(f"{movieID}")
    # print(movie.data['plot'][0])


    title = movie['title']
    year = movie['year']
    director = movie.data['director'][0]['name']
    director = director[:1]+'.'
    plot = movie.data['plot'][0]
    genres = movie.data['genres']
    youtube = plus(title)
    image = jpg(title)


    if(int(year) < 1960):
        dec = '50s'
    elif(1960 <= int(year) <= 1969):
        dec = '60s'
    elif(1970 <= int(year) <= 1979):
        dec = '70s'
    elif(1980 <= int(year) <= 1989):
        dec = '80s'
    elif(1990 <= int(year) <= 1999):
        dec = '90s'
    elif(2000 <= int(year) <= 2009):
        dec = '00s'
    elif(2010 <= int(year) <= 2019):
        dec = '10s'
    elif(2020 <= int(year) <= 2029):
        dec = '20s'
    else:
        dec = '30s'


    genre = ''
    genreTag = ''
    xPass = -1
    for x in genres:
        xPass += 1
        if xPass+1 == len(genres):
            genre = (f"{genre} {genres[xPass]}")
            genreTag = (f"{genreTag} {genres[xPass]}")
        else:
            genre = (f"{genre} {genres[xPass]}")
            genreTag = (f"{genreTag} {genres[xPass]} •")


    # print(f"{title} - {youtube} - {year} - {director} - {plot} - {genreTag}")
    print(f"<div id='mov' class='contained Recent {dec} {genre}'> \n    <div class=container> \n        <img src='content\{image}.jpg'> \n        <div class='overlay'></div> \n    </div> \n    <a target='_blank' href='https://www.youtube.com/results?search_query={youtube}'> \n        <div class='text'><b>{title}</b></div>\n <p class='text'> Directed by {director} ({year})</p>\n    </a>\n    <div class='bio'>{plot} \n    <br><br>{genreTag}</div>\n</div>")
    time.sleep(5)
    webbrowser.open_new(f"https://duckduckgo.com/?q={youtube}")


def main():
    startSearch()

main()

