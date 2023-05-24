import os
import requests 
from bs4 import BeautifulSoup
import csv



response = requests.get("https://www.jumia.co.ke/home-office-appliances/")
if response.status_code != 200:
    print("Error: Failed to retrieve the webpage.")
    exit()

jumia_text = response.text

soup = BeautifulSoup(jumia_text, "html.parser")

appliance_list = []
appliances = (soup.find_all("div", class_= "info"))
if not appliances:
    print ("No appliances in this webpage.")
else:
    for appliance in appliances:
        # appliance_img = appliance.find ("img-c") 
        appliance_name = appliance.find("h3").text if appliance.find("h3") else "unavailable"
        appliance_price = appliance.find ("div" ,class_="prc").text if appliance.find("div", class_="prc") else "unavailable"
        applliance_discount = appliance.find("div" ,class_="bdg _dsct _sm").text if appliance.find("div", class_="bdg _dsct _sm") else "unavailable"
        appliance = {'name': appliance_name, 'price': appliance_price, 'discount': applliance_discount}
        appliance_list.append(appliance)

print(appliance_list)

if appliance_list:
    with open ("appliances.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=appliance_list[0].keys())
        writer.writeheader()
        for appliance in appliance_list:
            writer.writerow(appliance)
else:
    print("No data to write to CSV file")
        
        


