import base64
import paho.mqtt.client as mqtt
import json
from datetime import datetime
import pymongo

#MongoDB Connector
client = pymongo.MongoClient("mongodb+srv://User_1:IOT2019@cluseteray-0qixz.mongodb.net/test?retryWrites=true&w=majority")
db=client.parkingStatus.status

def Connect():

    print("Connecting ......................")

    #Settings
    MQTT_Broker = "212.98.137.194"
    MQTT_Port = 1883
    Keep_Alive_Interval = 60
    MQTT_Topic1 = "application/19/device/d9e867a11f60c195/rx"
    MQTT_Topic2 = "application/19/device/3bcd5eaa94e9877c/rx"


    
    #Client Insatance
    client = mqtt.Client()
    client.username_pw_set('user','bonjour')

    #Functions definition
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(MQTT_Topic2)
        client.subscribe(MQTT_Topic1)
    
    def on_message(client, userdata, msg):
        m = json.loads(msg.payload)
        status=m['object']['payload']
        print(status)
        date=datetime.now()
        spots={"status":status,"created_on":date}
        db.insert_one(spots)
    
    #Callbacks assignment
    client.on_message = on_message
    client.on_connect = on_connect
    
        
    # Connection start
    client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

    # Keep alive
    client.loop_forever()

def getStatus():
    a=db.find().sort("created_on",-1).limit(1)
    a=list(a)
    print(a)