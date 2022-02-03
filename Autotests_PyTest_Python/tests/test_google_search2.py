import pytest
from selenium import webdriver
from support.PageObjects.GooglePage import GooglePage
from support.StepObjects.GoogleSteps import GoogleSteps


@pytest.fixture()
def init_driver():
    # Setup
    driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
    # Test
    yield driver
    # Teardown
    driver.close()
    driver.quit()


def test_search(init_driver):
    init_driver.get("https://www.google.com/")
    tester = GoogleSteps(init_driver)
    tester.setValueInSearch("GeForce 1650")
    result = tester.getCountResultSearch()
    assert result > 0, "Количество найденых ответов должно быть больше 0"
