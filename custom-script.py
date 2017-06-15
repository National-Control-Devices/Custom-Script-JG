#import socket object for TCP communications
import socket
import time

#change to IP address of the board
IPADDRESS = "192.168.1.22"
#change the time to delay between on and off commands
DELAY = 5
#change the total number of times the loop will run
TOTALLOOPS = 9

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IPADDRESS, 2101))
print "Beginning Loop"

for i in range(0,TOTALLOOPS):
    for currentRelay in range(0,32):
        checksum = (170 + 3 + 254 + 148 + currentRelay) & 255
        command = bytearray([170, 3, 254, 148, currentRelay, checksum])
        s.send(command)
        time.sleep(DELAY)
        bback = s.recv(8)
        checksum = (170 + 3 + 254 + 147 + currentRelay) & 255
        command = bytearray([170, 3, 254, 147, currentRelay, checksum])
        s.send(command)
        bback = s.recv(8)
print "Done with Loop"
