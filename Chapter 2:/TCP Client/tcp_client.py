import socket

target_host = "localhost"
target_port = 9998

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET= Standard IPv4 addresss,
# SOCK_STREAM=TCP Client

# conectamos al cliente
client.connect((target_host, target_port))

# send data - convertimos el string a bytes
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(request.encode())

# recibir respuesta - decodificamos los bytes a string
response = client.recv(4096)
print(response.decode())

client.close()