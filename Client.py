import socket
import json

def enviar_mensaje(tipo):
    # Conectamos al servidor local
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('127.0.0.1', 9999))
    
    # Preparamos el mensaje
    mensaje = {"type": tipo}
    cliente.send(json.dumps(mensaje).encode('utf-8'))
    
    # Recibimos la respuesta
    respuesta = cliente.recv(1024).decode('utf-8')
    print(f"Respuesta del servidor: {respuesta}")
    
    cliente.close()

if __name__ == "__main__":
    # Prueba 1: Enviar un ataque
    print("Enviando ATTACK...")
    enviar_mensaje("ATTACK")
    
    # Prueba 2: Enviar un ping normal
    print("\nEnviando PING...")
    enviar_mensaje("PING")