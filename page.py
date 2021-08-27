from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import PageLocators as Locators
""" Shortcuts

self.driver.find_element(*locators.)
self.driver.find_elements(*locators.)

self.wait.until(EC.visibility_of_element_located((locators.)))
self.wait.until(EC.visibility_of_all_elements_located((locators.)))
self.wait.until(EC.visibility_of_any_elements_located((locators.)))

"""


class PageObject(object):
    def __init__(self, driver):
        """ Interact with page objects """
        self.driver = driver
        self.locator = Locators

        """ The <seconds_time> time to wait for elements appear on page 
        2 - May cause issues, but fast
        5 - Stable 
        """
        seconds_time = 5
        self.wait = WebDriverWait(self.driver, seconds_time)

    def not_found(self):
        """ Return page object """
        return self.wait.until(EC.visibility_of_element_located((Locators.NOT_FOUND)))

    def denied(self):
        """ Return page object """
        return self.wait.until(EC.visibility_of_element_located((Locators.DENIED)))

    def username(self):
        """ Return all username found """
        for username in self.wait.until(EC.visibility_of_all_elements_located((Locators.USERNAME))):
            yield username

    def password(self):
        """ Return all password found """
        for password in self.wait.until(EC.visibility_of_all_elements_located((Locators.PASSWORD))):
            yield password
