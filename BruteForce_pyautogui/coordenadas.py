import pyautogui
import time

# terá 3 segundos para colocar o cursor do mouse no local que deseja pegar as coordenadas
time.sleep(3)
x, y = pyautogui.position()

print(f"Coordenada X: {x}")
print(f"Coordenada Y: {y}")