import paho.mqtt.client as mqtt


BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "rumah/lampu"


client = mqtt.Client()
client.connect(BROKER, PORT, 60)


while True:
    cmd = input("Ketik ON / OFF: ").upper()
    if cmd in ["ON", "OFF"]:
        client.publish(TOPIC, cmd, qos=1)
        print(f"Kirim perintah: {cmd}")