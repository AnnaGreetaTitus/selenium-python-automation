# Selenium Dropdown Automation

This project demonstrates how to automate dropdown handling using Selenium with Python.

## Website Used

https://demoqa.com/select-menu

## Concepts Covered

* React Dropdown Handling
* Normal HTML Dropdown Handling
* Select Class
* XPath Locators
* Dropdown Option Validation

## Tools & Technologies

* Python
* Selenium WebDriver
* ChromeDriver
* VS Code

## Scenario Automated

### React Dropdown

* Open custom React dropdown
* Select:
  * `Group 2, option 1`

### Old Style Dropdown

* Use Selenium `Select` class
* Select:
  * `Purple`

### Dropdown Validation

* Print selected option
* Print all available dropdown options

## Locator Strategies Used

| Locator Type | Purpose               |
| ------------ | --------------------- |
| XPath        | React dropdown        |
| XPath        | React dropdown option |
| XPath        | Old style dropdown    |

## Select Methods Learned

### Select by visible text
```python
select_by_visible_text("Purple")
```

### Select by value
```python
select_by_value("2")
```

### Select by index
```python
select_by_index(1)
```

## Learning Outcome

Through this practice, I learned:

* Difference between normal and React dropdowns
* How to handle custom dropdowns manually
* How Selenium Select class works
* How to print dropdown values
* How to use XPath for dropdown automation

## Author

Anna Greeta Titus
