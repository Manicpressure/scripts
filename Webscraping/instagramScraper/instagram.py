import os
import sys
import wget
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# Configure Chrome to disable notifications
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chromeOptions.add_experimental_option("prefs", prefs)

chromeService = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chromeService, options=chromeOptions)
driver.get('https://www.instagram.com')

username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# Use your own username and password for login
USERNAME = "user"
PASSWORD = "password"

username.clear()
username.send_keys(USERNAME)
password.clear()
password.send_keys(PASSWORD)

loginButton = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
loginButton.click()
time.sleep(5)

# Directly navigate to the hashtag search page
query = sys.argv[1]
driver.get(f"https://www.instagram.com/explore/tags/{query}")
time.sleep(5)

imageLinks = []
allImages = driver.find_elements(By.TAG_NAME, 'img')

for img in allImages:
    src = img.get_attribute('src')
    if src and src.startswith('https://scontent'):
        imageLinks.append(src)

driver.close()

# Save images to a directory named after the search query
directory = os.path.join(os.getcwd(), query)
os.makedirs(directory, exist_ok=True)

# Count existing files in the directory
counter = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

for links in imageLinks:
    saveAs = os.path.join(directory, f"{query}{counter}.jpg")
    wget.download(links, saveAs)
    counter += 1
