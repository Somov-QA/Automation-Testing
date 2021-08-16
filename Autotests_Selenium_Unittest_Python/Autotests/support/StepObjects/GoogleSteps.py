from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from support.PageObjects.GooglePage import GooglePage

class GoogleSteps:
    driver = 0

    def __init__(self, webdriver):
        self.driver = webdriver

    def setValueInSearch(self, value):
        searchField = GooglePage.getInputSearch(self)
        searchField.send_keys(value)
        searchField.send_keys(Keys.ENTER)

    def getCountResultSearch(self):
        resultElements = GooglePage.getListResultsSearch(self)
        return len(resultElements)