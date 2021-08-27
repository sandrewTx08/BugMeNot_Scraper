import unittest
import selenium.common.exceptions
import pandas as pd
from setup import DriverSetup
from datetime import datetime


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Setup class for Webdriver tests """
        cls.driver = DriverSetup.driver
        cls.page = DriverSetup.page
        cls.site = input('SITE: ')

    def test_(self):
        """ Access page """
        try:
            self.url = f'http://bugmenot.com/view/{self.site}'
            self.driver.get(self.url)

        except selenium.common.exceptions.WebDriverException:
            print(f'Can access "{self.site}", please verify you internet or proxy connection.')
            DriverSetup().close_browser()

    def test_not_found(self):
        """ Seek 'not found' response """
        try:
            print(f'CHECK: invalid results "{self.site}" response...')
            self.page.not_found()
            print(f'ERROR: Site not found "{self.site}" is invalid.')

        except selenium.common.exceptions.TimeoutException:
            print(f'CHECK: results found {self.site}.')

    def test_denied(self):
        """ Seek 'denied' response """
        try:
            print(f'CHECK: "{self.site}" allowed results response...')
            self.page.denied()
            print(f'ERROR: "{self.site}" is denied for results.')

        except selenium.common.exceptions.TimeoutException:
            print(f'CHECK: results allowed {self.site}.')

    def test_username(self):
        """ Assert site usernames """
        self.assertIsNotNone(self.page.username)

    def test_password(self):
        """ Assert site password """
        self.assertIsNotNone(self.page.password)

    def test_table_creation(self):
        """ Create a table based on Username and Password results """

        """ Store Usernames in array """
        username_row = []
        for username in self.page.username():
            username_row.append(username.text)

        """ Store Password in array """
        password_row = []
        for password in self.page.password():
            password_row.append(password.text)

        """ Create a sheet key with arrays containing the Username and Password """
        sheet = {
            'Username': username_row,
            'Password': password_row
        }

        """ Build a table output from sheet """
        try:
            df = pd.DataFrame(sheet)
            print(f'SUCCESS: Displaying accounts in "{self.site}".\n')
            print(df)

            """ Save table as file 
            Format example: testcom_01Jan2008.html
            """
            file_name = f"{self.site.replace('.', '')}_{datetime.now().strftime('%d%b%Y')}"
            print(f'File saved as "{file_name}"')
            df.to_html(f'{file_name}.html')

        except ResourceWarning:
            """ Exception while file is opened by system """

            print('Please, try close table output files!')
        except PermissionError:
            """ Exception while file is opened by system """

            print('Please, try close table output files!')

    @classmethod
    def tearDownClass(cls):
        """ End of test """
        DriverSetup().close_browser()


if __name__ == '__main__':
    unittest.main()
