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