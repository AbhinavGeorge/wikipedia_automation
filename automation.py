from selenium import webdriver
import time

inp = input("what do you want to know about?\n")

driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org/')


searchbox = driver.find_element_by_xpath('//*[@id="searchInput"]')
searchbox.send_keys(inp)

searchbutton = driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
searchbutton.click()
