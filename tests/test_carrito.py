from selenium import webdriver
from selenium.webdriver.common.by import By


def test_carrito():
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

        # agregamos la mochila al carrito
        agregar = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        agregar.click()

        # verificamos que el carrito tenga un producto
        cantidad = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cantidad.text == "1"

        # entramos al carrito
        carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        carrito.click()

        # verificamos que entramos al carrito
        assert "cart.html" in driver.current_url

        # verificamos que este la mochila
        assert driver.find_element(By.CLASS_NAME, "inventory_item_name").text == "Sauce Labs Backpack"

    finally:
        driver.quit()