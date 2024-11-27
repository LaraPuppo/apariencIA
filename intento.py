import serial
import pynput.keyboard

# Establecer la conexión serial - IMPORTANTE VER EL COM Y EL NUMERO SIEMPRE EN 9600
arduino = serial.Serial('COM6', 9600)
keyboard = pynput.keyboard.Controller()

while True:
    if arduino.in_waiting > 0:
        command = arduino.readline().decode('utf-8').strip()  # Leer y decodificar el comando
        print(f"Comando recibido: {command}")
        
        if command == "left":
            keyboard.press(pynput.keyboard.Key.left)  # Usar Key.left para la flecha izquierda
            keyboard.release(pynput.keyboard.Key.left)
        elif command == "right":
            keyboard.press(pynput.keyboard.Key.right)  # Usar Key.right para la flecha derecha
            keyboard.release(pynput.keyboard.Key.right)
        elif command == "d":
            keyboard.press('d')  # Para la letra "d"
            keyboard.release('d')
