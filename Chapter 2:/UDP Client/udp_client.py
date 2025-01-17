import socket

target_host = "127.0.0.1"
target_port = 9997

    # creamos objeto de enchufe
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM=UDP connection

    # mandamos información
client.sendto(b"AAABBBCCC", (target_host,target_port))

    # recibir información
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()

print("Done.")
