# WebScraping en Python
## Se accede a
* SRI
    * Facturas Electronicas
        * Comprobantes electrónicos recibidos

---
Python
pip install setuptools
* Flask -  pip install Flask
* json  
* time  
* webdriver_manager.chrome - pip install webdriver-manager
* selenium - pip install selenium  

[Requerimentos](requirements.txt)

---
GET  
* /api/datos

http://127.0.0.1:5000/api/datos/?ruc=0992933607001&contrase%C3%B1a=NEXT2021next*&a%C3%B1o=2023&mes=4&dia=0

---
[Url del SRI que se accede](https://srienlinea.sri.gob.ec/auth/realms/Internet/protocol/openid-connect/auth?client_id=app-sri-claves-angular&redirect_uri=https%3A%2F%2Fsrienlinea.sri.gob.ec%2Fsri-en-linea%2F%2Fcontribuyente%2Fperfil&state=6a24eaa5-88c2-4636-a37c-12f95b58befc&nonce=b8104ad7-3c32-4571-85bc-8e4a86df3f2e&response_mode=fragment&response_type=code&scope=openid)  

Metodo que se utiliza  
obtenerdatos(ruc, contraseña, año, mes, dia)  
Datos que se deben ingresar  
* ruc  
* contraseña  
* año  
* mes  
* dia  