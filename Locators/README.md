# Selenium Locators Practice

This project demonstrates Selenium automation using Python with different locator strategies and explicit waits.

## Website Used

https://the-internet.herokuapp.com/login

## Concepts Covered

* ID Locator
* Name Locator
* XPath Locator
* Explicit Waits
* Login Automation
* Logout Automation
* Error Message Validation

## Tools & Technologies

* Python
* Selenium WebDriver
* ChromeDriver
* VS Code

## Scenario Automated

### Invalid Login Test

* Enter wrong username and password
* Click Login
* Capture and print error message

### Valid Login Test

* Enter correct username and password
* Click Login
* Capture and print success message
* Logout successfully

## Locator Strategies Used

| Locator Type | Example       |
| ------------ | ------------- |
| Name         | username      |
| ID           | password      |
| XPath        | Login button  |
| XPath        | Logout button |

## Waits Used

This project uses Explicit Waits with:

* `visibility_of_element_located`
* `element_to_be_clickable`
* `presence_of_element_located`

## Learning Outcome

Through this practice, I learned:

* How to use different Selenium locators
* How to automate login functionality
* How to use explicit waits properly
* How to validate messages after actions
* How to improve script stability

## Author

Anna Greeta Titus
