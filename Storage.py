from time import gmtime, strftime
from subprocess import check_output
import bluetooth
import LED

def get_bluetooth_mac_addr():
    addr_info = str(check_output(["hcitool", "dev"]), "UTF-8")
    chunks = addr_info.split('\t')
    mac_addr = chunks[-1][:-1]
    return mac_addr

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
# Get mac address
mac = get_bluetooth_mac_addr()
print(strftime("[%H:%M:%S] ", gmtime()) + "Created socket at " + mac + " on port " str(port)) 
server_sock.bind(("",port))

# List for clients
print(strftime("[%H:%M:%S] ", gmtime()) + "Listening for client connections")
server_sock.listen(1)

client_sock,address = server_sock.accept()
print(strftime("[%H:%M:%S] ", gmtime()) + " Accepted connection from " + str(address) + " on port " + str(port))

data = client_sock.recv(1024).decode("utf-8")
print(strftime("[%H:%M:%S] ", gmtime()) + " Received Payload: " + str(data))

client_sock.close()
server_sock.close()

led = LED.LED(int(data))
led.showVarieties()
