from pages.base_page import BasePage

class AddAPlayerForm(BasePage):
    add_a_player_expected_title = 'Add player'
    add_player_button_xpath = "//*[text()= 'ADD PLAYER']"
    add_a_player_page = ('https://scouts-test.futbolkolektyw.pl/en/players/add')

    def click_sign_in(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.add_a_player_page) == self.add_a_player_expected_title

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    def assert_title(self, url, add_a_player_expected_title):
        actual_title = self.get_page_title(url)
        self.assertEqual(add_a_player_expected_title, actual_title)