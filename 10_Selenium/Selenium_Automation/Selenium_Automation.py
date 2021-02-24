from selenium import webdriver

chrome_browser = webdriver.Chrome('/Users/roger-that/Documents/Roger-That/Dev/Assets/Selenium_Drivers/chromedriver')
#! One option is to save all the driver into /user/local/bin

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

#! Try to check if We are on the right page
#+ We have to target some html to check. In this case we are targetting the title of the page
print('Selenium Easy Demo' in chrome_browser.title)

#! Assert - this will check if the value exists, if not it will stop our code and error out
assert 'Selenium Easy Demo' in chrome_browser.title
# Returns True

#! Targetting a button
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
print(show_message_button)
# Output -> <selenium.webdriver.remote.webelement.WebElement (session="e73d081f34615d80a19dd251db2ecf01", element="950857de-288c-4f32-8ad4-4e98c2e0c457")>
#    We are getting a WebElement
print(show_message_button.get_attribute('innerHTML'))
# Output -> Show message

#! Example 1 - Using Id
assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Hello there, how are you?')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'Hello there, how are you?' in chrome_browser.page_source

#! Example 2 - Using CSS
assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_button = chrome_browser.find_element_by_css_selector('#get-input > .btn')
user_message.clear()
user_message.send_keys('Hello there, how are you?')

show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'Hello there, how are you?' in chrome_browser.page_source

#! Close browsers
chrome_browser.close()
chrome_browser.close()
# Closes all the instaces of the chrome, if we opened more than one chrome during the test
# chrome_browser.quit()