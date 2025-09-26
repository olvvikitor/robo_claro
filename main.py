import src.automation.login.login as login_module
import src.automation.navegation.navegatePage as navegation_module
class Main:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login_instance = login_module.Login(self.username, self.password)

    def run(self):
        if self.login_instance.perform_login():
            print("Login successful.")
            navegation_instance = navegation_module.NavegatePage(self.login_instance.driver)
            navegation_instance.navigate_to_page()
        else:
            print("Login failed.")

if __name__ == "__main__":
    USERNAME = "93239859"
    PASSWORD = "N1nh@*25"
    main_instance = Main(USERNAME, PASSWORD)
    main_instance.run()