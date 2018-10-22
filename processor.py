import pika
import time
import json
from src.argParser import processor_parser
import bluetooth

args = processor_parser().parse_args()
bt_strorage = args.bt_addr
port = args.port_num
sock_size = args.socket_size

clientMessage = "" #dict type
bluetoothMessage = "" 

print("["+time.ctime()+"]" + " Checkpoint  00: Created rabbitmq at 0.0.0.0")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

def send_command(command):
	print("["+time.ctime()+"]" + " Checkpoint  03: Connecting to"+ bt_strorage +" on port " + port)
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bt_strorage, int(port))) #first port in bluetooth
	
	sock.send(command)
	
	response = ""
	r = sock.recv(int(sock_size))
	print(r)
	response = response + str(json.loads(r.decode("utf-8")))
	
	print("["+time.ctime()+"]" + " Checkpoint  04: Received answer payload :"+response)
	sock.close()
	return response


def on_request(ch, method, props, body):
    clientMessage = json.loads(body.decode("utf-8"))
    print("["+time.ctime()+"]" + " Checkpoint  02: Recieved request payload : "+ str(body))
    response = send_command(body)

    ch.basic_publish(exchange='',
                    routing_key=props.reply_to,
                    properties=pika.BasicProperties(correlation_id = \
                                                        props.correlation_id),
                    body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print("["+time.ctime()+"]" + " Checkpoint  01: Awaiting client requests")
channel.start_consuming()
