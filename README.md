
<img src="http://bugmenot.com/assets/img/logo.png">

# BugMeNot_Scraper
Retrieve BugMeNot webpage share login through _Page Object Model_ (POM), exporting results.

# Usage:
1. Download all requirements and install it.
2. Execute the `python test_main.py`.
3. Type wanted URL. 
4. Wait scraping logins.
5. table is created in **HTML** and **CSV** format.

# Goal:
 Return share login information:
- **Username**
- **Password**
- **Success rate**
- **Votes**
- **Login age**

### Colect all share login data from a file list!.
1. Assure `url_list.text` is in project folder.
2. Execute `python automated_list.py`.
3. Wait until run all URL inside document lines is done.

#### Document example:
```
test.com
example.com
fake.com
site.com
```
All URL inside file document will be executed at BugMeNot search and then a table output is recorded.

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

Files saved as: `/report/site_com.html`  
## Tools utilized & Requirements:
-  ### Browser automation:
    `selenium` ChromeWebdriver for browser automation.

- ### Creating Table:
    `pandas` creates table containing all find share login.
