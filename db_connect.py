import base64
import paho.mqtt.client as mqtt
import json
from datetime import datetime
import pymongo

#Global Variables
topicsList=[]
client = pymongo.MongoClient("mongodb+srv://User_1:IOT2019@cluseteray-0qixz.mongodb.net/test?retryWrites=true&w=majority")
db=client.parkingStatus.status

def getTopics():
    topics=client.parkingStatus.topics
    cursor = topics.find({})
    for document in cursor:
          topicsList.append(document['topic'])

def Connect():

    print("Connecting ......................")

    #Settings
    MQTT_Broker = "212.98.137.194"
    MQTT_Port = 1883
    Keep_Alive_Interval = 60

    #Client Insatance
    client = mqtt.Client()
    client.username_pw_set('user','bonjour')

    #Functions definition
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        for i in topicsList:
            client.subscribe(i)
            client.subscribe(i)
    
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
    getTopics()
    client.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

    # Keep alive
    client.loop_forever()

def getStatus():
    a=db.find().sort("created_on",-1).limit(1)
    a=list(a)
    a=a[0]["status"]
    a=json.dumps(a)
    return a