from selenium import webdriver

# Abro el navegador en pantalla completa
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

# Cierro el navegador
def after_scenario(context,scenario):
    context.driver.quit()
