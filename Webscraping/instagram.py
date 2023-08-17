# 2023-08-13 update
# added comments for clarification
# updated code to work on latest version of instagram as of 2023-08-13
# note: meta has changed the desktop version of instagram
# hashtag search now only show the top 9 posts, effectively neutering this script

# !!! How to use command: !!!
# python3 instagram.py searchQuery (n)
# do not include hashtag in search query
# n is the number of times to scroll down the page, do not use as of 2023-08-13

# Required packages
# pip install webdriver-manager
# pip install wget
# pip install selenium
# pip install time
# webdriver-manager will try to use the latest version of chrome, and if the version of chrome installed on your computer is not up to date,
# the webdriver module will crash. 

# IMPORT LIBRARIES
from selenium import webdriver # webdriver to manipulate a user agent
from selenium.webdriver.common.keys import Keys # Keys to type
from selenium.webdriver.support import expected_conditions as EC # EC to form conditionals
from selenium.webdriver.common.by import By # By to select elements off the page
from selenium.webdriver.support.wait import WebDriverWait # WebDriverWait to timeout the user agent 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service as ChromeService

import os # os to manipulate OS commands
import sys # sys for taking in arguments
import wget # wget to download images
import time # time to incorporate sleeping time

# LOGGING IN
# configure chrome to disable notifications
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chromeOptions.add_experimental_option("prefs",prefs)

# create a Service object for ChromeDriver
chromeService = ChromeService(ChromeDriverManager().install())
# use the Service object to initialize the Chrome driver
driver = webdriver.Chrome(service=chromeService, options=chromeOptions)
driver.get('https://www.instagram.com') # navigate to the URL

# select the username element in the variable 'username'
# make a conditional, if it takes longer than 10 seconds, the script will time out (WebDriverWaiter(driver,10))
# the conditional (EC.element_to_be_clickable) will force UA to wait until the element is clickable
# By. will use the css selector to find the html element 
# in this case the unique html element is identified by input class with name='username'
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

# the text boxes needs to be cleared before typing or the text may append to the prefilled text
# improvement - save username/password in file and read credentials from there for security reasons
# login is required to access instagram photos
username.clear()
username.send_keys("user")
password.clear()
password.send_keys("password")

# click on log in button identified by unique html element
loginButton = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
loginButton.click()
time.sleep(5)

# The below section can be skipped because we can manipulate the url to search a query
#############################################
# everytime you log in there is a popup which needs to be dispelled
# this is a javascript popup so it is difficult to find a css element which can be uniquely identifiable
# therefore, need to use xpath
# 'Not Now' is selected because it is a unique string within the page 
#try:
#	loginInfoPopup = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Not Now")]')))
#	loginInfoPopup.click()
#except:
#	pass
	
# after first popup is dispelled, another popup will pop when the page loads
#try:
#	notificationsPopup = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Not Now")]')))
#	notificationsPopup.click()
#except:
#	pass
#############################################

# search query
# use the URL to directly navigate to the search results page
# take search query from python command
query=sys.argv[1]
driver.get("https://www.instagram.com/explore/tags/"+query)
time.sleep(5)


# the below section can be skipped because hashtag searching only returns the top 9 posts - there is no more scrolling
#############################################
# scroll down the screen however many times you set during the command
#scrollScreens = int(sys.argv[2])
#for n in range(scrollScreens):
#	driver.execute_script(("window.scrollTo(0,document.body.scrollHeight);"))
#	time.sleep(3)
#############################################


imageLinks = [] #initialize a list to store image links in
# find all img elements on page
allImages = driver.find_elements(By.TAG_NAME, 'img')
# iterate through each 'img' tag and extract the src tag contents. 
for img in allImages:
	src = img.get_attribute('src')
	if src and src.startswith('https://scontent'): # make sure src exists first, if true, it needs to start with that url to be a valid image source
		imageLinks.append(src) #add image link to list 

driver.close() # close driver at the end

# Save images to computer 
directory = os.path.join(os.getcwd(), query) # save it in current directory+searchQuery
os.makedirs(directory, exist_ok=True) # make the directory if it doesnt exist

# Instead of starting from 0, count files in the directory and start from there - just in case we run the same search query multiple times
counter = len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])

for links in imageLinks:
	saveAs = os.path.join(directory, query + str(counter) + '.jpg') # the directory to which the downloaded images will be saved to
	wget.download(links, saveAs) # download images
	counter += 1

# Reference
# 2023-08-13 current coding on the tags page is as follows so it should still work:
# <img alt="Photo by Lawson the Shiba on August 12, 2023. May be an image of fox and pet." crossorigin="anonymous" src="https://scontent-akl1-1.cdninstagram.com/v/t51.2885-15/366449285_837282910896016_3801095076464177810_n.webp?stp=dst-jpg_e35&amp;_nc_ht=scontent-akl1-1.cdninstagram.com&amp;_nc_cat=104&amp;_nc_ohc=Q0DOrL7RkNYAX84QFbP&amp;edm=AGyKU4gBAAAA&amp;ccb=7-5&amp;ig_cache_key=MzE2ODI3NjMzNzMxMTc3NzYxNw%3D%3D.2-ccb7-5&amp;oh=00_AfDZcPITgLaP1-4Zp5UJ_21r6RCWkp8w3YKoM8I5JLWAAg&amp;oe=64DD52B9&amp;_nc_sid=2011ad" class="x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3" style="object-fit: cover;">




