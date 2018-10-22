import pika
import json
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
ipadd = args.proc_ip

#preparing the payload
payload = prep(args)

#setting up the RabbitMQ queue
queue = sendClientRequest(ipadd)
response = queue.call(payload)
res = response.decode("utf-8").replace("{'Msg': '", "").replace("'}", "")

print("["+time.ctime()+"]" + " Checkpoint  02: Response : "+ res)
