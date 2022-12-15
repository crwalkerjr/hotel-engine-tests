import chromedriver_autoinstaller
import geckodriver_autoinstaller
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



github_search_api = "https://api.github.com/search/repositories"
query_param = "?q="
query = "create-react-app"

response = requests.get(f"{github_search_api}{query_param}{query}", 
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"})

payload = response.json()
url = payload['items'][0]['html_url']

geckodriver_autoinstaller.install()
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get(url)

expected_about_text = "Set up a modern web app by running one command."

about = driver.find_elements(By.CSS_SELECTOR, "p.f4.my-3")
assert about[0].text == expected_about_text

driver.close()