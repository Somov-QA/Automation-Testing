import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture()
def driver():
    # Setup
    web_driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
    web_driver.set_window_size(1920, 1000)
    web_driver.set_window_position(0, 0)
    web_driver.fullscreen_window()
    # Test
    yield web_driver
    # Teardown
    web_driver.close()
    web_driver.quit()


def test_order(driver):
    driver.get("https://mgts.ru/")
    locator_button = "//div[contains(@class, 'header_desktop')]//button[@class='btn-blue']"
    button = driver.find_element(By.XPATH, locator_button)
    button.click()

    time_wait = 25
    locator_popup = "//div[@class='popup_body']"
    WebDriverWait(driver, time_wait).until(EC.presence_of_element_located((By.XPATH, locator_popup)),
                                      message=f"Can't find element by locator {locator_popup}")
    input_name = driver.find_element(By.ID, "popup_name")
    input_name.send_keys("Тестирование Зионек")
    time.sleep(1)
    input_phone = driver.find_element(By.ID, "popup_phone")
    input_phone.send_keys("9999999999")
    time.sleep(1)
    button_send = driver.find_element(By.ID, "SUBMIT_ORDER")
    button_send.click()

    time_wait = 25
    WebDriverWait(driver, time_wait).until(EC.presence_of_element_located((By.ID, "last_order_sended")),
                                      message=f"Can't find element by locator last_order_sended")

    # assert result > 0, "Количество найденых ответов должно быть больше 0"
