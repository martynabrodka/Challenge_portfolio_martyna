from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.settings import DEFAULT_LOCATOR_TYPE, EXPLICITLY_WAIT
import time

class AddAPlayerForm(BasePage):
    add_a_player_expected_title = "Add player"
    add_a_player_button_xpath = "//*[text()= 'Add player']"
    add_a_player_url = ('https://dareit.futbolkolektyw.pl/en/players/add')
    pop_up_inscription_required_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/p"
    expected_pop_up_inscription = "Required"
    add_a_player_page_title_xpath = "//header//h6"
    email_field_xpath = "//input[@name='email']"
    name_field_xpath = "//input[@name='name']"
    surname_field_xpath = "//input[@name='surname']"
    phone_field_xpath = "//input[@name='phone']"
    weight_field_xpath = "//input[@name='weight']"
    height_field_xpath = "//input[@name='height']"
    age_field_xpath = "//input[@name='age']"
    leg_dropdown_xpath = "//*[*id='mui-component-select-leg']"
    right_leg_choose_xpath = "//div[3]/ul/li[1]"
    left_leg_choose_xpath = "//div[3]/ul/li[2]"
    club_field_xpath = "//input[@name='club']"
    level_field_xpath = "//input[@name='level']"
    main_position_field_xpath = "//input[@name='mainPosition']"
    second_position_field_xpath = "//input[@name='secondPosition']"
    district_field_xpath = "//*[contains(@id,'select-district')]"
    district_xpath_map = {
        "Lower Silesia": "//li[1]",
        "Kuyavia-Pomerania": "//li[2]",
        "Lublin": "//li[3]",
        "Lubusz": "//li[4]",
        "Łódź": "//li[5]",
        "Lesser Poland": "//li[6]",
        "Masovia": "//li[7]",
        "Opole": "//li[8]",
        "Subcarpathia": "//li[9]",
        "Podlaskie": "//li[10]",
        "Pomerania": "//li[11]",
        "Solesia": "//li[12]",
        "Holy Cross Province": "//li[13]",
        "Warmia-Masuria": "//li[14]",
        "Greater Poland": "//li[15]",
        "West Pomerania": "//li[16]"

    }
    achievements_field_xpath = "//input[@name='achievements']"
    add_language_button_xpath = "//button[@aria-label='Add language']"
    ninety_minut_field_xpath = "//input[@name='webLaczy']"
    laczy_nas_pilka_field_xpath = "//input[@name='web90']"
    facebook_field_xpath = "//input[@name='webFB']"
    add_link_to_youtube_button_xpath = "//button[@aria-label='Add link to Youtube']"
    add_a_player_submit_button_xpath = "//button[@type='submit']"
    add_a_player_clear_button_xpath = "//button[@type='submit']//following-sibling::button"

    def click_add_a_player_button(self):
        self.click_on_the_element(self.add_a_player_button_xpath)
    def title_of_page(self):
        assert self.get_page_title(self.add_a_player_url) == self.add_a_player_expected_title
    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, add_a_player_expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(add_a_player_expected_title, actual_title)
    def click_submit_a_player(self):
        self.click_on_the_element(self.add_a_player_submit_button_xpath)

    def assert_required_name(self, add_a_player_url, expected_pop_up_inscription):
        actual_view = self.pop_up_inscription_required_xpath(add_a_player_url)
        self.assertEqual(expected_pop_up_inscription, actual_view)


    def wait_for_element_to_be_visible(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_visible((locator_type, locator)))
        time.sleep(3)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)
    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)