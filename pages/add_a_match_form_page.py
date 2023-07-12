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