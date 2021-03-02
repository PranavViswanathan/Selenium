from selenium import webdriver
import time
PATH = "C:\Program Files (x86)\chromedriver.exe" # Location of the webdriver file

driver = webdriver.Chrome(PATH)
driver.get("https://pranavcoder.netlify.app/")

driver.close() # Closes the tab
#driver.quit() # Closes chrome
