import time

class NavegatePage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self):
        self.driver.get('https://claro.qualtrics.com/reporting-dashboard/web/6616d90f5c152200082e2233/pages/Page_4bccad9e-f0d7-4265-8a8c-22b831245106/view')
        time.sleep(5)
        