import paho.mqtt.client as mqtt
import json
import time

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "capstone/data"
DATABASE = "database.json"

def save_data(data):
    try:
        with open(DATABASE, "r") as f:
            db = json.load(f)
    except:
        db = []

    db.append(data)

    with open(DATABASE, "w") as f:
        json.dump(db, f, indent=2)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    data = eval(payload)   # parsing dict string
    data["timestamp"] = time.time()
    save_data(data)
    print("Data diterima:", data)

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)

print("Core Server aktif...")
client.loop_forever()