import pika
import time
import json
from src.argParser import processor_parser

args = processor_parser().parse_args()
bt_strorage = args.bt_addr
port = args.port_num
soc = args.socket_size

clientMessage = "" #dict type
bluetoothMessage = "" 

print("["+time.ctime()+"]" + " Checkpoint  00: Created rabbitmq at 0.0.0.0")
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

def send_command(bd_addr, command, port):
	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	sock.connect((bd_addr, port)) #first port in bluetooth
	
	print "Sending command (%s)" % command
	sock.send(command)
	sock.settimeout(4)
	response = ""
	try:
		while True:
			r = sock.recv(255)
			if not r:
				break
			response = response + r
			if r.find(";") != -1: # we have reach end of message
				break
	except:
		pass

    print("["+time.ctime()+"]" + " Checkpoint  04: Received answer payload :"+response)
	sock.close() 

def createResponse(string):
    return string

def connectblue(n):
    print("["+time.ctime()+"]" + " Checkpoint  03: Connecting to"+ bt_strorage +" on port " + port)
    print(n)
    return createResponse(n)

def on_request(ch, method, props, body):
    clientMessage = json.loads(body)
    print("["+time.ctime()+"]" + " Checkpoint  02: Recieved request payload : "+ str(body))
    response = connectblue(body)

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
