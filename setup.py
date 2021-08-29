from selenium import webdriver
from page import PageObject as Page
import sys


class DriverSetup:
    def close_browser(self):
        """ Close terminal"""
        self.driver.close()
        self.driver.quit()
        sys.exit()

    """ Setup Webdriver test """
    driver_path = r'D://chromedriver.exe'

    """ Call the options class """
    chrome_options = webdriver.ChromeOptions()

    """ Disable images """
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

    """ Optional args """
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--proxy-server=%s' % '')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--test-type")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--verbose")

    """ Load webdriver """
    driver = webdriver.Chrome(driver_path, options=chrome_options)

    """ Page Object """
    page = Page(driver)

    """ URL """
    url = page.url(input('[URL] : '))
