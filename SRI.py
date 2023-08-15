# pip install selenium

    # Usar si no se tiene instalado el driver
# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager

    # Librerias
import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

    # Url que se va a abrir
url = 'https://srienlinea.sri.gob.ec/auth/realms/Internet/protocol/openid-connect/auth?client_id=app-sri-claves-angular&redirect_uri=https%3A%2F%2Fsrienlinea.sri.gob.ec%2Fsri-en-linea%2F%2Fcontribuyente%2Fperfil&state=5f407cb6-8e2f-42cf-862d-1db82e9ee733&nonce=7170967a-159d-4c56-a389-181abb76b503&response_mode=fragment&response_type=code&scope=openid'

    # Credenciales que se usaran
# ruc = "0992933607001"
# contraseña = "NEXT2021next*"
# año = "2023"
# mes = "4"
# dia = "0"

def obtenerdatos(ruc, contraseña, año, mes, dia):
        # Opciones con las que inicia el driver/navegador
    options = Options()
    options.add_experimental_option("detach", True)
    # options.add_argument('--headless')  # Ejecutar en modo headless, sin mostrar el navegador, se daña
    options.add_argument("--start-maximized")
    # options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')

        # Driver que se usa para abrir el navegador con la opciones, usar la segunda si no se tiene instalado el driver (https://chromedriver.chromium.org/downloads)
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Abre el navegador con la Url, ingresado en ventana maximizada
    driver.get(url)
    # driver.maximize_window()

    time.sleep(15)
    usuario = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#usuario'))
    ).send_keys(ruc)
    time.sleep(15)
    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#password'))
    ).send_keys(contraseña)
    time.sleep(5)
    login = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'input#kc-login'))
    ).click()
    time.sleep(10)
    SideBar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button#sri-menu'))
    ).click()
    time.sleep(15)
    Facturacion = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "FACTURACIÓN ELECTRÓNICA")]'))
    ).click()
    time.sleep(15)
    Comprobantes = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "Comprobantes electrónicos recibidos")]'))
    ).click()
    time.sleep(15)
    SelectYear = Select(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'frmPrincipal:ano')))
    ).select_by_value(año)
    time.sleep(15)
    SelectMonth = Select(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'frmPrincipal:mes')))
    ).select_by_value(mes)
    time.sleep(15)
    SelectDay = Select(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'frmPrincipal:dia')))
    ).select_by_value(dia)
    time.sleep(15)
    Consultar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button#btnRecaptcha'))
    ).click()


    time.sleep(60)    
    print("Inicio")

    Select75 = Select(WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'ui-paginator-rpp-options')))
    ).select_by_value('75')

    time.sleep(15)

    data = []
    nombres_campos = ["Nro","RUC", "Comprobante", "Clave / Autorizacion", "Fecha_Autorizacion", "Fecha_Emision", "Tipo"]
    page = 1

    while True:
        print("tabla")
        tabla = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'frmPrincipal:tablaCompRecibidos_data')))

        filas = tabla.find_elements(By.TAG_NAME, 'tr')

        for i, fila in enumerate(filas):
            fila_data = {}
            celdas = fila.find_elements(By.TAG_NAME, 'td')
            for j, celda in enumerate(celdas):
                if j==0 or j==7 or j==8 or j==9:continue
                nombre_campo = nombres_campos[j]
                texto_celda = celda.text
                fila_data[nombre_campo] = texto_celda
                # print(texto_celda)
            data.append(fila_data)
        
        try:    
            next_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.ui-paginator-next')))
            
            is_enabled = 'ui-state-disabled' not in next_button.get_attribute('class')
            if not is_enabled:
                print("Se ha alcanzado el final de las páginas.")
                break
            
            next_button.click()
            page += 1
            time.sleep(10)
        except Exception as e:
            print("Ocurrió una excepción:", str(e))
            break

    driver.quit()
    print("Fin")
    final_data = {str(i + 1): row_data for i, row_data in enumerate(data)}

    with open('tabla_data.json', 'w') as file:
        json.dump(final_data, file, indent=4)
