from selenium.webdriver.common.by import By
""" Shortcuts

= (By.XPATH, '')
= (By.XPATH, '//*[@]')

= (By.XPATH, "")
= (By.XPATH, "//*[@]")

"""


class PageLocators(object):
    """ Location for elements path in the page """

    """ Exception locations """
    NOT_FOUND = (By.XPATH, "//*[text()='No logins found. Please register a fake account then ']")
    DENIED = (By.XPATH, "//*[text()='This site has been barred from the bugmenot system.']")

    """ Target locations """
    USERNAME = (By.XPATH, '//*[@class="account"]/dl/dd[1]')
    PASSWORD = (By.XPATH, '//*[@class="account"]/dl/dd[2]')
    OTHER = (By.XPATH, '//*[@class="account"]/dl/dd[3]/kbd')
    SUCCESS_RATE = (By.XPATH, '//*[@class="account"]/dl/dd[@class="stats"]/ul/li[@class]')
    VOTES = (By.XPATH, '//*[@class="account"]/dl/dd[@class="stats"]/ul/li[2]')
    LOGIN_AGE = (By.XPATH, '//*[@class="account"]/dl/dd[@class="stats"]/ul/li[3]')
