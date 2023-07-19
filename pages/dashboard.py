from pages.base_page import BasePage
import time

class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/'
    scouts_panel_paragraph_xpath = "//h6"
    main_page_button_xpath = "//*[contains(@class, 'MuiTypography-root MuiListItemText-primary')]"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    polski_button_xpath = "//*[text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    ilosc_graczy_table_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[1]/div/div[1]"
    ilosc_meczy_table_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[2]/div/div[1]"
    ilosc_raportow_table_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[3]/div/div[1]"
    ilosc_akcji_table_xpath = "//*[@id='__next']/div[1]/main/div[2]/div[4]/div/div[1]"
    logo_scouts_panel_xpath = "//*[contains(@class, 'MuiCardMedia-root jss130')]"
    scouts_panel_subheading_xpath = "//h2"
    panel_information_xpath = "//*[contains(@class, 'MuiTypography-colorTextSecondary')]"
    contact_button_xpath = "//*[contains(@class, 'MuiButton-label')]"
    linki_pomocnicze_subheading_xpath = "//*[text()='Linki pomocnicze']"
    add_a_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    aktywnosc_subheading_xpath = "//*[text()='Aktywnosć']"
    ostatnio_stworzony_gracz_subtitle_xpath = "//*[contains(@class, 'MuiTypography-subtitle1')]"
    ostatnio_stworzony_gracz_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    ostatnio_zaaktualizowany_gracz_subtitle_xpath = "//*[text()='Ostatnio zaaktualizowany gracz']"
    ostatnio_zaaktualizowany_gracz_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1"
    ostatnio_stworzony_mecz_subtitle_xpath = "//*[text()='Ostatnio stworzony mecz']"
    ostatnio_stworzony_mecz_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
    ostatnio_zaaktualizowany_mecz_subtitle_xpath = "//*[text()='Ostatnio zaaktualizowany mecz']"
    ostatanio_zaaktualizowany_mecz_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[4]/button/span[1]"
    ostatnio_zaaktualizowany_raport_subtitle_xpath = "//*[text()='Ostatnio zaaktualizowany raport']"
    ostatnio_zaaktualizowany_raport_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1]"

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_sign_out(self):
        self.click_on_the_element(self.sign_out_button_xpath)
