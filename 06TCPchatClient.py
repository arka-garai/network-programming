import socket

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 23456

# Connect to server
s.connect((host, port))
print("Connected to server")

while True:
    # Send message to server
    msg = input("Client: ")
    s.send(msg.encode())

    if msg.lower() == "bye":
        break

    # Receive reply from server
    reply = s.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == "bye":
        break

# Close connection
s.close()
