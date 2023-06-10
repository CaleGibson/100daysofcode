import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
start = response.text
soup = BeautifulSoup(start, "html.parser")

title_info = soup.find_all(name="h3", class_="title")

list = []
for h3 in title_info:
    list.append(h3.text)


new_list = list[::-1]
for movie in new_list:
    print(movie)
with open("movies.txt", mode="w")as file:
    for movie in new_list:
        file.write(f"{movie}\n")