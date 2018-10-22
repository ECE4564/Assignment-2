# Assignment-2
## System Syntax 
### Client Operation 
The client can be run in the following manner: 
```
client.py -proc <Processor IP Addr> -action <Action> -book <Book Info>
```
The IP address following the -proc flag specifies the IP address for the intermediary 
between the client and the storage server, known as the processor. The client and the 
processor will communicate via RabbitMQ Remote Procedure Call. The argument following 
the -action flag can be either ADD, BUY, SELL, DELETE, COUNT, or LIST. This determines 
what operation will be performed in the database on the next piece of information passed 
to the program, the Book Info. 
### Processor Operation 
The processor can be run in the following manner:
```
processor.py -storage <Storage Bluetooth Mac Addr> -p <Storage Port Number> -z <Socket Size> 
```
As described above, the processor acts as an intermediate step between the client and the 
storage server, Therefore it requires the Bluetooth Mac address and port number of the 
storage, as the processor and storage will communicate via Bluetooth. The Mac address 
follows the -storage flag, and the storage port number follows the -p flag. Finally, 
a socket size can be designated following the -z flag according to the needs of the program. 
### Storage Operation 
The storage can be run in the following manner: 
```
storage.py -p <Port Number> -b <Backlog> -z <Socket Size> 
```
Following the -p flag, the port number to listen for communication from the processor 
can be specified. No Mac address argument is needed here, because the processor will 
initiate the communication between the two. A backlog size can be specified following the 
-b flag, and the socket size can be specified following the -z flag. 