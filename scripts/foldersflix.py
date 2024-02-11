import os
import string

folder = 'F:\WATCH DOC'

def remove(string):
    return string.replace(" ", "-")

count = 0 
dirlist = [item for item in os.listdir(folder) if os.path.isdir(os.path.join(folder,item))]
for item in dirlist:
    folder=item.split(",")
    folder=item.lstrip("']")
    mov,dire,year=item.split("(")
    movs=remove(mov)
    # count += 1
    # print(count)
    if(int(year[:-1]) < 1960):
        dec = '50s'
    elif(1960 <= int(year[:-1]) <= 1969):
        dec = '60s'
    elif(1970 <= int(year[:-1]) <= 1979):
        dec = '70s'
    elif(1980 <= int(year[:-1]) <= 1989):
        dec = '80s'
    elif(1990 <= int(year[:-1]) <= 1999):
        dec = '90s'
    elif(2000 <= int(year[:-1]) <= 2009):
        dec = '00s'
    elif(2010 <= int(year[:-1]) <= 2019):
        dec = '10s'
    elif(2020 <= int(year[:-1]) <= 2029):
        dec = '20s'

    print('<div class="contained %s">' % dec)
    print('     <div class="container">')
    print('         <img src=content\%s.jpg>'  % movs[:-1])
    print('         <div class="overlay"></div>')
    print('         </div>')
    print('         <a href="https://www.youtube.com/results?search_query=%s">' % movs[:-1])
    print('             <div class="text"><b>%s</b></div>' % (mov))
    print('             <p class="text"> Directed by %s (%s)</p>' % (dire[:-2], year[:-1]))
    print('         </a>')
    print('     <div class="bio">bio</div>')
    print('</div>')
    print('')



