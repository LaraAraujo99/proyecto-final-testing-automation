from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_login_validation(login_in_driver):
    try:
        driver = login_in_driver

        assert "/inventory.html" in driver.current_url, "No se redirigio al inventario"
    except Exception as e:
        print(f"Error en test_logn: {e}")
        raise











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