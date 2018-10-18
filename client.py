import pika
from src.argParser import client_parser
from src.checkAction import check
from src.clientPayload import prep
import src.clientSendRq
import time
import sys

print("["+time.ctime()+"]" + " Checkpoint  00: Initialized client")

args = client_parser().parse_args()
argFlag = check (args)
if not argFlag:
    sys.exit(0)

#preparing the payload
payload = prep(args)
