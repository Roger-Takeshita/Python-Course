# SUMMARY

- [SUMMARY](#summary)
- [SELENIUM](#selenium)
  - [Selenium Links](#selenium-links)
  - [Installation Selenium](#installation-selenium)
  - [Drivers](#drivers)
    - [webdriver](#webdriver)
  - [Modules](#modules)
  - [Browser Arguments](#browser-arguments)
    - [Auto Download](#auto-download)
    - [Disable Notifications in FireFox](#disable-notifications-in-firefox)
    - [Open Specific Browser Using Binary](#open-specific-browser-using-binary)
  - [Selenium Commands](#selenium-commands)
    - [Read Browser Details](#read-browser-details)
    - [Go to a Specified URL](#go-to-a-specified-url)
    - [Locating Elements](#locating-elements)
      - [Python Selenium Commands for Operation on Elements](#python-selenium-commands-for-operation-on-elements)
    - [Waits](#waits)
      - [Expected Conditions](#expected-conditions)
      - [Custom Wait Conditions](#custom-wait-conditions)
      - [Explicit Waits](#explicit-waits)
      - [Implicit Waits](#implicit-waits)

# SELENIUM

## Selenium Links

[Go Back to Summary](#summary)

-   [Python Selenium Commands Cheat Sheet](http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/)
-   [Taking Screenshot Using Python Selenium WebDriver](http://allselenium.info/taking-screenshot-using-python-selenium-webdriver/)
-   [Capture screenshot of an Element using Python Selenium WebDriver](http://allselenium.info/capture-screenshot-element-using-python-selenium-webdriver/)
-   [Waits](https://selenium-python.readthedocs.io/waits.html)

## Installation Selenium

[Go Back to Summary](#summary)

-   Install globally

    ```Bash
      pip3 install selenium
    ```

## Drivers

[Go Back to Summary](#summary)

-   Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires **geckodriver**, which needs to be installed before the below examples can be run. Make sure it’s in your PATH, e. g., place it in `/usr/bin` or `/usr/local/bin`.

    | Chrome:  | https://sites.google.com/a/chromium.org/chromedriver/downloads        |
    | -------- | --------------------------------------------------------------------- |
    | Edge:    | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ |
    | Firefox: | https://github.com/mozilla/geckodriver/releases                       |
    | Safari:  | https://webkit.org/blog/6900/webdriver-support-in-safari-10/          |

### webdriver

[Go Back to Summary](#summary)

-   Import `webdriver` module from `selenium`
-   `webdriver` allow us to interact with the browser using code - `from selenium import webdriver`
-   **Driver setup**

```Python
  # Chrome
  chromedriver = webdriver.Chrome(executable_path=”Path to Chrome driver”)

  # Internet Explorer:
  iedriver = webdriver.IE(executable_path=”­Pat­h To­ IEDriverServer.exe”)

  # Edge:
  edgedriver = webdriver.Edge(executable_path=”­Pat­h To­ MicrosoftWebDriver.exe”)

  # Opera:
  operadriver = webdriver.Opera(executable_path=”­Pat­h To­ operadriver”)

  # Safari:
  # SafariDriver now requires manual installation of the extension prior to automation
```

## Modules

[Go Back to Summary](#summary)

-   Important modules to import

    ```Python
      from selenium import webdriver
      from selenium.webdriver.support.wait import WebDriverWait
      from selenium.webdriver.support import expected_conditions
      from selenium.webdriver.support.ui import Select

      from selenium.webdriver.common.by import By
      from selenium.webdriver.common.action_chains import ActionChains

      from selenium.common.exceptions import NoSuchElementException

      from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

      from selenium.webdriver.chrome.options import Options
      from selenium.webdriver.firefox.options import Options
    ```

## Browser Arguments

[Go Back to Summary](#summary)

-   `–headless`: To open browser in headless mode. Works in both Chrome and Firefox browser
-   `–start-maximized`: To start browser maximized to screen. Requires only for Chrome browser. Firefox by default starts maximized
-   `–incognito`: To open private chrome browser
-   `–disable-notifications`: To disable notifications, works Only in Chrome browser

    ```Python
      from selenium import webdriver
      from selenium.webdriver.chrome.options import Options

      options = Options()
      options.add_argument("--headless")
      options.add_argument("--start-maximized")
      options.add_argument("--disable-notifications")
      options.add_argument("--incognito")

      driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")

      # OR

      from selenium import webdriver
      from selenium.webdriver.chrome.options import Options

      options = Options()
      options.add_argument("--incognito","--start-maximized","--headless")
      driver = webdriver.Chrome(chrome_options=options, executable_path="Path to driver")
    ```

### Auto Download

[Go Back to Summary](#summary)

-   Chrome

    ```Python
      from selenium import webdriver

      options = webdriver.ChromeOptions()
      options.add_argument("download.default_directory=")

      driver = webdriver.Chrome(chrome_options=options, executable_path="Path to chrome driver")
    ```

-   Firefox

    ```Python
      from selenium import webdriver
      from selenium.webdriver.firefox.options import Options

      firefoxOptions = Options()
      firefoxOptions.set_preference("browser.download.folderList",2)
      firefoxOptions.set_preference("browser.download.manager.showWhenStarting", False)
      firefoxOptions.set_preference("browser.download.dir","/data")
      firefoxOptions.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")

      firefoxdriver = webdriver.Firefox(firefox_options=firefoxOptions, executable_path="Path to firefox driver")
    ```

-   We can add any MIME types in the list. MIME for few types of files are given below.

    1. Text File (.txt) – `text/plain`
    2. PDF File (.pdf) – `application/pdf`
    3. CSV File (.csv) – `text/csv` or `application/csv`
    4. MS Excel File (.xlsx) – `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` or `application/vnd.ms-excel`
    5. MS word File (.docx) – `application/vnd.openxmlformats-officedocument.wordprocessingml.document`
    6. Zip file (.zip) – `application/zip`

-   **Note:** The value of `browser.download.folderList` can be set to either `0`, `1`, or 2`.
    -   `0` – Files will be downloaded on the user’s desktop.
    -   `1` – Files will be downloaded in the Downloads folder.
    -   `2` – Files will be stored on the location specified for the most recent download

### Disable Notifications in FireFox

[Go Back to Summary](#summary)

```Python
  firefoxOptions.set_preference(“dom.webnotifications.serviceworker.enabled”, false);
  firefoxOptions.set_preference(“dom.webnotifications.enabled”, false);
```

### Open Specific Browser Using Binary

[Go Back to Summary](#summary)

-   Firefox

    ```Python
      from selenium import webdriver
      from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

      binary = FirefoxBinary('path/to/binary')
      driver = webdriver.Firefox(firefox_binary=binary)
    ```

-   Chrome

    ```Python
      from selenium import webdriver
      from selenium.webdriver.chrome.options import Options

      options = Options()
      options.binary_location = “”
      driver = webdriver.Chrome(chrome_options=options, executable_path=””)
      driver.get(‘http://google.com/’)
    ```

## Selenium Commands

### Read Browser Details

[Go Back to Summary](#summary)

```Python
  driver.title
  driver.window_handles
  driver.current_window_handles
  driver.current_url
  driver.page_source
```

### Go to a Specified URL

[Go Back to Summary](#summary)

```Python
  driver.get(“http://google.com”)
  driver.back()
  driver.forward()
  driver.refresh()
```

### Locating Elements

[Go Back to Summary](#summary)

-   `driver.find_element_by_<property>` – To find the first element matching the given locator argument. Returns a WebElement
-   `driver.find_elements_by_<property>` – To find all elements matching the given locator argument. Returns a list of WebElement

-   **By ID**

    ```Python
      <input id=”q” type=”text” />

      element = driver.find_element_by_id(“q”)
    ```

-   **By Name**

    ```Python
      <input id=”q” name=”search” type=”text” />

      element = driver.find_element_by_name(“search”)
    ```

-   **By Class Name**

    ```Python
      <div class=”username” style=”display: block;”>…</div>

      element = driver.find_element_by_class_name(“username”)
    ```

-   **By Tag Name**

    ```Python
      <div class=”username” style=”display: block;”>…</div>

      element = driver.find_element_by_tag_name(“div”)
    ```

-   **By Link Text**

    ```Python
      <a href=”#”>Refresh</a>

      element = driver.find_element_by_link_text(“Refresh”)
    ```

-   **By Partial Link Text**

    ```Python
      <a href=”#”>Refresh Here</a>

      element = driver.find_element_by_partial_link_text(“Refresh”)
    ```

-   **By XPath**

    ```Python
      <form id=”testform” action=”submit” method=”get”>

      Username: <input type=”text” />
      Password: <input type=”password” />

      </form>

      element = driver.find_element_by_xpath(“//form[@id=’testform’]/input[1]”)
    ```

-   **By CSS Selector**

    ```Python
      <form id=”testform” action=”submit” method=”get”>

      <input class=”username” type=”text” />
      <input class=”password” type=”password” />

      </form>

      element = driver.find_element_by_css_selector(“form#testform>input.username”)
    ```

#### Python Selenium Commands for Operation on Elements

[Go Back to Summary](#summary)

-   **button/link/image:**

        ```Python
          click()
          get_attribute()
          is_displayed()
          is_enabled()
        ```

-   **Text field:**

        ```Python
          send_keys()
          clear()
        ```

-   **Checkbox/Radio:**

    ```Python
      is_selected()
      click()
    ```

-   **Select:**

    -   Find out the select element using any element locating strategies and then select options from list using index, visible text or option value.

    ```Python
      select = Select(driver.find_element_by_id(""))

      select.select_by_index(1)
      select.select_by_value("") # pass value
      select.select_by_visible_text("") # pass visible text
    ```

-   **Element properties:**

    -   These methods return either `true` or `false`.

    ```Python
      is_displayed()
      is_selected()
      is_enabled()
    ```

-   **Read Attribute:**

    ```Python
      get_attribute(“”)
    ```

-   **Get attribute from a disabled text box**

    ```Python
      driver.find_element_by_id(“id”).get_attribute(“value”);
    ```

-   **Screenshot:**

    -   **Note:** An important note to store screenshots is that `save_screenshot(‘filename’)` and `get_screenshot_as_file(‘filename’)` will work only when extension of file is **.png**. Otherwise content of the screenshot can’t be viewed.
    -   Read articles for more details about taking [screenshot](http://allselenium.info/taking-screenshot-using-python-selenium-webdriver/) and element [screenshot](http://allselenium.info/capture-screenshot-element-using-python-selenium-webdriver/)

    ```Python
      from selenium import webdriver

      driver = webdriver.Firefox(executable_path='[Browser Driver Path]')
      driver.get('[URL to Open]')

      driver.get_screenshot_as_file('sample_screenshot_2.png')
      driver.save_screenshot('sample_screenshot_1.png')
    ```

### Waits

[Go Back to Summary](#summary)

-   [Waits](https://selenium-python.readthedocs.io/waits.html)
-   Selenium Webdriver provides two types of waits - implicit & explicit. An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution. An implicit wait makes WebDriver poll the DOM for a certain amount of time when trying to locate an element.

#### Expected Conditions

[Go Back to Summary](#summary)

-   There are some common conditions that are frequently of use when automating web browsers. Listed below are the names of each. Selenium Python binding provides some [convenience methods](http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions) so you don’t have to code an `expected_condition` class yourself or create your own utility package for them.

    ```Python
      title_is
      title_contains
      presence_of_element_located
      visibility_of_element_located
      visibility_of
      presence_of_all_elements_located
      text_to_be_present_in_element
      text_to_be_present_in_element_value
      frame_to_be_available_and_switch_to_it
      invisibility_of_element_located
      element_to_be_clickable
      staleness_of
      element_to_be_selected
      element_located_to_be_selected
      element_selection_state_to_be
      element_located_selection_state_to_be
      alert_is_present
    ```

    ```Python
      from selenium.webdriver.support import expected_conditions as EC

      wait = WebDriverWait(driver, 10)
      element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
    ```

#### Custom Wait Conditions

[Go Back to Summary](#summary)

-   You can also create custom wait conditions when none of the previous convenience methods fit your requirements. A custom wait condition can be created using a class with `__call__` method which returns `False` when the condition doesn’t match.

    ```Python
      class element_has_css_class(object):
        """An expectation for checking that an element has a particular css class.

          locator - used to find the element
          returns the WebElement once it has the particular css class
          """
          def __init__(self, locator, css_class):
            self.locator = locator
            self.css_class = css_class

          def __call__(self, driver):
            element = driver.find_element(*self.locator)   # Finding the referenced element
            if self.css_class in element.get_attribute("class"):
                return element
            else:
                return False

        # Wait until an element with id='myNewInput' has class 'myCSSClass'
        wait = WebDriverWait(driver, 10)
        element = wait.until(element_has_css_class((By.ID, 'myNewInput'), "myCSSClass"))
    ```

#### Explicit Waits

[Go Back to Summary](#summary)

-   An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait.

    ```Python
      from selenium import webdriver
      from selenium.webdriver.common.by import By
      from selenium.webdriver.support.ui import WebDriverWait
      from selenium.webdriver.support import expected_conditions as EC

      driver = webdriver.Firefox()
      driver.get("http://somedomain/url_that_delays_loading")
      try:
          element = WebDriverWait(driver, 10).until(
              EC.presence_of_element_located((By.ID, "myDynamicElement"))
          )
      finally:
          driver.quit()
    ```

    -   In the code above, Selenium will wait for a maximum of `10 seconds` for an element matching the given criteria to be found. If no element is found in that time, a TimeoutException is thrown. By default, WebDriverWait calls the ExpectedCondition every **500 milliseconds** until it returns success. ExpectedCondition will return true (Boolean) in case of success or not null if it fails to locate an element.

#### Implicit Waits

[Go Back to Summary](#summary)

-   An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. The default setting is 0 (zero). Once set, the implicit wait is set for the life of the WebDriver object.

    ```Python
      from selenium import webdriver

      driver = webdriver.Firefox()
      driver.implicitly_wait(10) # seconds
      driver.get("http://somedomain/url_that_delays_loading")
      myDynamicElement = driver.find_element_by_id("myDynamicElement")
    ```
