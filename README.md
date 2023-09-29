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

![image](https://github.com/GiovanniMatos/Gmail_BruteForce/assets/99231397/668f2314-5cba-49e9-b12a-8f2a42d80d0d)
![Captura de tela de 2023-09-27 10-27-23](https://github.com/GiovanniMatos/BruteForce/assets/99231397/6b6f7ce9-9a48-43f3-9b13-8d293fdd78bb)
![Captura de tela 2023-09-25 075153](https://github.com/GiovanniMatos/Gmail_BruteForce/assets/99231397/03cacaed-3f06-4d40-a215-b22800e7d795)

obs: caso deseje que o programa execute apenas pelo terminal, retire o texto "headless=False" que está entre parênteses e deixe-o vazio "()".
