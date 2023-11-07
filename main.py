from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

# Configurar el navegador
driver = webdriver.Chrome()

# URL de la página web
url = "https://shop.samsung.com/ar/lavasecarropas-9-5kg-con-control-ia-y-ecobubble-inox---beneficio-pre-registro/p?skuId=137773"
driver.get(url)

# Locator que deseas validar
locator = (By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div/div[1]/div/div[7]/div/section/div/div[2]/div/div[4]/div/div/div[2]")

while True:
    try:
        element = driver.find_element(*locator)
        if element.is_displayed():
            print("Locator encontrado en la página.")
            respuesta = "no hay stock"
        else:
            print("Locator no encontrado en la página. Notificando...")
            respuesta = "si hay stock"
        # URL del webhook de Google Chat
webhook_url = "https://chat.googleapis.com/v1/spaces/AAAARcBFhCU/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=JjX67BMcUAJmQfzfKywG-DhQDphWhULXpoA-sdyi-DU"

def enviar_notificacion(respuesta):
    payload = {
        "text": respuesta
    }
    
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(webhook_url, json=payload, headers=headers)

        if response.status_code == 200:
            print("Notificación enviada con éxito")
        else:
            print(f"Error al enviar la notificación. Código de estado: {response.status_code}")
    except Exception as e:
        print(f"Error al enviar la notificación: {str(e)}")

# Luego, puedes llamar a la función enviar_notificacion con el mensaje deseado
mensaje = "Nico el lavarropas!."
enviar_notificacion(mensaje)
    except:
        print("Error al buscar el locator.")
        respuesta = "error al buscar el locator"
