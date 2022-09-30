import time
import sys
import paho.mqtt.client as mqtt
from pymodbus.client.sync import ModbusTcpClient
import datetime

THINGSBOARD_HOST = 'demo.thingsboard.io'
ACCESS_TOKEN = 'djPnvrIXbjqAcE2HlwqJ'
IP_Address = 'localhost'
Port = 503
#IP_Address = '192.168.1.11'
INTERVAL=2
address_count = 10
old = []
for i in range(address_count): old.append('')

modbusclient = ModbusTcpClient(IP_Address,Port)
#next_reading = time.time()
client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

#read_register = 200
#read_register2 = 100
#read_qty = 10
#print("Connect MQTT")
#print("client can connect")
#try:
print(modbusclient.connect())
while True:

    x = datetime.datetime.now()
    #result = client.read_holding_registers(0,address_count,unit=0x01)
    result = modbusclient.read_input_registers(200,address_count,unit=0x01)
    #address : 300201-300210
    h = result.registers
    for j in range(address_count):
        if old[j] != h[j]:
            if old[j] != '':
                print( 'Time : '+ str(x) +' Address : '+ str(j) +' Value : '+ str(h[j]))
                payload = "{Address"+str(j)+": " + str(result.registers[j]) + "}"
                client.publish('v1/devices/me/telemetry', payload)
            old[j] = h[j]

    time.sleep(0.1)
        # print("Temperature: {0}, Humidity: {1}".format(temperature, humidity))
        #result = client2.read_input_registers(read_register,read_qty,unit=0x01)
        #result2 = client2.read_input_registers(read_register2,read_qty,unit=0x01)
        #payload2 = "{\"Address 100-110\": " + str(result2.registers) + "}"
        #payload = "{\"Address 200-210\": " + str(result.registers) + "}"
        #client.publish('v1/devices/me/telemetry', payload)
        #client.publish('v1/devices/me/telemetry', payload2)
        #print(payload);
        #print(payload2);
        #next_reading += INTERVAL
        #sleep_time = next_reading-time.time()
        #if sleep_time > 0:
           # time.sleep(sleep_time)
        
#except KeyboardInterrupt:
#    pass

client.loop_stop()
client.disconnect()
