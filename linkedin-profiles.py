import time
import os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login = ""
password = ""

#start browser session
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#open linkedin in automated browser
driver.get("https://www.linkedin.com/")
time.sleep(2)

#logs you into Linkedin
driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input").send_keys(str(login))
password = driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input").send_keys(str(password))
driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div/form/div[2]/button").click()
print("successfully logged in")

#Loop through file that contains linkedin profile links
profiles = open("C:\Users\umut\Desktop\linkedin-profiles\profiles.txt", "r") 
for x in profiles:
    driver.get(x)
    time.sleep(2)
    try:
        elementt = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/button")
        driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[3]/div/div[2]/div/div/ul/li[2]/div").click()
        time.sleep(5)
    except:
        driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/div[4]/main/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div[2]/div/div/div/ul/div[1]/div[2]/div/div/button").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "/html/body/div[4]/div[5]/div/div[4]/main/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div[2]/div/div/div/ul/div[1]/div[2]/div/div/div/div/ul/li[4]/div").click()
        time.sleep(5)

    first = x.split("/in/",1)[1]
    last = first.split("/",1)[0]
    src = 'C:/Users/umut/Downloads/Profile.pdf'
    dst = 'C:/Users/umut/Downloads/{}.pdf'.format(last)
    os.rename(src, dst)
