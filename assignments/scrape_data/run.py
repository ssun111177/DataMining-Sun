import sys
import requests
import time
import random
import json

Movie_names = []

for i in range(0,6):
    i=str(i+1)
    url = "http://www.yifysubtitles.com/browse/page-"+i
    print(url)
    html = requests.get(url).text.split('\n')

    for line in html:
        found = line.find('class="media-object"')

        if found > 0:
            line = line[found:]
            pos = line.find('alt="')

            Movie_names.append(line[pos + 5:-34])


    time.sleep(random.randint(0, 1))
print (Movie_names)

with open('data.json','w') as file:
    movie=json.dumps(Movie_names,indent=1)
    file.write(movie)
