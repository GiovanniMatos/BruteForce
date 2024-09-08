# Brute Force 📧🔓

This code is useful for simulating a password attack, testing the security of your Gmail or Instagram passwords, and even recovering them if you've forgotten them. also to enumerate routes (/directory) in web applications.<br>
Don't use for illegal purposes.

After errors in smtplib (python lib), I decided to use lib Playwright to automate login attempts using wordlists. 
#
⚠️ <b>To avoid execution errors, keep the virtual environment</b><br><br>
<b>Virtualenv Windows</b><br>
Open command prompt and run the commands below<br>
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
## Installation
Go to the path to install, e.g. /Desktop and run the commands below:<br>

```bash
git clone https://github.com/GiovanniMatos/BruteForce.git
cd BruteForce
pip install -r requirements.txt
playwright install firefox
```
# Usage: 
<b>python3 main.py -h</b><br>
<b>python3 main.py -w default -u insta_user --instagram</b><br>
<b>python3 main.py -w ./your_wordlist.txt -u email --gmail</b><br>
<b>python3 main.py -w ./your_wordlist.txt -url https://github.com --routes</b>
#
After adding email/user and wordlist (.txt file with possible passwords) the browser will open to the login page. <br>
For password in wordlist, it will be tried one by one until you find the correct password.<br> 
After that, the browser will open to the user's account page.

![270344512-668f2314-5cba-49e9-b12a-8f2a42d80d0d](https://github.com/GiovanniMatos/BruteForce/assets/99231397/83c24574-8fdd-42ba-99c4-a5fc2d1b84b1)
![271019514-6b6f7ce9-9a48-43f3-9b13-8d293fdd78bb](https://github.com/GiovanniMatos/BruteForce/assets/99231397/44e052a4-6e69-4b14-a5a5-e28bac41a2cd)

Note: if you want the program to run only through the terminal, remove the text "headless=False" that is between parentheses and leave it empty "()".<br>
<b>______________________________________________________________________________________________________________</b>

## Brute Force with pyautogui
```bash
pip install pyautogui
```
Added a folder with the code made with the pyautogui lib for the same purpose, you must use the file "coordenadas.py" to get the coordinates of the user field (which will vary according to your screen).
After that, simply define your list of passwords with the name "wordlist.txt" and when running "main.py", enter the Instagram user to be tested in the terminal.<br>
![Sem título](https://github.com/GiovanniMatos/BruteForce/assets/64111507/ef156dd4-2859-4e8c-ada4-29d1982378a5)
