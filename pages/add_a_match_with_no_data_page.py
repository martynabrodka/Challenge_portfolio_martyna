from pages.base_page import BasePage

class AddAMatchForm(BasePage):
    adding_match_player_title_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"
    my_team_input_xpath = "//*[@name='myTeam']"
    enemy_team_input_xpath = "//*[@name='enemyTeam']"
    my_team_score_input_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_input_xpath = "//*[@name='enemyTeamScore']"
    date_input_xpath = "//*[@name='date']"
    match_at_home_button_xpath = "//*[contains(@class, 'jss45')]"
    match_out_home_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[1]/span[1]/input"
    tshirt_color_input_xpath = "//*[@name='tshirt']"
    league_input_xpath = "//*[@name='league']"
    time_played_input_xpath = "//*[@name='timePlayed']"
    number_input_xpath = "//*[@name='number']"
    web_match_input_xpath = "//*[@name='webMatch']"
    general_input_xpath = "//*[@name='general']"
    rating_input_xpath = "//*[@name='rating']"
    submit_button_xpath = "//*[contains(@class, 'MuiButton-label')]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    pass
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

#inne:
# add_a_player_page.element_to_be_visible("//button[@type='submit']")