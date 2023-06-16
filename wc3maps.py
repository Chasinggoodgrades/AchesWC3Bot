from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

from bs4 import BeautifulSoup

def map_search(keywords):
    url = "https://wc3maps.com/live"
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(15)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("tr")

    found_maps = []

    map_elements = soup.find_all("div", class_="mantine-Text-root mantine-1nf8cz8")

    ##print(map_elements)

    for element in map_elements:
        map_name_element = element.find("a")
        if map_name_element:
            map_name = map_name_element.get_text(strip=True)
            found_maps.append(map_name) ## Every Map in List, add to x List
            if any(keyword.lower() in map_name.lower() for keyword in keywords):
                map_name = re.sub(r"\d+\s+(seconds|minutes)\s+ago$", "", map_name)
                print(map_name) ## console debug
                print("-----")  ## console debug
    driver.close()

    found_maps = "\n".join(found_maps) ## Compiles all the maps into a nice new-lined list

    return found_maps

def getLobbies(keywords):
    url = "https://wc3maps.com/live"
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(15)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("tr")

    found_maps = []

    map_elements = soup.find_all("div", class_="mantine-Text-root mantine-1nf8cz8")

    ##print(map_elements)

    for element in map_elements:
        map_name_element = element.find("a")
        if map_name_element:
            map_name = map_name_element.get_text(strip=True)
            if any(keyword.lower() in map_name.lower() for keyword in keywords):
                map_name = re.sub(r"\d+\s+(seconds|minutes)\s+ago$", "", map_name)
                found_maps.append(map_name) ## Keyword Lobbies
                print(map_name)
                print("-----")
    driver.close()

    return found_maps



keywords = ["tower defense", "ts", "rkr", "Run Kitty Run", "RM", "RMK", "td"]
results = map_search(keywords)
print(results)
