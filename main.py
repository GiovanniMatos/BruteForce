from gmail_brute import gmail
from instagram_brute import instagram
from banner import banner
from dirbrute import routes
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--instagram', action='store_true', help='Instagram Brute Force')
parser.add_argument('--gmail', action='store_true', help='Gmail Brute Force')
parser.add_argument('--wordlist','-w', help='Wordlist Path or "default" for default wordlist')
parser.add_argument('--user','-u', help='Username, Email')
parser.add_argument('--url','-url', help='Url routes enumeration')
parser.add_argument('--routes', action='store_true', help='Web Application directory enumeration')
args = parser.parse_args()
enum_routes = args.routes
user = args.user
url = args.url
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

# para diretorios
if enum_routes and url:
    if args.wordlist == "default":
        wordlist = open('common.txt', 'r').readlines()
    else:
        wordlist_path = args.wordlist
        wordlist = open(wordlist_path, 'r').readlines()
    routes(url, wordlist)
