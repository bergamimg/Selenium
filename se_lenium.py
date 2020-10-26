from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import win32gui
from datetime import datetime, date
import os.path

## Define Path Driver
path_driver = r'C:\Users\Desktop\GitHub\4.Selenium\chromedriver_versao_86.exe'

## Define Path for storing files
path_files =r'C:\Users\Desktop\GitHub\4.Selenium'

## Define browser preferences
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('disable-popup-blockin')
options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension'])

## Start browser
chrome = webdriver.Chrome(options=options, executable_path=path_driver)
chrome.get('https://www.google.com.br')
time.sleep(2)

## Get the current date
def get_date():
    current_date = datetime.now().strftime('%d/%m/%Y')
    return current_date

google_search_bar = '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'
google_search_button = '//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]'

## Function to find the xpaths
def looking_for_xpath(path, key):
    try:
        time.sleep(1)
        the_element = WebDriverWait(chrome, 3).until(EC.element_to_be_clickable((By.XPATH, path)))
    except:
        print("\n Cant find the element \n")
        pass
    the_element.send_keys(key)
    time.sleep(1)

## Finding the google search bar and typing on it
looking_for_xpath(google_search_bar, get_date()+''' weather forecast''')

## Finding the google search button and pressing it
looking_for_xpath(google_search_button, (Keys.ENTER))

## Saving a screenshot from the result weather forecast in a directory
image_01 = pyautogui.screenshot(region=(0,0,1500,1000))
image_01.save(os.path.join(path_files,'my_screenshot_01.png'))

chrome.quit()
