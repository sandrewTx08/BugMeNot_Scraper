
<img src="http://bugmenot.com/assets/img/logo.png">

# BugMeNot_Scraper
### Retrieve BugMeNot webpage share login.

# Goal:
### Return share login information:
- **Username**
- **Password**

So on  and other attributes.

# Tools utilized & Requirements:
- ### Browser automation:
    `selenium` ChromeWebdriver for browser automation.

- ### Creating Table:
    `pandas` creates table containing all find share login.

## Output example:
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Username</th>
      <th>Password</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>test.account1@email.com</td>
      <td>passwordTEST1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>test.account2@email.com</td>
      <td>passwordTEST2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>test.account3@email.com</td>
      <td>passwordTEST3</td>
    </tr>
  </tbody>
</table>

# Usage:
### 1. Download all requirements and install it.
2. Execute the `python test_main.py`
3. Type a site with some kind of authentication
4. Scraping logins
5. A table is created in **HTML** format
