import pytest
from selenium import webdriver
from support.PageObjects.GooglePage import GooglePage
from support.StepObjects.GoogleSteps import GoogleSteps


class TestGoogleSearch:
    driver = 0

    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1024,768")
        options.add_argument(
            '--user-agent="Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1"')
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe", chrome_options=options)
        self.driver.implicitly_wait(5)

    def test_search(self):
        self.driver.get("https://www.google.com/")
        tester = GoogleSteps(self.driver)
        tester.setValueInSearch("GeForce 1650")
        result = tester.getCountResultSearch()
        assert result > 0, "Количество найденых ответов должно быть больше 0"

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()
