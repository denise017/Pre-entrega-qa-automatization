from selenium import webdriver
from selenium.webdriver.common.by import By


def test_catalogo():
    # abrimos el navegador
    driver = webdriver.Chrome()

    try:
        # entramos a la pagina
        driver.get("https://www.saucedemo.com/")

        # hacemos el login
        usuario = driver.find_element(By.ID, "user-name")
        contraseña = driver.find_element(By.ID, "password")
        boton = driver.find_element(By.ID, "login-button")

        usuario.send_keys("standard_user")
        contraseña.send_keys("secret_sauce")
        boton.click()

        # verificamos el titulo de la pagina
        assert driver.title == "Swag Labs"

        # buscamos todos los productos
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")

        # verificamos que haya productos
        assert len(productos) > 0

        # buscamos el primer producto
        primer_producto = productos[0]

        nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name")
        precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price")

        # verificamos el nombre y el precio
        assert nombre.text == "Sauce Labs Backpack"
        assert precio.text == "$29.99"

        # verificamos que el menu y el filtro esten visibles

        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

        assert menu.is_displayed()
        assert filtro.is_displayed()

    finally:
        driver.quit()