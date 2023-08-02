import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
from pages.add_a_player_page import AddAPlayerForm
from pages.dashboard import Dashboard
from selenium.webdriver.support import expected_conditions as EC
#from pages.base_page import BasePage
import time
from utils.settings import DEFAULT_LOCATOR_TYPE, EXPLICITLY_WAIT

class TestAddAPlayerPage(unittest.TestCase):
    add_a_player_xpath = "//*[text()='Add player']"

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

    def test_add_a_player_with_age_above_100(self):
        add_a_player_page = AddAPlayerForm(self.driver)
        time.sleep(3)
        add_a_player_page.get_page_title(add_a_player_page.add_a_player_url)
        time.sleep(3)
        add_a_player_page.type_in_name('Lemon') #fulfilling required fields
        add_a_player_page.type_in_surname('Smith') #fulfilling required fields
        add_a_player_page.type_in_main_position('goalkeeper') #fulfilling required fields
        add_a_player_page.type_in_age('20-07-1890') #fulfilling required fields
        time.sleep(3)
        print('test_add_a_player_with_age_above_100 - not ok, check the Bug')

    def test_add_a_player_without_mandatory_fields(self):
        add_a_player_page = AddAPlayerForm(self.driver)
        time.sleep(3)
        add_a_player_page.get_page_title(add_a_player_page.add_a_player_url)
        add_a_player_page.click_submit_a_player()
        time.sleep(3)
        print('test_add_a_player_without_mandatory_fields - not ok, check the Bug')

    def test_add_a_player_page(self):
        add_a_player_page = AddAPlayerForm(self.driver)
        add_a_player_page.title_of_page()
        time.sleep(5)

    def test_check_title(self):
        actual_title = self.get_page_title('https://dareit.futbolkolektyw.pl/en/players/add')
        add_a_player_expected_title = 'Add player'
        assert actual_title == add_a_player_expected_title
    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(expected_title, actual_title)

    def wait_for_element_to_be_visible(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_visible((locator_type, locator)))
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")