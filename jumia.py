import os
import requests as r
from bs4 import BeautifulSoup


response = r.get("https://www.jumia.co.ke/home-office-appliances/")
jumia_text = response.text

soup = BeautifulSoup(jumia_text, "html.parser")

items = (soup.find_all("div", class_= "img-c"))
print (len(items))



# response  = requests.get(mainurl)
# if response.ok:
#  soup = BeautifulSoup(response.text, "lxml")
#  title = str(soup.find("title"))
#  title = title.replace("<title>", "")
#  title = title.replace("</title>", "")
#  print("The title is : " + str(title))
# os.system("pause")


