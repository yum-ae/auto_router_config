from selenium import webdriver
import time
import selenium


#Firefoxを操作
driver = webdriver.Firefox()
driver.set_page_load_timeout(5)


driver.get("http://name:pw@192.168.2.1/wan_lan01_2.html")

print(driver.find_element_by_css_selector("div#mainInner").text)

