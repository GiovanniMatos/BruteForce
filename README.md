# Brute Force 📧🔓

Este código é útil para simular uma tentativa de invasão para testar a segurança da sua senha do Gmail ou Instagram e até mesmo recuperá-la caso tenha esquecido.<br>
Não use para fins ilegais.

Após smtplib apresentar erros, resolvi utilizar a biblioteca Playwright para automatizar as tentativas de login, usando wordlist.
#
⚠️ <b>Para evitar erros na execução, mantenha o Ambiente Virtual</b><br><br>
<b>Virtualenv Windows</b><br>
Abra o prompt de comando como administrador e execute os comandos abaixo:<br>
```bash
pip install virtualenv
python -m venv venv
.\venv\Scripts\activate
```
<b>Virtualenv Linux</b><br>
```bash
pip install virtualenv
python3 -m venv venv
source venv/bin/activate
```
(venv)
## Instalação
Vá ao diretório desejado para fazer a instalação, ex: Área de Trabalho, e execute os comandos abaixo:<br>

```bash
git clone https://github.com/GiovanniMatos/BruteForce.git
cd BruteForce
pip install playwright
playwright install
```
#
<b>python3 BruteForce.py -h</b><br>
<b>python3 BruteForce.py -w default -u usuario_do_insta --instagram</b><br>
<b>python3 BruteForce.py -w ./sua_wordlist.txt -u email --gmail</b>
#
Após o email/user e wordlist (arquivo .txt contendo possiveis senhas), o navegador será aberto na página de login. <br>
Para cada senha da wordlist, será testada no formulário uma por uma até a senha correspondente ao email/usuário ser encontrada.<br> 
Logo após isso o navegador abrirá a conta pertencente ao email/usuário adicionado.

![270344512-668f2314-5cba-49e9-b12a-8f2a42d80d0d](https://github.com/GiovanniMatos/BruteForce/assets/99231397/83c24574-8fdd-42ba-99c4-a5fc2d1b84b1)
![271019514-6b6f7ce9-9a48-43f3-9b13-8d293fdd78bb](https://github.com/GiovanniMatos/BruteForce/assets/99231397/44e052a4-6e69-4b14-a5a5-e28bac41a2cd)

obs: caso deseje que o programa execute apenas pelo terminal, retire o texto "headless=False" que está entre parênteses e deixe-o vazio "()".<br>
<b>______________________________________________________________________________________________________________</b>

## Brute Force com pyautogui
```bash
pip install pyautogui
```
Adicionada uma pasta com o codigo feito com a lib pyautogui, com o mesmo propósito, deverá usar o arquivo "coordenadas.py" para pegar as coordenadas do campo de usuário (que irá variar de acordo com sua tela).
Após isso, basta definir a sua lista de senhas com o nome "wordlist.txt" e ao executar o "main.py", digite o usuário do instagram a ser testado.<br>
![Sem título](https://github.com/GiovanniMatos/BruteForce/assets/64111507/ef156dd4-2859-4e8c-ada4-29d1982378a5)
