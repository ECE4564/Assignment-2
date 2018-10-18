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

queue = sendClientRequest()
print(" [x] Requesting fib(30)")
response = queue.call(30)
print(" [.] Got %r" % response)