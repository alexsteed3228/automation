from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.expected_conditions import alert_is_present



browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/training-ground")
sel = browser.find_element(By.ID, 'sel1')
my_select = Select(sel)

