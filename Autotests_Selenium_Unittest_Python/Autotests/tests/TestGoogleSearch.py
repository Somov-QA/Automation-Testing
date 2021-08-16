import unittest

from selenium import webdriver
from support.PageObjects.GooglePage import GooglePage
from support.StepObjects.GoogleSteps import GoogleSteps

class TestGoogleSearch(unittest.TestCase):

    def test_search(self):
        driver = webdriver.Chrome(executable_path="../webdriver/chromedriver.exe")
        driver.get("https://www.google.com/")
        tester = GoogleSteps(driver)
        tester.setValueInSearch("GeForce 1650")
        result = tester.getCountResultSearch()
        print("Count: ", result)
        self.assertNotEqual(0, result);
        print("Tests finished: SUCCESS")
        driver.close()
        driver.quit()


if __name__ == '__main__':
    unittest.main()
