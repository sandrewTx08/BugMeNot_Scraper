import unittest
from setup import DriverSetup as Browser
import pandas as pd


class Test_A_AutomatedList(unittest.TestCase):
    """ Colect all share login data from a file list """

    def test_A2_automatedlist(self):
        """ Execution of automated list """

        username_row = []
        def username():
            for username in Browser.page.username():
                """ Append attribute in arrays """
                username_row.append(username.text)

        password_row = []
        def password():
            for password in Browser.page.password():
                """ Append attribute in arrays """
                password_row.append(password.text)

        success_rate_row = []
        def success_rate():
            for success_rate in Browser.page.success_rate():
                """ Append attribute in arrays """
                success_rate_row.append(success_rate.text[:-12])

        votes_row = []
        def votes():
            for votes in Browser.page.votes():
                """ Append attribute in arrays """
                votes_row.append(votes.text[:-5])

        login_age_row = []
        def login_age():
            for login_age in Browser.page.login_age():
                """ Append attribute in arrays """
                login_age_row.append(login_age.text[:-3])

        def append_rows():
            """ Append attributes function call """
            username()
            password()
            success_rate()
            votes()
            login_age()

        def append_rows_clear():
            """ Clear login arrays """
            username_row.clear()
            password_row.clear()
            success_rate_row.clear()
            votes_row.clear()
            login_age_row.clear()

        def save_output():
            """ Save output as file """

            """ Create a dictionary with arrays 
            Convert dictionary to sheet     """
            df = pd.DataFrame.from_dict({
                'Username': username_row,
                'Password': password_row,
                'Success_Rate': success_rate_row,
                'Votes': votes_row,
                'Login_Age': login_age_row,
            })

            """ Save sheet as file output """
            file_name = f"{line.replace('.', '_')}"
            file_name = file_name.replace('\r\n', '')
            df.to_html(f'report/{file_name}.html', encoding='utf-8')
            df.to_csv(f'report/{file_name}.csv', encoding='utf-8')

        """ Work 
        1. Read line from document then access URL
        2. Append all share login attributes 
        3. Sheet is created after saved as filename
        4. Appended row are cleaned
        5. Back to loop until lines is read and executed
        """
        list_file_name = 'url_list.txt'
        with open(f'.\\{list_file_name}', 'r', newline='') as url_list:

            def count_lines():
                with open(f'.\\{list_file_name}', 'r', newline='') as url_list:
                    for count, line in enumerate(url_list):
                        pass
                return count + 1

            lines_len = count_lines()
            counter = 0

            for line in url_list.readlines():
                Browser.page.url(line)

                counter += 1
                line = line.replace('\r\n', '')
                print(f'COUNTER:[{counter}] / MAX:[{lines_len}] | SITE:[{line}]')

                if counter == lines_len:
                    print('SUCCESS EVERY LOGIN CATALOGED!')

                append_rows()
                save_output()
                append_rows_clear()

            url_list.close()

    @classmethod
    def tearDownClass(cls):
        """ End of test"""
        Browser().close_browser()


if __name__ == '__main__':
    unittest.main(verbosity=2)
