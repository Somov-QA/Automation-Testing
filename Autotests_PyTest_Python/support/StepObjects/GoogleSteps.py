from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from support.PageObjects.GooglePage import GooglePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleSteps:
    driver = 0

    def __init__(self, webdriver):
        self.driver = webdriver

    def setValueInSearch(self, value):
        searchField = GooglePage.getInputSearch(self.driver)
        searchField.send_keys(value)
        searchField.send_keys(Keys.ENTER)

    def getCountResultSearch(self):
        resultElements = GooglePage.getListResultsSearch(self.driver)
        return len(resultElements)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")
