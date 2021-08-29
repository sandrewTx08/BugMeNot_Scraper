import unittest
import selenium.common.exceptions
from setup import DriverSetup as Browser
import pandas as pd


class TestShareLogin(unittest.TestCase):
    """ Retrieve BugMeNot webpage share login """
    @classmethod
    def setUpClass(cls):
        """ Setup class for Webdriver tests """
        cls.url = Browser.page.url(url=input('[URL] : '))

    def setUp(self):
        """ Wait for amount of time each test """
        Browser.page.implicitly_wait()

    def test_page(self):
        """ Access BugMeNot page """
        try:
            self.assertEqual(Browser.driver.title[-8:], 'BugMeNot')

        except selenium.common.exceptions.WebDriverException:
            """ Close browser on failure """
            Browser().close_browser()

    @classmethod
    def test_not_found(cls):
        """ Seek 'not found' response """
        try:
            Browser.page.not_found()

        except selenium.common.exceptions.TimeoutException:
            """ 'Not found' response not found """

    @classmethod
    def test_denied(cls):
        """ Seek 'denied' response """
        try:
            Browser.page.denied()

        except selenium.common.exceptions.TimeoutException:
            """ Denied response not found """

    def test_username(self):
        """ Assert usernames """
        for username in Browser.page.username():
            self.assertIsNotNone(username)

    def test_password(self):
        """ Assert passwords """
        for password in Browser.page.password():
            self.assertIsNotNone(password)

    def test_success_rate(self):
        """ Assert success rate """
        for success_rate in Browser.page.success_rate():
            self.assertIsNotNone(success_rate)

    def test_votes(self):
        """ Assert votes """
        for votes in Browser.page.votes():
            self.assertIsNotNone(votes)

    def test_login_age(self):
        """ Assert login ages """
        for login_age in Browser.page.login_age():
            self.assertIsNotNone(login_age)

    def test_table_creation(self):
        """ Create a table based on Username and Password results """

        """ Store login information in arrays"""
        username_row = []
        for username in Browser.page.username():
            username_row.append(username.text)

        """ Store login information in arrays"""
        password_row = []
        for password in Browser.page.password():
            password_row.append(password.text)

        """ Store login information in arrays"""
        success_rate_row = []
        for success_rate in Browser.page.success_rate():
            success_rate_row.append(success_rate.text[:-12])

        """ Store login information in arrays"""
        votes_row = []
        for votes in Browser.page.votes():
            votes_row.append(votes.text[:-5])

        """ Store login information in arrays"""
        login_age_row = []
        for login_age in Browser.page.login_age():
            login_age_row.append(login_age.text[:-3])

        """ Create a dictionary with arrays from all logins """
        sheet = {
            'Username': username_row,
            'Password': password_row,
            'Success_Rate': success_rate_row,
            'Votes': votes_row,
            'Login_Age': login_age_row
        }

        """ Build a table output from sheet """
        df = pd.DataFrame(sheet)
        try:
            """ Save table as file in 'report' folder
            Format example: 'test_com.html' """

            file_name = f"{self.url.replace('.', '_')}"
            df.to_html(f'report/{file_name}.html')
            df.to_csv(f'report/{file_name}.csv')

        except ResourceWarning:
            """ Exception while file is opened by system """

        except PermissionError:
            """ Exception while file is opened by system """
        print(df)

    @classmethod
    def tearDownClass(cls):
        """ End of test"""
        Browser().close_browser()


if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)
