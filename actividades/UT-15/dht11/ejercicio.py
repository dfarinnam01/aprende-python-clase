import time
import board
import adafruit_dht

# DHT11 conectado al GPIO4 (pin físico 7)
dht = adafruit_dht.DHT11(board.D4)

while True:
    try:
        temperatura = dht.temperature
        humedad = dht.humidity

        print(f"Temperatura: {temperatura} °C")
        print(f"Humedad: {humedad} %")
        print("-" * 20)

    except RuntimeError:
       print("Error mi loco")

    time.sleep(2)
