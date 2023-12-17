import pika, json

params = pika.URLParameters('amqps://guaeccua:muAiHT_V_Gf9NXww-tvD7grP7zry-foX@rattlesnake.rmq.cloudamqp.com/guaeccua')
connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
