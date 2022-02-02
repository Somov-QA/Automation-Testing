import pytest
from selenium import webdriver
from support.PageObjects.GooglePage import GooglePage
from support.StepObjects.GoogleSteps import GoogleSteps

# https://docs.pytest.org/en/6.2.x/xunit_setup.html
# setup , test, teardown

def setup_modile():
    print("setup")

def test_one():
    print("test")

def teardown_module():
    print("teardown")

if __name__ == "__main__":
    pytest.main(["-s", "test_google_search2.py"])