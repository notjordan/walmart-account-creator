from selenium import webdriver
import os
import time
import logging
from colorama import Fore
from colorama import Style
from datetime import datetime
from pprint import pprint
import colorama
import inquirer

#Headless Stuff
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
options.add_argument('log-level=2')
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

#Logging Config
logging.basicConfig(format='%(asctime)s %(message)s')
startTime = time.time()

#Creating The Account
driver.get('https://www.walmart.com/account/signup?tid=0&returnUrl=%2F')
logging.warning(Fore.BLUE + Style.BRIGHT + "Loading Walmart.com" + Style.RESET_ALL)
time.sleep(1)
name = driver.find_element_by_id("first-name-su")
name.send_keys("NAME HERE")
logging.warning(Fore.BLUE + Style.BRIGHT + "Sending name" + Style.RESET_ALL)
lastname = driver.find_element_by_id("last-name-su")
lastname.send_keys("LAST NAME HERE")
email1 = driver.find_element_by_id("email-su")
email1.send_keys("EMAIL HERE")
logging.warning(Fore.BLUE + Style.BRIGHT + "Sending email" + Style.RESET_ALL)
password = driver.find_element_by_id("password-su")
password.send_keys("PASSWORD HERE")
logging.warning(Fore.BLUE + Style.BRIGHT + "Sending password" + Style.RESET_ALL)
time.sleep(.5)
driver.find_element_by_xpath("""//*[@id="sign-up-form"]/button[1]""").click()
logging.warning(Fore.GREEN + Style.BRIGHT + "Creating account " + Style.RESET_ALL)

#Time Stamp
print(Fore.BLUE + Style.BRIGHT + "" + Style.RESET_ALL)
executionTime = (time.time() - startTime)
try:
  print(' Account made in - ' + str(executionTime))
except:
  print("Could Not Post Time")


#Completion  Sound.
from playsound import playsound
playsound ('sound.mp3')
