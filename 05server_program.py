import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket is created successfully")

host = socket.gethostname()
port = 23456

s.bind((host, port))
print("Socket is binded to %s" % (port))

s.listen(5)
print("Socket is listening")

while True:
    # Establish connection with client
    c, addr = s.accept()
    print('Got connection from', addr)

    # Send a thank you message to the client
    c.send(b'Thank you for connecting')

    # Receive the reply using the CLIENT socket 'c' (NOT 's')
    client_message = c.recv(1024)
    print("Client says:", client_message.decode('utf-8'))

    # Close the connection with this specific client
    c.close()

# ouput

# Socket is created successfully
# Socket is binded to 23456
# Socket is listening
# Got connection from ('127.0.0.1', 36522)
# Client says: hello from client
