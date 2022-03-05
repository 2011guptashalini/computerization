'''This is the class which is the main class'''
import time
import os
from os.path                                    import realpath, dirname

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.json_helper                      import LoadJson, GetJsonValue

import frontend.frontend

CURRENT_DIR = dirname(realpath(__file__))

caps_web_browser =[{
            'os_version': '10',
            'os': 'Windows',
            'browser': 'chrome',
            'browser_version': 'latest',
            'name': 'Parallel Test1', # test name
            'build': 'browserstack-build-1' # Your tests will be organized within this build
        },
        {
            'os_version': '10',
            'os': 'Windows',
            'browser': 'firefox',
            'browser_version': 'latest',
            'name': 'Parallel Test2',
            'build': 'browserstack-build-1'
        },
        {
            'os_version': 'Big Sur',
            'os': 'OS X',
            'browser': 'safari',
            'browser_version': 'latest',
            'name': 'Parallel Test3',
            'build': 'browserstack-build-1'
        }
        ]

caps_mobile_browser =[{
        'realMobile': 'true',
        'browserName': 'ios',
        'device': 'iPhone 13 Pro Max',
        'os_version': '15',
        'name': 'Parallel Test1', # test name
        'build': 'browserstack-build-1' # Your tests will be organized within this build
        },
        {
        'realMobile': 'true',
        'browserName': 'android',
        'device': 'Samsung Galaxy S21 Ultra',
        'os_version': '11.0',
        'name': 'Parallel Test2',
        'build': 'browserstack-build-1'
        },
        {
        'realMobile': 'true',
        'browserName': 'ios',
        'device': 'iPad Air 4',
        'os_version': '14',
        'name': 'Parallel Test3',
        'build': 'browserstack-build-1'
        }
]

caps_native_app = {
    # Set your access credentials
    "browserstack.user" : "shalini148",
    "browserstack.key" : "gzfKAzry62i8V9eA8Fdf",
  
    # Set URL of the application under test
    "app" : "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
  
    # Specify device and os_version for testing
    "device" : "Google Pixel 3",
    "os_version" : "9.0",
      
    # Set other BrowserStack capabilities
    "project" : "First Python project", 
    "build" : "browserstack-build-1",
    "name" : "first_test"
}


class LocateBy:
    ''' A class allowing easier reference to a locate by method when selecting ways to interact with an element '''
    ID = 'id'
    CLASSNAME = 'class name'
    XPATH = 'xpath'
    CSS_SELECTOR = 'css selector'
    TAG_NAME = 'tag name'
    LINK_TEXT = 'link text'

class Locators:
    ''' This class is used to control, read and provide access to the locators provided in a json file. The json file must follow a particular
        structure for it to be compatible with this locator class. You can see an example json file already in the directory /driver/locators '''
    def __init__(self, locator_file_name, project_name):
        self.locator_file = f'{CURRENT_DIR}\\applications\\{project_name}\\{locator_file_name}.json'
        self.locators = LoadJson.using_filepath(self.locator_file)

    def get_locator(self, locator_name):
        ''' Pass in the name of the locator. This method returns 2 values, the 1st is the locator type (xpath, id, classname) and the
            2nd is the actual locator locator/value '''
        locator = self.locators.get(locator_name)
        if locator is None:
            raise Exception('locator not found!')

        locator_type = locator.get('type')
        locator_value = locator.get('value')
        return locator_type, locator_value

    def get_locator_type(self, locator_name):
        ''' Pass in the locators name and get returned the type of locator it is. '''
        return self.get_locator(locator_name)[0]

    def get_locator_value(self, locator_name):
        ''' Pass in the locators name and get returned the type of locator it is. '''
        return self.get_locator(locator_name)[1]


'''If user selects Locally from the front end'''
class DriverFactoryLocal:
    def open_local_browser(self, browser):
        if frontend.frontend.chrome_cb == 'CHECKED'
            driver = webdriver.Chrome(ChromeDriverManager().install())
        
        if frontend.frontend.firefox_cb == 'CHECKED'
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        
        if frontend.frontend.edge_cb == 'CHECKED'
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())


'''If user selects Browser Stack from the front end'''
class DriverFactoryBS:
    def __init__(self, user_name, password, app_url):
        self.user_name = frontend.frontend.bs_user_name_text
        self.password = frontend.frontend.bs_access_key_text
        self.app_url = frontend.frontend.bs_native_url_text
        self.command_executor = 'https://{user_name}:{password}@hub-cloud.browserstack.com/wd/hub'


    def open_web_bs_browser(self, browser):
        driver = webdriver.Remote(
        command_executor='https://{user_name}:{password}@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=caps_web_browser)
    

    def open_mobile_browser(self, browser):
        driver = webdriver.Remote(
        command_executor='https://shalini_ItaWko:q5c84xV3V9yawZx9giq9@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=caps_mobile_browser)

    def open_mobile_native(self):
        pass
    



if frontend.frontend.web_site_rb == 'SELECTED' && frontend.frontend.locally_rb == 'SELECTED':
    DriverFactoryLocal.open_local_browser()

if frontend.frontend.web_site_rb == 'SELECTED' && frontend.frontend.browser_stack_rb == 'SELECTED':
    DriverFactoryBS.open_web_bs_browser()

if frontend.frontend.mobile_site_rb == 'SELECTED':
    DriverFactoryBS.open_mobile_bs_browser()

if frontend.frontend.mobile_native_rb == 'SELECTED':
    DriverFactoryBS.open_mobile_native()
