from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv
import requests

link ="https://www.booking.com/hotel/index.fr.html?label=gen173nr-10CAEoggI46AdIM1gEaECIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4Auq28tYGwAIB0gIkZDU3NWE1ZjQtMDY0Yi00MmQ5LTljZDctNWI0NmQ4MzI5MDZi2AIB4AIB&aid=304142"

hotels_datails = []

def booking():

 browser = webdriver.Chrome()
 browser.get(link)
 time.sleep(5)

 
 items = browser.find_elements("class name","fd6e9622ae")
 
 time.sleep(20)

 for i in items :
  try:
   hotel_name= i.find_element("class name","cc045b173b").text.strip()
  except:
   continue
  try:
   hotel_place = i.find_element("class name","b57285a9c3").text.strip()
  except:
   continue
  try:
   hotel_rating = i.find_element("class name","dff2e52086").text.strip()
  except:
   continue
  try:
   hotel_price = i.find_element("class name","d387ed9fbd").text.strip()
  except:
   continue
  hotels_datails.append({ 
    "hotel name" :hotel_name,
    "hotel place": hotel_place,
    "hotel rating": hotel_rating,
    "hotel price" : hotel_price,
   })

 def printing():
  header =hotels_datails[0].keys()
  path = r"C:\Users\Abdeldjalil\Desktop\hotels_daitals.csv"
  with open(path,"w") as file:
   writer = csv.DictWriter(file, header)
   writer.writeheader()
   writer.writerows(hotels_datails)
   print("file printed !")

 printing()
booking()

