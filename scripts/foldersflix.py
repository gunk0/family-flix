import os
import string

folder = '/Volumes/Seagate Backup Plus Drive/WATCH MOVIE/Romance'
parent = '/Volumes/Seagate Backup Plus Drive/Flix/content/mov'

def remove(string):
    return string.replace(" ", "-")


dirlist = [item for item in os.listdir(folder) if os.path.isdir(os.path.join(folder,item))]
for item in dirlist:
    folder=item.split(",")
    folder=item.lstrip("']")
    mov,dire,year=item.split("(")
    movs=remove(mov)
    path1= os.path.join(parent,movs[:-1])
    if not os.path.exists(path1):
        os.mkdir(path1)
    else:
        pass
    path2= os.path.join(path1,"img")
    if not os.path.exists(path2):
        os.mkdir(path2)
    else:
        pass
    path3= os.path.join(path1,"sample")
    if not os.path.exists(path3):
        os.mkdir(path3)
    else:
        pass

    print('<div class="contained">')
    print('     <div class="container">')
    print('         <img src=content\%s.jpg>'  % movs[:-1])
    print('         <div class="overlay"></div>')
    print('         </div>')
    print('         <a href="https://www.youtube.com/results?search_query=%s">' % movs[:-1])
    print('             <div class="text">Check out <b>%s</b></div>' % (mov))
    print('             <p class="text"> Directed by %s (%s)</p>' % (dire[:-2], year[:-1]))
    print('         </a>')
    print('     <div class="bio">bio</div>')
    print('</div>')
    print('')


