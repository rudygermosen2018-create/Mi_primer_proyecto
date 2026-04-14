print("Hola, soy el profe Rudy 🔥")
import socket

objetivo = "google.com"
ip = socket.gethostbyname(objetivo)

print("La IP de", objetivo, "es:", ip)