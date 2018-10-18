import pika
from src.argParser import client_parser
from src.checkAction import check

args = client_parser().parse_args()
print(args)
# ret = check (args)
# print(ret)