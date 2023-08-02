# challenge2_automat_portfolio_martyna_brodka

#   Task 1: Konfiguracja oprogramowania
  ## Subtask 1: Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT Challenge?
    
  Witam, mam na imię Martyna. Niedawno zakończyłam swoje pierwsze wyzwanie z Dare IT - Zostań testerem manualnym. Jako, że dużo wyniosłam z tego kursu, naturalną koleją rzeczy było dla mnie kontynuowanie nauki, tym razem w testowaniu automatycznym z Pythonem. Moim celem jest rozpoczęcie swojej pierwszej pracy w testowaniu oprogramowania. Mam nadzieję, że realizacja tego wyzwania przybliży mnie do niego w możliwie najkrótszym czasie 😃💪🍀
 
#   Task 2: Selektory
  ## Subtask 2: Wypisz wszystkie elementy znajdujące się na stronie https://scouts-test.futbolkolektyw.pl/pl/login oraz wymień do nich po 3 selektory

  👉 **Przypomnij_hasło_hyperlink_xpath**

    1️⃣ //*[@id="__next"]/form/div/div[1]/a

    2️⃣ //*[text()="Przypomnij hasło"]

    3️⃣ //child::div/a

  👉 **Scouts_Panel_heading_xpath**

    1️⃣ //*[@id="__next"]/form/div/div[1]/h5

    2️⃣ //*[text()="Scouts Panel"]

    3️⃣ //*[contains(@class, "MuiTypography-root MuiTypography-h5")]

  👉 **Login_input_xpath**
  
    1️⃣ //*[@id="login"]
    
    2️⃣ //*[text()="Login"]
  
    3️⃣ //*[contains(@class, "MuiInputBase-root MuiInput")]
  
  👉 **Hasło_input_xpath**
  
    1️⃣ //*[@id="password"]
  
    2️⃣ //*[text()="Hasło"]
  
    3️⃣ //*[@name="password"]
    
  👉 **Polski_button_xpath**
    
    1️⃣ //*[@id="__next"]/form/div/div[2]/div/div
    
    2️⃣ //*[contains(@class, "MuiSelect-root MuiSelect-select")]
    
    3️⃣ //*[text()="Polski"]
    
  👉 **Zaloguj_button_xpath**
  
    1️⃣ //*[@id="__next"]/form/div/div[2]/button/span[1]
    
    2️⃣ //*[contains(@class, "MuiButton-label")]
    
    3️⃣ //*[text()="Zaloguj"]

  ## Subtask 3: Dodawanie selektorów do projektu

  👉 [plik login_page.py](https://drive.google.com/file/d/1LdHD33bwBfDnl-icLolzI86fMZ1Fsd4X/view?usp=drive_link)

  ## Subtask 4: Dodanie nowego pliku

  👉 [plik dashboard.py](https://drive.google.com/file/d/1tDkzutJBS2_RLWI9kK62CHAgS8866uyC/view?usp=drive_link)

  ## Subtask 5: Dodanie nowego pliku - add a match form

  👉 [plik add_a_match_form.py](https://drive.google.com/file/d/1fj1m4UDF-zc7bhKhusjsF1CNXRSsBaEk/view?usp=drive_link)
  
#   Task 3: Pierwszy test automatyczny i asserty
  ## Subtask 1: Uzupełnienie strony logowania
  👉 [plik login_page.py](https://drive.google.com/file/d/1YsZQIgspEi9A_g12IoZoAxMX-pPHO92G/view?usp=drive_link)

  ## Subtask 2: Nowy przypadek testowy
  👉 [plik log_in_to_the_system.py](https://drive.google.com/file/d/1-cMOA0qvtX-Kohymr02NUTfIRI7BeuBU/view?usp=drive_link)

  ## Subtask 3: Assert
  👉 [plik check_title_dashboard.py](https://drive.google.com/file/d/1LgKx9BddTuu7BZD5y3O4NSQ-JU_u8d-V/view?usp=drive_link)

  ## Subtask 4: Assert na stronie 'Add player'
  👉 [plik add_a_player.py](https://drive.google.com/file/d/19wgaOylHJ8IcayoP9S7MaOj98Dkn50yI/view?usp=drive_link)

  ## Subtask 5: Zadanie dodatkowe
  👉 [plik base_page.py](https://drive.google.com/file/d/1bXMHzbUKitCoqiAXjdz7jwLHcNA-rd27/view?usp=drive_link)

#   Task 4: Refactor, debbuger i przypadki testowe
  ## Subtask 1: Pisanie przypadków testowych
  👉 [Moje przypadki testowe](https://docs.google.com/spreadsheets/d/1oCMoi-DnKfkXnT81NxHQOofQZwvXlf0uxOOeNOGXsws/edit?usp=drive_link)

  ## Subtask 2: Pisanie kodu na podstawie przypadków testowych
  👉 Moje testy:
  
  [test_add_a_player_with_age_above_100 || test_add_a_player_without_mandatory_fields](https://github.com/martynabrodka/challenge2_automat_portfolio_martyna/blob/main/test_cases/add_a_player.py)

  [test_log_in_with_wrong_password || test_sign_out_of_the_system](https://github.com/martynabrodka/challenge2_automat_portfolio_martyna/blob/main/test_cases/log_in_to_the_system.py)

  [test_change_language](https://github.com/martynabrodka/challenge2_automat_portfolio_martyna/blob/main/test_cases/check_title_dashboard.py)

  ## Subtask 3: Dodanie nagrań z uruchomionych testów na dysku google
  👉 [Nagranie z testów 1-4](https://drive.google.com/file/d/1ehrMYM4nZ5nJTS4R3tR21oAsKGPWIshN/view?usp=drive_link)

  👉 [Nagranie z testu 5](https://drive.google.com/file/d/1ULI6hPqih2wDB8_kKl2SlBw3iCJCeBSt/view?usp=drive_link)

#   Task 5: Robot Framework
  ## Subtask 1: Przepisanie testów z zadania 4 na Robot Framework

  👉 [My test cases in Robot Framework](https://github.com/martynabrodka/test_robotframework.git)

#   Task 6: Raportowanie błędów i raport z testów
  ## Subtask 2: Zgłaszanie błędów
  👉 [My reported bugs(auto)](https://docs.google.com/spreadsheets/d/1FIdp6GxTHnairIT1u8cfehFB0X-CVmjoOduRehm3puQ/edit?usp=drive_link)

  ## Subtask 3: Raport z testów
  👉 [Test report auto](https://docs.google.com/spreadsheets/d/1hMPS9euSHF762eKXP4l0XdkegYESSOrABoE-5sMd2X0/edit?usp=drive_link)

  ## Subtask 4: Moje portfolio
  👉 [PORTFOLIO Martyna Bródka](https://github.com/martynabrodka/portfolio_martyna_brodka/blob/main/README.md#portfolio_martyna_brodka)