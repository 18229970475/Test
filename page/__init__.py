#!/usr/bin/python       
# -*- coding:UTF-8 -*-
from time import sleep

from selenium import webdriver
class Login:
    def login(self, username, password):
        driver = webdriver.Firefox()
        driver.get("http://121.40.208.200:44888/#/login")
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_xpath("//button[@class='el-button el-button--primary']").click()
        sleep(3)
        driver.quit()

login = Login()
login.login("admin", "6234567")
login.login("admin", "123456")