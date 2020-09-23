# This is the file for scraping the web and finding the data behind-the-scenes

# Imports And Setup
import requests
from bs4 import BeautifulSoup, SoupStrainer
website = requests.get("https://www.worldometers.info/coronavirus/")
parse_ref = SoupStrainer(id="nav-tabContent")
parse_ref2 = SoupStrainer("title")
soup = BeautifulSoup(website.text, "lxml", parse_only=parse_ref)
soup2 = BeautifulSoup(website.text, "lxml", parse_only=parse_ref2)

# Finds Total Numbers
total_list = soup2.title.string.replace("Coronavirus Update (Live): ", "").replace(" Deaths from COVID-19 Virus Pandemic - Worldometer", "").split(" Cases and ")

# Initializes Web Scraping For Interface
def initialize_interface_scraping(region, num=0):
    parents = soup.select("a[href=\"country/" + region + "/\"]")[num].parents
    row = list(parents)[1]
    cell_list = []
    for child in row.children:
        if child.string != "\n":
            cell_list.append(child.string)
        if len(cell_list) == 5:
            break
    return [cell_list[2], cell_list[4], cell_list[0], cell_list[1]]

# Initializes Web Scraping For Learner
def initialize_learner_scraping(region):
    return [initialize_interface_scraping(region, num=1), initialize_interface_scraping(region, num=2)]