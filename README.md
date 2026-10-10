En este proyecto se automatizaron algunas funcionalidades de la pagina "saucedemo" utilizando python, selenium y pytest

Se realizaron tres pruebas (que se ejecutan de forma independiente): inicio de sesion con credenciales validas, verificacion del cátalogo de productos y agregar un producto al carrito para comprobar que aparezca correctamente

Para instalar las dependencias primero hay que crear y activar un entorno virtual:

--python3 -m venv .venv

--source .venv/bin/activate

Despues instalar las dependencias:

--pip install -r requirements.txt

Para ejecutar las pruebas:

--python -m pytest

El reporte HTML se genera automáticamente al ejecutar las pruebas gracias a la configuracion del archivo pytest.ini Y los reportes se guardan en la carpeta reports, en el archivo reporte.html

Las tres pruebas se ejecutaron correctamente con un resultado de 3 passed y 0 failed