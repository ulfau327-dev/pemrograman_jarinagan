import paho.mqtt.client as mqtt


BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "rumah/lampu"




def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC)




def on_message(client, userdata, msg):
    pesan = msg.payload.decode()
    if pesan == "ON":
        print("💡 NYALA")
    elif pesan == "OFF":
        print("⚫ MATI")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(BROKER, PORT, 60)
client.loop_forever()