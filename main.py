from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/trial-of-the-stones')

def FindEl(value):
    element_found = browser.find_element(By.XPATH, str(value))
    return element_found


locator_inputF1 = FindEl('//div/input[@id="r1Input"]')
locator_button_1 = FindEl('//div/button[@name="r1Btn"]')
locator_inputF2 = FindEl("//*[contains(@name, 'r2I')]")
locator_button_2 = FindEl("//*[contains(@name, 'r2B')]")
locator_wealth_1 = FindEl("//div/span/b[text()='Jessica']/../..//p")
locator_wealth_2 = FindEl("//div/span/b[text()='Bernard']/../..//p")
locator_inputF3 = FindEl("//*[contains(@name, 'r3I')]")
locator_button_3 = FindEl("//*[contains(@name, 'r3B')]")
locator_button_4 = FindEl("//button[@name='checkButn']")

locator_inputF1.send_keys('rock')
locator_button_1.click()

locator_first_answer = FindEl("//div[@id='passwordBanner']/h4")
locator_inputF2.send_keys(locator_first_answer.text)
locator_button_2.click()

a, b = int(locator_wealth_1.text), int(locator_wealth_2.text)
if a > b:
    locator_inputF3.send_keys('Jessica')
else:
    locator_inputF3.send_keys('Bernard')
locator_button_3.click()
locator_button_4.click()
