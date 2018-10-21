import pika
from src.argParser import client_parser
from src.checkAction import check
from src.clientPayload import prep
from src.clientSendRq import sendClientRequest
import time
import sys

print("["+time.ctime()+"]" + " Checkpoint  00: Initialized client")

args = client_parser().parse_args()
argFlag = check (args)
if not argFlag:
    sys.exit(0)

#preparing the payload
payload = prep(args)

#setting up the RabbitMQ queue
queue = sendClientRequest()
print(" [x] Requesting")
response = queue.call(payload)
print(" [.] Got %r" % response)