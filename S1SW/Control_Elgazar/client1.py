import socket

HOST, PORT = "localhost", 9999


# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	# Connect to server.
	sock.connect((HOST, PORT))
	data = " "
	while True:
		data = input()
		if data == 'q': break

		# Send data.
		sock.sendall(bytes(data + "\n", "utf-8"))

		# Receive data from the server and shut down.
		received = str(sock.recv(4096), "utf-8")
		print("Sent:     {}".format(data))
		print("Received: {}".format(received))