from bs4 import BeautifulSoup
import requests

url = 'https://knewone.com/discover?page=7'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

print (soup)
