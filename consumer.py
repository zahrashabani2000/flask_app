import pika, json

params = pika.URLParameters('amqps://guaeccua:muAiHT_V_Gf9NXww-tvD7grP7zry-foX@rattlesnake.rmq.cloudamqp.com/guaeccua')

connection = pika.BlockingConnection(params)

channel = connection.channel()


channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Recived in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        db.session.add(product)
        db.session.commit()
        print('Product Created')
    
    elif properties.content_type == 'product_updated':
        product = Product.query.get(data=['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit()
        print('Product updated')

    
    elif properties.content_type == 'product_deleted':
        product = Product.query.get(data)
        db.session.delete(product)
        db.session.commit()
        print('Product deleted')


channel.basic.consume(queue='rabbitPro', on_massage_callback=callable)

print('Started consuming')

channel.start_consuming()

channel.close()