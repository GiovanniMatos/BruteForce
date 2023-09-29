from gmail_brute import gmail
from instagram_brute import instagram
from banner import banner
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--instagram', action='store_true', help='Brute Force em Instagram')
parser.add_argument('--gmail', action='store_true', help='Brute Force em Gmail')
parser.add_argument('--wordlist','-w', help='Caminho da wordlist ou "default" para usar a padrão')
parser.add_argument('--user','-u', help='Username ou Email')
args = parser.parse_args()
user = args.user
banner()

if args.wordlist == "default":
    wordlist = open('wordlist.txt', 'r').readlines()
else:
    wordlist_path = args.wordlist
    wordlist = open(wordlist_path, 'r').readlines()

if args.instagram:
    instagram(user, wordlist)
elif args.gmail:
    gmail(user, wordlist)