import network
import time
import machine

WIFI_SSID = "nombre de tu wifi"  
WIFI_PASSWORD ="Contraseña"  

def connect_to_wifi(ssid, password):

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print("Conectando a la red WiFi...")
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            print("Intentando conectar...")
            time.sleep(1)

   
    if wlan.isconnected():
        print("¡Conexión exitosa!")
        print("Dirección IP:", wlan.ifconfig()[0])
    else:
        print("No se pudo conectar a la red WiFi.")


def check_wifi_connection():
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        print("Conexión WiFi activa.")
        print("Dirección IP:", wlan.ifconfig()[0])
    else:
        print("No hay conexión WiFi.")

def reconnect_wifi():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print("Reconectando a la red WiFi...")
        connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)


connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)

while True:
    check_wifi_connection()  
    time.sleep(10)  
    reconnect_wifi() 
