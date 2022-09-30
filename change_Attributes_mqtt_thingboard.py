import time
import sys
import paho.mqtt.client as mqtt

THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = '8wKkSElnm23l50XPBh1T'

# Data capture and upload interval in seconds. Less interval will eventually hang the DHT22.
INTERVAL=2
humidity = 250
temperature = 1020
next_reading = time.time() 
client = mqtt.Client()
# Set access token
client.username_pw_set(ACCESS_TOKEN)
# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()
print("Connect MQTT")
try:
    while True:
        print("Temperature: {0}, Humidity: {1}".format(temperature, humidity))
        payload = "{\"Humidity\": " + str(humidity) + "," + "\"Temperature\": " + str(temperature)+ "}"
        # Sending humidity and temperature data to ThingsBoard
        client.publish('v1/devices/me/attributes', payload)
        humidity += 1
        temperature += 1
        print(payload);
        next_reading += INTERVAL
        sleep_time = next_reading-time.time()
        if sleep_time > 0:
            time.sleep(sleep_time)
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
