# 5)Write socket program in Python to send a message from a
# client machine to a server machine
# and a server machine to a client machine using TCP.
import socket

s = socket.socket()
host = socket.gethostname()
port = 23456

# Connect to the server
s.connect((host, port))

# Receive the thank you message
mssg = s.recv(1024)
print("Server says:", mssg.decode('utf-8'))

# Send a reply back to the server
s.send(b'hello from client')

# Close the connection
s.close()


# output
# Server says: Thank you for connecting
