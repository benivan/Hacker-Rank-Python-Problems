from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
data = BeautifulSoup(html,"html.parser")
namelist = data.find_all("span" , {"class" : "green"})
namelist1= data.findAll(text="the prince")
print(len(namelist1))
for name in namelist:
    print(name.get_text())












