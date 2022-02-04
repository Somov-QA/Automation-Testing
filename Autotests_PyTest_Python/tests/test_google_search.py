import pytest
from selenium import webdriver
from support.PageObjects.GooglePage import GooglePage
from support.StepObjects.GoogleSteps import GoogleSteps

def test_search():
    driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe") # устарело
    driver.get("https://www.google.com/")
    tester = GoogleSteps(driver)
    tester.setValueInSearch("GeForce 1650")
    result = tester.getCountResultSearch()
    assert result != 0, "Количество найденых ответов должно быть больше 0"
    driver.close()
    driver.quit()

if __name__ == '__main__':
    #pytest.main()
    pytest.main(["-s -v", "test_google_search.py"])