# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 20:14:34 2023

@author: Jagadeesh Damarla
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import pandas as pd
import os
import datetime
import time



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# ytLink = "https://youtu.be/XmzBhBXbYsg"

#Path to Links file along with file name
linksList = pd.read_csv("D:\WebScrapping\Links.csv")

#Copy the downloads folder below
downloadsFolder = r"C:\Users\DELL\Downloads"

for link in list(linksList["Playlist_Links"]) :
    print("Processing for the link {}".format(link))

    try:
        #opening the ss youtube
        driver.get("https://ssyoutube.com/")

        #waiting for page to load in seconds
        pageDelay = 10
        downloadButton = WebDriverWait(driver, pageDelay).until(EC.presence_of_element_located((By.ID, 'search')))
        print(downloadButton)
        urlTextBox = driver.find_element(By.ID, 'id_url')
        urlTextBox.clear()
        urlTextBox.send_keys(link)
        downloadButton.send_keys(Keys.ENTER)
        # WebDriverWait(driver, pageDelay).until(EC.presence_of_element_located((By.ID, 'myTabContent')))
        time.sleep(10)
        resultsDiv =  driver.find_elements(By.ID , "myTabContent")
        downloadTable = driver.find_elements(By.TAG_NAME, "td")
        #selects the download option for the first option available
    
        downloadTable[1].click()
        time.sleep(10)
        # driver.execute_script("window.open('');")
        cd = driver.window_handles
        # a pop up opens when we click on the download and hence closing it
        driver.switch_to.window(cd[1])
        driver.close()
        time.sleep(10)
        driver.switch_to.window(cd[0])
        
        # I purposefully am not closing the chrome window, this is because the forced closure of chrome 
        # will stop downloads
        # There may be many pop ups, donot click on any of them
        
        
        
    except Exception as e:
        print("Waited for 10 seconds and the page load failed. Please check if the website is available or re-run the code with increased delay")
        print("Exception occured is :"+str(e))

    
