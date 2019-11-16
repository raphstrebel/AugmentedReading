from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
import requests as rq

themes = ["fire", "rain", "wind", "forest","water"]
themes_dict = {}
for theme in themes:
    link = "https://inspirassion.com/en/related/" + theme
    req = rq.get(link)
    page = bs(req.text)
    strongs = page.find_all("strong")
    for val in strongs:
        themes_dict[val.text] = theme