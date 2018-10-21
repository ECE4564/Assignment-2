from time import sleep, gmtime, strftime
from subprocess import check_output
from src.argParser import storage_parser
import bluetooth
import threading
import signal
import sys
import LED
import MongoDB

def get_bluetooth_mac_addr():
    addr_info = str(check_output(["hcitool", "dev"]), "UTF-8")
    chunks = addr_info.split('\t')
    mac_addr = chunks[-1][:-1]
    return mac_addr

def signal_handler(sig, frame):
    print("\nExitting program...")
    kill_program = 1
    threadLED.join()
    sys.exit(0)

def MongoControl():
    # Get mac address
    mac = get_bluetooth_mac_addr()
    print(strftime("[%H:%M:%S] ", gmtime()) + "Created socket at " + mac + " on port " + str(port)) 
    server_sock.bind(("",port))

    # List for clients
    print(strftime("[%H:%M:%S] ", gmtime()) + "Listening for client connections")
    server_sock.listen(1)

    client_sock,address = server_sock.accept()
    print(strftime("[%H:%M:%S] ", gmtime()) + " Accepted connection from " + str(address) + " on port " + str(port))

    data = client_sock.recv(1024).decode("utf-8")
    print(strftime("[%H:%M:%S] ", gmtime()) + " Received Payload: " + str(data))

    # when data is received, initialize MongoDB
    db = MongoDB.MongoDB()
    db_result = ""

    # update database based on received action
    action = data["Action"]
    if action == "ADD":
        db_result = db.insert(data["Book Info"])
    elif action == "BUY":
        db.change_stock(data["Book Info"], data["Count"])
    elif action == "SELL":
        db.change_stock(data["Book Info"], -data["Count"])  # not sure if this will negate the value correctly
    elif action == "LIST":
        db_result = db.list_all()
    elif action == "DELETE":
        db.remove(data["Book Info"])
    elif action == "COUNT":
        book_list = db.list_all()
        in_stock = 0
        for book in book_list:
            if book["stock"] != 0:
                in_stock += 1
        db_result = "OK: " + str(in_stock) + " books in stock"

    # send result
    # something like:
    # client_sock.send(payload["Msg"] = db_result

    client_sock.close()
    server_sock.close()

def LEDShow():
    while(1):
        led = LED.LED(254)
        led.showVarieties()
        if kill_program == 1:
            print('Exit')
            led.turnOff()
            break

# Get command line arguments
args = storage_parser().parse_args()

# Start bluetooth socket
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

# Create clean exit signal
signal.signal(signal.SIGINT, signal_handler)

port = 1
kill_program = 0

# Start the two threads
threadLED = threading.Thread(target=LEDShow, args=())
threadMongo = threading.Thread(target=MongoControl, args=())

threadLED.daemon = True
threadMongo.daemon = True

threadLED.start()
threadMongo.start()

threadMongo.join()
threadLED.join()
