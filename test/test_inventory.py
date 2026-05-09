from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver

def test_inventory_title(driver_logged):
    titulo = driver_logged.title
    assert titulo == "Swag Labs", "El titulo de la pagina a la que se accede no es correcto"


def test_productos_visibles(driver_logged):
    # find_elements busca varios elementos
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    # Busco cuantos elementos tiene la lista y si es mayor a 0
    assert len(productos) > 0 


def test_ui_elements(driver_logged):
    # Capturar el elemento
    menu = driver_logged.find_element(By.ID,"react-burger-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")
    # Me permite saber si están visibles en la página
    # Hacer la prueba
    assert menu.is_displayed(), "El ícono del menu no está presente en la página"
    assert filtro.is_displayed(), "El filtro del catálogo no  está presente en la página"