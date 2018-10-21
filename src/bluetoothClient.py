import bluetooth
import bluetoothvars

def sendToStorage(instr):
    port =1 
    sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    sock.connect((bd_storage, port))
    sock.send("hello!!")
    sock.close()

sendToStorage("hello")