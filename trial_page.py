from selenium.webdriver.common.by import By

from BaseElement import BaseElement

from BasePage import BasePage

from locator import Locator


class TrialPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    @property
    def stone_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r1Input')
        return BaseElement(self.driver, locator=locator)

    @property
    def stone_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r1Btn')
        return BaseElement(self.driver, locator=locator)

    @property
    def secret_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r2Input')
        return BaseElement(self.driver, locator=locator)

    @property
    def secret_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r2Butn')
        return BaseElement(self.driver, locator=locator)

    @property
    def stone_answer(self):
        locator = Locator(By.XPATH, "//div[@id='passwordBanner']/h4")
        return BaseElement(self.driver, locator=locator)

    @property
    def jessica_wealth(self):
        locator = Locator(By.XPATH, "//b[text()='Jessica']/../..//p")
        return BaseElement(self.driver, locator=locator)

    @property
    def bernard_wealth(self):
        locator = Locator(By.XPATH, "//b[text()='Bernard']/../..//p")
        return BaseElement(self.driver, locator=locator)

    @property
    def merchants_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r3Input')
        return BaseElement(self.driver, locator=locator)

    @property
    def merchants_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r3Butn')
        return BaseElement(self.driver, locator=locator)

    @property
    def check_answer_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#checkButn')
        return BaseElement(self.driver, locator=locator)
