import requests
from tbot import TBot

TOKEN = '827940689:AAFH0jE2qa6wvid-3my020PSv1sRO_F5bDM'
BOT_URL = f'https://api.telegram.org/bot{TOKEN}/'
HOST = '94.237.74.114'
URL = f'/telegram/{TOKEN}'
WEBHOOK_URL = f'{HOST}/{URL}'

bot = TBot(TOKEN)

x = lambda: requests.get(BOT_URL + 'setWebhook', json={'url': WEBHOOK_URL})