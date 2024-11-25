import serial
import pynput.keyboard
import time

# Configura el puerto serial (ajusta COM3 si tu puerto es diferente)
puerto_serial = 'COM3'  # Cambia este valor si tu puerto es otro

# Abre el puerto serial
arduino = serial.Serial(puerto_serial, 9600, timeout=1)

# Configura el controlador de teclado
keyboard = pynput.keyboard.Controller()

# Esperar un poco para establecer la conexión
time.sleep(1)

print("Esperando la tecla...")

while True:
    # Lee los datos enviados por Arduino
    data = arduino.readline().decode('utf-8').strip()  # Lee una línea y elimina espacios

    # Verifica si se ha recibido la letra 'D'
    if data == 'D':
        print("Botón presionado! Simulando la tecla 'D'.")
        keyboard.press('d')  # Simula la pulsación de la tecla 'd'
        keyboard.release('d')  # Libera la tecla
    elif data == ' ':
        print("Botón no presionado.")
    
    time.sleep(0.1)  # Pausa para evitar sobrecargar el loop
