import importlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyperclip
from selenium.webdriver.common.keys import Keys
import timeit
import traceback
import loginTest

itemDetails=["Apple","50","1000","fruits"]

def deleteItem(driver,itemDetails):
    time.sleep(5)
    itemTab=driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[2]/a/span[1]")
    itemTab.click()
    time.sleep(5)
    itemTab = driver.find_element_by_xpath("//*[@id='main-content']/section/a")
    itemTab.click()
    deleteButton=driver.find_elemetn_by_xpath("")
    time.sleep(5)
    itemSubm.click()


    pass


if (__name__=="__main__"):
    options = webdriver.ChromeOptions()
    # help to prevent close automatically
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        options=options, executable_path='chromedriver.exe')  # give chrome driver path
    driver.maximize_window()
    loginTest.login(driver)
    deleteItem(driver,itemDetails)

    pass
