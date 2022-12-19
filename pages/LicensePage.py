from selenium.webdriver.common.by import By

class LicensePage(object):
    """ LicensePage Page Object to manage elements from license page

    :param: driver: Browser as a selenium webdriver
    """

    def __init__(self, driver):
        self.driver = driver
        self.license_text = self.parse_license_text()

    def parse_license_text(self):
        """ Utility method to parse license text from list of table rows

        :param: list of text rows from html table containing license text
        :return: string of license text
        """
        list_of_rows = self.driver.find_elements(By.CLASS_NAME, "blob-code.blob-code-inner.js-file-line")
        license_text = ""
        for text in [row.text for row in list_of_rows]:
            license_text += f"{text}\n"
        return license_text.rstrip("\n")   # remove final newline