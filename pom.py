from selenium import webdriver

from TraingGround import TrainingGroundPage
from trial_page import TrialPage

"""trial of the stones testing"""
browser = webdriver.Chrome()
stone_text = 'rock'

trial_page = TrialPage(driver=browser)
trial_page.go()

trial_page.stone_input.input_text(stone_text)
trial_page.stone_button.click()

password_text = trial_page.stone_answer.attribute('textContent') #ищем аттрибут в html где находится этот текст
assert password_text == 'bamboo', 'Failed'
trial_page.secret_input.input_text(password_text)
trial_page.secret_button.click()

wealth_1 = int(trial_page.jessica_wealth.attribute('textContent'))
wealth_2 = int(trial_page.bernard_wealth.attribute('textContent'))

if wealth_1 > wealth_2:
    trial_page.merchants_input.input_text('Jessica')
else:
    trial_page.merchants_input.input_text('Bernard')

trial_page.merchants_button.click()
trial_page.check_answer_button.click()