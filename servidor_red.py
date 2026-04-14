import socket
import json
import threading # Importamos threading

def manejar_cliente(client, addr):
    """Función que corre en un hilo separado por cada cliente."""
    print(f"[+] Nueva conexión desde: {addr}")
    try:
        data = client.recv(1024).decode('utf-8')
        if data:
            payload = json.loads(data)
            tipo = payload.get("type", "PING")
            
            # Lógica de filtrado
            if tipo == "ATTACK":
                resultado = {"status": "BLOQUEADO", "color": "RED"}
            else:
                resultado = {"status": "ACEPTADO", "color": "GREEN"}
            
            client.send(json.dumps(resultado).encode('utf-8'))
    except Exception as e:
        print(f"[!] Error procesando cliente {addr}: {e}")
    finally:
        client.close()
        print(f"[-] Conexión cerrada con {addr}")

def iniciar_servidor(puerto):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', puerto))
    server.listen(5)
    print(f"[*] Servidor escuchando en puerto {puerto}...")

    while True:
        client, addr = server.accept()
        # Creamos un hilo para cada cliente que se conecta
        hilo = threading.Thread(target=manejar_cliente, args=(client, addr))
        hilo.start() # Iniciamos el hilo
        print(f"[!] Hilos activos: {threading.active_count() - 1}")

if __name__ == "__main__":
    iniciar_servidor(9999)