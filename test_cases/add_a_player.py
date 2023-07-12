import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.add_a_player_page import AddAPlayerForm
#from pages.base_page import BasePage
import time

class TestAddAPlayerPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user10@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in()
        time.sleep(5)

    def test_add_a_player_page(self):
        add_a_player_page = AddAPlayerForm(self.driver)
        add_a_player_page.title_of_page()
        time.sleep(5)

    def test_check_title(self):
        actual_title = self.get_page_title('https://scouts-test.futbolkolektyw.pl/en/players/add')
        add_a_player_expected_title = 'Add player'
        assert actual_title == add_a_player_expected_title
    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")