
class GithubRepoPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.sidebar = driver.find_element(By.CLASS_NAME, "Layout-sidebar")
        self.sidebar_links = self.sidebar.find_elements(By.CSS_SELECTOR, "a.Link--muted")

    locators = {
        "sidebar": ("CLASS_NAME", "Layout-sidebar")
    }