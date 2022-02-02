import pytest
from selenium import webdriver
from support.PageObjects.GooglePage import GooglePage
from support.StepObjects.GoogleSteps import GoogleSteps


class TestGoogleSearch:
    driver = 0

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
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
