from setup import DriverSetup as Browser
import pandas as pd


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
    username()
    password()
    success_rate()
    votes()
    login_age()

def append_rows_clear():
    username_row.clear()
    password_row.clear()
    success_rate_row.clear()
    votes_row.clear()
    login_age_row.clear()

def save_output():
    df = pd.DataFrame.from_dict({
        'Username': username_row,
        'Password': password_row,
        'Success_Rate': success_rate_row,
        'Votes': votes_row,
        'Login_Age': login_age_row,
    })

    file_name = f"{line.replace('.', '_')}"
    file_name = file_name.replace('\r\n', '')
    df.to_html(f'report/{file_name}.html', encoding='utf-8')
    df.to_csv(f'report/{file_name}.csv', encoding='utf-8')


with open('url_list.txt', 'r', newline='') as url_list:
    for line in url_list.readlines():
        Browser.page.url(line)
        append_rows()
        save_output()
        append_rows_clear()

    Browser().close_browser()
    url_list.close()