from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_cart(login_in_driver):
    driver = login_in_driver

    # Agregar producto al carrito
    driver.find_elements(By.CLASS_NAME, "btn_inventory")[0].click()
    
    contador_cart = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    assert contador_cart.text == "1", "El producto no de agrego correctamente"

    # Obtener nombre del primer producto
    product_name = driver.find_elements(By.CLASS_NAME,"inventory_item_name")[0].text

    # Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Obtener el nombre del producto en el carrito
    cart_item = driver.find_element(By.CLASS_NAME,"inventory_item_name").text

    # Verificar que los nombres sean iguales
    assert cart_item == product_name, "El producto agregado no coincide"

