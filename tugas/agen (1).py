import paho.mqtt.client as mqtt
import time
import random

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "capstone/data"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)
client.loop_start()

print("Agent berjalan...")

while True:
    data = {
        "device": "agent-01",
        "suhu": round(random.uniform(25, 35), 2),
        "cpu": round(random.uniform(10, 90), 2)
    }

    client.publish(TOPIC, str(data), qos=1)
    print("Kirim:", data)
    time.sleep(2)