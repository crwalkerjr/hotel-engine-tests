from selenium.webdriver.common.by import By

class RepoPage(object):
    """ RepoPage Page Object to manage elements from repository homepage

    :param: driver: Browser as a selenium webdriver    
    """
    def __init__(self, driver):
        self.driver = driver
        self.sidebar = driver.find_element(By.CLASS_NAME, "Layout-sidebar")
        self.sidebar_links = self.sidebar.find_elements(By.CSS_SELECTOR, "a.Link--muted")
        self.about = self.sidebar.find_element(By.CSS_SELECTOR, "p.f4.my-3")
        self.license_link = self.sidebar_links[1]
