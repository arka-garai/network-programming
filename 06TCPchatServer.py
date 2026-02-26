import socket

# Create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server socket created")

host = socket.gethostname()
port = 23456

# Bind socket to host and port
s.bind((host, port))
print("Server binded to port", port)

# Listen for client connections
s.listen()
print("Server is listening...")

while True:
    # Accept connection from client
    c, addr = s.accept()
    print("Connected to client:", addr)

    while True:
        # Receive message from client
        msg = c.recv(1024).decode()
        print("Client:", msg)

        if msg.lower() == "bye":
            break

        # Send reply to client
        reply = input("Server: ")
        c.send(reply.encode())

        if reply.lower() == "bye":
            break

    # Close client connection (iterative nature)
    c.close()
    print("Connection closed")
