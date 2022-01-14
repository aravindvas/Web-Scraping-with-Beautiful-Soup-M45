from bs4 import BeautifulSoup
import lxml
import requests

rsp =requests.get(url="https://news.ycombinator.com")
txt = rsp.text

soup = BeautifulSoup(txt, "html.parser")
print(soup.title)
links = soup.find_all(name="a", class_="storylink")
txt = []
lnk = []
for k in links:
    txt2 = k.getText()
    txt.append(txt2)
    lnk2 = k.get("href")
    lnk.append(lnk2)
link2 = [int(ij.getText().split()[0]) for ij in soup.find_all(name="span", class_="score")]

print(txt)
print(lnk)
mx = max(link2)
ind = link2.index(mx)
print(txt[ind])
print(lnk[ind])



# with open("website.html", encoding="utf8") as fl:
#     cont = fl.read()
#
# # sp = BeautifulSoup(cont, "html.parser")
# sp = BeautifulSoup(cont, "lxml")
# # print(sp.prettify())
# # print(sp.a)
# all = sp.find_all(name="a")
# print(all)
# for i in all:
#     print(i.getText())
#     print(i.get("href"))
#
# print(sp.find(name="h3",class_="heading"))
#
# print(sp.select_one(selector="#name"))
#
# print(sp.select(".heading"))