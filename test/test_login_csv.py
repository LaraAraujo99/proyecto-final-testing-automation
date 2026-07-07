from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from page.login_page import LoginPage
from utils.data_reader import read_users_csv
import pytest

@pytest.mark.parametrize("user", read_users_csv())
def test_login(driver,user):
    login_page = LoginPage(driver)

    login_page.login(user["username"],user["password"])
    if user["valid"] == "true":    
      assert "/inventory.html" in driver.current_url, "No se redirigió al invntario"
    else: 
       error = login_page.get_error_message()
       assert "Epic sadface" in error








# driver = webdriver.Chrome()
# try:
#  # Ingreso a la página 
#     driver.get("https://www.saucedemo.com/")

# # Ingresar usuario
#     usuario = driver.find_element(By.ID,"user-name")
#     usuario.send_keys("standard_user")

# # Ingresar contraseña
#     password = driver.find_element(By.ID, "password")
#     password.send_keys("secret_sauce")

# # Presionar boton login
#     password.send_keys(Keys.RETURN)

#     # boton = driver.find_element(By.ID, "login-button").click()

# # Verificar URL
#     if "/inventory.html" in driver.current_url:
#         print("Ok")
#     else:
#         print("Fail")

# finally:
#     driver.quit()