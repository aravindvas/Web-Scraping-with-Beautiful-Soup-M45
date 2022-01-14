import requests
from bs4 import BeautifulSoup

rsp2 = requests.get(url="https://www.imdb.com/chart/top/")
dat = rsp2.text

soup2 = BeautifulSoup(dat, "html.parser")

lk = soup2.find_all(name="a")
num = soup2.find_all(name="td", class_="titleColumn")
# mv = [jk.getText() for jk in lk]
# print(mv)
no = [ik.getText() for ik in num]
for lo in no:
    print(lo)
with open("movies.txt", mode="w") as fl:
    for kk in no:
        fl.write(kk)