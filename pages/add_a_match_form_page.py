from pages.base_page import BasePage

class Add_a_match_form(BasePage):
    adding_match_player_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[1]/div/span"
    my_team_input_xpath = "//*[contains(@class, 'MuiInputBase-input')]"
    enemy_team_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input"
    my_team_score_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input"
    enemy_team_score_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input"
    date_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[5]/div/div/input"
    match_at_home_button_xpath = "//*[contains(@class, 'jss45')]"
    match_out_home_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[6]/fieldset/div/label[2]/span[1]/span[1]/input"
    t_shirt_color_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div/input"
    league_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[8]/div/div/input"
    time_played_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    number_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[10]/div/div/input"
    web_match_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[11]/div/div/input"
    general_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[12]/div/div/input"
    rating_input_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[2]/div/div[13]/div/div/input"
    submit_button_xpath = "//*[contains(@class, 'MuiButton-label')]"
    clear_button_xpath = "//*[@id='__next']/div[1]/main/div[2]/form/div[3]/button[2]/span[1]"
    pass