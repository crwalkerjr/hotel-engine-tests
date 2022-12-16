import chromedriver_autoinstaller
import geckodriver_autoinstaller
import pytest
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Install webdrivers
geckodriver_autoinstaller.install()
chromedriver_autoinstaller.install()


# HELPER FUNCTIONS

def get_repo(query):
    """
    """
    github_search_api = "https://api.github.com/search/repositories"
    query_param = "?q="
    response = requests.get(f"{github_search_api}{query_param}{query}", 
        headers = {"Accept": "application/vnd.github+json",
                   "X-GitHub-Api-Version": "2022-11-28"})

    payload = response.json()
    return payload['items'][0]['html_url']


def parse_license(list_of_rows):
    """
    """
    license_text = """"""
    for text in [row.text for row in list_of_rows]:
        license_text += f"{text}\n"
    return license_text.rstrip("\n")   # remove final newline


# TESTS

@pytest.mark.parametrize(
    "driver, query, expected_about_text, expected_license_filename",
    [
        # Case 1 - Chrome
        pytest.param(
            webdriver.Chrome(),
            "create-react-app",
            "Set up a modern web app by running one command.",
            "expected_license.txt",
            id="chrome"),
        # Case 2 - Firefox
        pytest.param(
            webdriver.Firefox(),
            "create-react-app",
            "Set up a modern web app by running one command.",
            "expected_license.txt",
            id="firefox")
    ])
def test_repo_contents(driver, query, expected_about_text, expected_license_filename):
    """
    """
    repo_url = get_repo(query)
    driver.implicitly_wait(5)
    driver.get(repo_url)

    sidebar = driver.find_element(By.CLASS_NAME, "Layout-sidebar")

    about = sidebar.find_element(By.CSS_SELECTOR, "p.f4.my-3")
    assert about.text == expected_about_text

    license = sidebar.find_elements(By.CSS_SELECTOR, "a.Link--muted")[1]

    license.click() 

    license_file_list_of_rows = driver.find_elements(By.CLASS_NAME, "blob-code.blob-code-inner.js-file-line")

    license_text = parse_license(license_file_list_of_rows)

    with open(expected_license_filename) as f:
        expected_license = f.read()
        assert license_text == expected_license


    driver.close()

