import chromedriver_autoinstaller
import geckodriver_autoinstaller
import pytest
import requests
import time
from pages.LicensePage import LicensePage
from pages.RepoPage import RepoPage
from selenium import webdriver
from selenium.webdriver.common.by import By

# Install webdrivers
geckodriver_autoinstaller.install()
chromedriver_autoinstaller.install()


# HELPER FUNCTIONS

def get_repo(query):
    """ Utility function to query Github's search api and return the given repo's url
    
    :param: query: string of repo to be queried
    :return: string of queried repo's url
    """
    github_search_api = "https://api.github.com/search/repositories"
    query_param = "?q="
    response = requests.get(f"{github_search_api}{query_param}{query}", 
        headers = {"Accept": "application/vnd.github+json",
                   "X-GitHub-Api-Version": "2022-11-28"})

    payload = response.json()
    return payload['items'][0]['html_url']


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
    """ Test to verify the "About" text and license of a GitHub repository

    :param: driver: Selenium WebDriver browser
    :param: query: GitHub repo to be queried
    :param: expected_about_text: string of expected About text
    :param: expected_license_filename: string for filename containing expected licesnse text
    """
    repo_url = get_repo(query)
    driver.implicitly_wait(5)
    driver.get(repo_url)
    repo_page = RepoPage(driver)

    assert repo_page.about.text == expected_about_text

    repo_page.license_link.click() 

    license_page = LicensePage(driver)

    with open(expected_license_filename) as f:
        expected_license = f.read()
        assert license_page.license_text == expected_license

    driver.close()

