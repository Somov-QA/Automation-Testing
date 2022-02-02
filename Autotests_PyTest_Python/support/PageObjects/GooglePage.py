class GooglePage:
    inputSearchName = "q"
    searchResultsClass = "g"

    def getInputSearch(self):
        inputSearch = self.driver.find_element_by_name(GooglePage.inputSearchName)
        return inputSearch

    def getListResultsSearch(self):
        searchResult = self.driver.find_elements_by_class_name(GooglePage.searchResultsClass)
        return searchResult
