import pytest
from selenium import webdriver 
# from utils.login_page import login 
from page.login_page import LoginPage
from utils.data_reader import read_users_csv

import pathlib
import pytest_html

@pytest.fixture
def driver():
    # Inicialización del navegador
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options = options)


    yield driver 

    driver.quit()

@pytest.fixture
def driver_logged(driver):
    login_page = LoginPage(driver)
    
    user = read_users_csv()[0]

    login_page.login(user["username"],user["password"])

    return driver

# Hook de pytest
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item,call):
    # item: representa el test que se está corriendo / call: Contiene la info sobre la ejecución del test
    outcome = yield
    # Registro del test en outcome

    report = outcome.get_result()

    # When = setup(preparación de la prueba), call(prueba corriendo) o teardown(finalización y eliminación de los datos de prueba)
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            target = pathlib.Path("reports/screenshots")
            # Crear la carpeta en caso de que no exista y si existe no genera otra carpeta
            target.mkdir(parents=True,exist_ok=True)

            # Nombre del archivo
            file_name = target / f"{item.name}.png"

            # Tomar captura de pantalla
            driver.save_screenshot(str(file_name))

            # verificar si se puede agregar otro dato (la captura) al reporte
            if hasattr(report, "extra"):
                report.extra.append({
                    "name": "screenshot",
                    "format": "imag",
                    "context": str(file_name)
                })

            extras = getattr(report, "extra", [])
            # añadir la captura al pytest_html
            extras.append(pytest_html.extras.png(str(file_name)))

            # Guardar las capturas extras dentro del reporte
            report.extras = extras