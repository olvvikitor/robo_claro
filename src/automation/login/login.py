import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import src.automation.configs.driverConstructor as driverConstructor

BASE_URL = "https://claro.qualtrics.com"

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        driver_instance = driverConstructor.DriverConstructor()
        self.driver = driver_instance.get_driver()

    def perform_login(self):
        try:
            # abre a página inicial do Qualtrics
            self.driver.get(f"{BASE_URL}/Q/MyProjectsSection")

            # preenche username
            username_input = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, 'username'))
            )
            username_input.send_keys(self.username)

            # preenche password
            password_input = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.ID, 'password'))
            )
            password_input.send_keys(self.password)

            # clica no botão de login
            self.driver.find_element(By.ID, "signOnButton").click()

            # aguarda PIN
            pin = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div[3]"))
            )
            print(f"PIN recebido: {pin.text.strip()}")

            # espera até realmente estar logado
            WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Projetos e programas')]"))
            )

            print("Login realizado com sucesso.")
            return True


        except (NoSuchElementException, TimeoutException) as e:
            print("Erro no login:", e)
            return False
