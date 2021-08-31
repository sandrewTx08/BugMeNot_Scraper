import unittest
import selenium.common.exceptions
from setup import DriverSetup as Browser
import pandas as pd


class Test_A_ShareLogin(unittest.TestCase):
    """ Test all share logins attributes """

    """ URL """
    url = Browser.page.url(input('[URL]: '))

    def setUp(self):
        """ Wait for amount of time each test """
        Browser.page.implicitly_wait()

    def test_A1_not_found(self):
        """ Seek 'not found' response """
        try:
            Browser.page.not_found()

        except selenium.common.exceptions.TimeoutException:
            """ 'Not found' response not found """

    def test_A2_denied(self):
        """ Seek 'denied' response """
        try:
            Browser.page.denied()

        except selenium.common.exceptions.TimeoutException:
            """ Denied response not found """

    username_row = []
    def test_A3_username(self):
        """ Test usernames """
        for username in Browser.page.username():
            """ Assert usernames """
            self.assertIsNotNone(username)

            """ Append attribute in arrays """
            self.username_row.append(username.text)

    password_row = []
    def test_A4_password(self):
        """ Test passwords """

        for password in Browser.page.password():
            """ Assert passwords """
            self.assertIsNotNone(password)

            """ Append attribute in arrays """
            self.password_row.append(password.text)

    success_rate_row = []
    def test_A5_success_rate(self):
        """ Test success rates """

        for success_rate in Browser.page.success_rate():
            """ Assert success rate """
            self.assertIsNotNone(success_rate)

            """ Append attribute in arrays """
            self.success_rate_row.append(success_rate.text[:-12])

    votes_row = []
    def test_A6_votes(self):
        """ Test votes """

        for votes in Browser.page.votes():
            """ Assert votes """
            self.assertIsNotNone(votes)

            """ Append attribute in arrays """
            self.votes_row.append(votes.text[:-5])

    login_age_row = []
    def test_A7_login_age(self):
        """ Test login ages """

        for login_age in Browser.page.login_age():
            """ Assert login ages """
            self.assertIsNotNone(login_age)

            """ Append attribute in arrays """
            self.login_age_row.append(login_age.text[:-3])

    # other_row = []
    # def test_8_other(self):
    #     """ Test 'other' """
    #     for other in Browser.page.other():
    #         """ Assert 'other' """
    #         self.assertIsNotNone(other)
    #
    #         """ Append attribute in arrays """
    #         self.other_row.append(other.text)


class Test_B_Table(unittest.TestCase):
    """ Create a table based on Username and Password results """

    def test_B1_create_table(self):
        """ Create a dictionary with arrays """
        share_login = Test_A_ShareLogin()
        return {
            'Username': share_login.username_row,
            'Password': share_login.password_row,
            'Success_Rate': share_login.success_rate_row,
            'Votes': share_login.votes_row,
            'Login_Age': share_login.login_age_row,
        }

    def test_B2_save_output(self):
        """ Convert dictionary to sheet """
        df = pd.DataFrame.from_dict(self.test_B1_create_table())
        print(df)

        try:
            """ Save sheet as file output """
            file_name = f"{Test_A_ShareLogin.url.replace('.', '_')}"
            df.to_html(f'report/{file_name}.html', encoding='utf-8')
            df.to_csv(f'report/{file_name}.csv',  encoding='utf-8')

        except ResourceWarning:
            """ Exception while file is opened by system """

        except PermissionError:
            """ Exception while file is opened by system """

    @classmethod
    def tearDownClass(cls):
        """ End of test"""
        Browser().close_browser()


if __name__ == '__main__':
    unittest.main(verbosity=2)
