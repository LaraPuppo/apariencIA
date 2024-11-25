from pynput.keyboard import Controller

# Crea una instancia del controlador del teclado
keyboard = Controller()

# Simula presionar la tecla 'd'
keyboard.press('d')
keyboard.release('d')

print("Tecla 'D' simulada correctamente.")
