
<img src="http://bugmenot.com/assets/img/logo.png">

# BugMeNot_Scraper
Retrieve BugMeNot webpage share login through _Page Object Model_ (POM), exporting results.

# Goal:
### Return share login information:
- **Username**
- **Password**
- **Success rate**
- **Votes**
- **Login age**

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
      <th>Success_Rate</th>
      <th>Votes</th>
      <th>Login_Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>testaccount@email.com</td>
      <td>passwordTest</td>
      <td>64%</td>
      <td>45</td>
      <td>5 months</td>
    </tr>
    <tr>
      <th>1</th>
      <td>testingfakeaccount</td>
      <td>passfake123</td>
      <td>39%</td>
      <td>201</td>
      <td>7 months</td>
    </tr>
    <tr>
      <th>2</th>
      <td>fakeaccount</td>
      <td>123456</td>
      <td>13%</td>
      <td>616</td>
      <td>2 years</td>
    </tr>
  </tbody>
</table>

#### File saved as: `/report/site_com.html`  

# Usage:
### 1. Download all requirements and install it.
2. Execute the `python test_main.py`
3. Type URL
4. Wait scraping logins
5. A table is created in **HTML** and **CSV** format.
