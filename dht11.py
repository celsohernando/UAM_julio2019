import Adafruit_DHT
import time
import json

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 14

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
      data = {'temperature': temperature, 'humidity': humidity}
      print(json.dumps(data))
      
    else:
      data = {'Error': 'check wirings'}
      print(json.dumps(data))
      
    time.sleep(3)
