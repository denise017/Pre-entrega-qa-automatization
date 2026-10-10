from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    # abrimos el navegador
    driver = webdriver.Chrome()

    try:
        # entramos a la pagina
        driver.get("https://www.saucedemo.com/")

        # buscamos los elementos del login
        usuario = driver.find_element(By.ID, "user-name")
        contraseña = driver.find_element(By.ID, "password")
        boton = driver.find_element(By.ID, "login-button")

        # ingresamos los datos
        usuario.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        boton.click()

        # verificamos que entro al inventario
        assert "inventory.html" in driver.current_url

        # verificamos el logo y el titulo
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")

        assert logo.text == "Swag Labs"
        assert titulo.text == "Products"

    finally:
        driver.quit()