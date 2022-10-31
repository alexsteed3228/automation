from selenium import webdriver
from selenium.webdriver.common.by import By

from BaseElement import BaseElement
from BasePage import BasePage
from locator import Locator


class TrainingGroundPage(BasePage):

    url = 'http://techstepacademy.com/training-ground/'


    @property
    def button1(self):
        locator = Locator(by=By.ID, value='b1')
        return BaseElement(driver=self.driver,
                           locator=locator
                           )


