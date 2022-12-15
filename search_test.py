import chromedriver_autoinstaller
import geckodriver_autoinstaller
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Install webdrivers
geckodriver_autoinstaller.install()
chromedriver_autoinstaller.install()

def get_repo(query):
    github_search_api = "https://api.github.com/search/repositories"
    query_param = "?q="
    response = requests.get(f"{github_search_api}{query_param}{query}", 
        headers = {"Accept": "application/vnd.github+json",
                   "X-GitHub-Api-Version": "2022-11-28"})

    payload = response.json()
    return payload['items'][0]['html_url']

@pytest.mark.parametrize(
    "driver, query",
    [
        # Case 1 - Chrome
        pytest.param(
            webdriver.Chrome(),
            "create-react-app",
            id="chrome"),
        # Case 2 - Firefox
        pytest.param(
            webdriver.Firefox(),
            "create-react-app",
            id="firefox")
    ])
def test_repo_contents(driver, query):
    """
    """
    repo_url = get_repo(query)
    driver.get(repo_url)

    expected_about_text = "Set up a modern web app by running one command."

    about = driver.find_elements(By.CSS_SELECTOR, "p.f4.my-3")
    assert about[0].text == expected_about_text

    driver.close()