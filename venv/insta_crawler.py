from selenium import webdriver
import time
import urllib.request
from selenium.webdriver.common.keys import Keys
from bs4 import *
import request

UserID = "01096458519"
UserPW = "skek8641!@#"
UserName = "regular.lee"

path = "chromedriver.exe"
driver=webdriver.Chrome(path)
driver.implicitly_wait(3)

driver.get('https://instagram.com')
'''
driver.find_element_by_id("id명")
driver.find_element_by_xpath("경로")
driver.find_element_by_css_selector("경로")
driver.find_element_by_xpath("").click()
'''
driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(UserID)
driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(UserPW)
driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[4]").click()

driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a/img").click()
driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()

SCROLL_PAUSE_TIME = 3

#스크롤 내리기 수정필요
while True:
    last_height = driver.execute_script("return document.body.scrollHeight")

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        else:
            last_height = new_height
            continue

