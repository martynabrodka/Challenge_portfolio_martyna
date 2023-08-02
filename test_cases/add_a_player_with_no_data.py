import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT, DEFAULT_LOCATOR_TYPE
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.add_a_player_page import AddAPlayerForm
from pages.dashboard import Dashboard
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
#from pages.base_page import BasePage
import time
from selenium.webdriver.common.by import By

class TestAddAPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://dareit.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user10@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in()
        time.sleep(5)

    #def test_add_a_player_with_no_data(self):
     #   add_a_player_page = AddAPlayerForm(self.driver)
      #  add_a_player_submit_button_xpath = self.driver.find_element(By.XPATH, "//button[@type='submit']").text
       # self.driver.execute_script("arguments[0].scrollIntoView()", add_a_player_submit_button_xpath)
        #add_a_player_page.click_submit_a_player()
        #time.sleep(5)

    def test_add_a_player_with_age_above_100(self):
        add_a_player_page = AddAPlayerForm(self.driver)
        time.sleep(3)
        add_a_player_page.get_page_title(add_a_player_page.add_a_player_url)
        time.sleep(3)
        add_a_player_page.type_in_age('20-07-1890')
        time.sleep(3)
        print('test_add_a_player_with_age_above_100 - not ok, check the Bug')



    def test_check_title(self):
        actual_title = self.get_page_title('https://dareit.futbolkolektyw.pl/en/players/add')
        add_a_player_expected_title = 'Add player'
        assert actual_title == add_a_player_expected_title
    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title




    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")