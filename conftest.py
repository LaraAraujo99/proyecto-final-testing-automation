import pytest
from selenium import webdriver 
from utils.login_page import login 

@pytest.fixture
def driver():
    # Inicialización del navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options = options)

# yield similar a un return 
    yield driver 

    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
