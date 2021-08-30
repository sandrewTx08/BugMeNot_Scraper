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

        """ The <seconds_time> time to wait for elements appear on page """
        self.seconds_time = 2
        self.wait = WebDriverWait(self.driver, self.seconds_time)

    def url(self, url):
        """ Search shared login based on URL argument """
        self.driver.get(f'http://bugmenot.com/view/{url}')
        return url

    def implicitly_wait(self):
        """ Wait elements on page """
        self.driver.implicitly_wait(self.seconds_time)

    def not_found(self):
        """ Return page object """
        return self.wait.until(EC.visibility_of_element_located((Locators.NOT_FOUND)))

    def denied(self):
        """ Return page object """
        return self.wait.until(EC.visibility_of_element_located((Locators.DENIED)))

    """ Returns all share login information:
    Username, Password, Success rate, Votes and Login age.
    """
    def username(self):
        """ Return values """
        for username in self.wait.until(EC.visibility_of_all_elements_located((Locators.USERNAME))):
            yield username

    def password(self):
        """ Return values """
        for password in self.wait.until(EC.visibility_of_all_elements_located((Locators.PASSWORD))):
            yield password

    def success_rate(self):
        """ Return values """
        for success_rate in self.wait.until(EC.visibility_of_all_elements_located((Locators.SUCCESS_RATE))):
            yield success_rate

    def votes(self):
        """ Return values """
        for votes in self.wait.until(EC.visibility_of_all_elements_located((Locators.VOTES))):
            yield votes

    def login_age(self):
        """ Return values """
        for login_age in self.wait.until(EC.visibility_of_all_elements_located((Locators.LOGIN_AGE))):
            yield login_age

    def other(self):
        for other in self.wait.until(EC.visibility_of_all_elements_located((Locators.OTHER))):
            yield other
