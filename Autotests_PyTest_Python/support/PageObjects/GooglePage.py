from selenium.webdriver.common.by import By

class GooglePage:
    inputSearchName = "q"
    searchResultsClass = "g"

    def getInputSearch(driver):
        #inputSearch = driver.find_element_by_name(GooglePage.inputSearchName)
        inputSearch = driver.find_element(By.NAME, GooglePage.inputSearchName)
        return inputSearch

    def getListResultsSearch(driver):
        #searchResult = driver.find_elements_by_class_name(GooglePage.searchResultsClass)
        searchResult = driver.find_elements(By.CLASS_NAME, GooglePage.searchResultsClass)
        return searchResult
