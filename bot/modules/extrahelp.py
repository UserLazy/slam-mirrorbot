import textwrap
import requests

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler

from bot import dispatcher

def extrahelp(update, context):
    help_string = '''
   ✙ 🧨 *Menu Xtra* 💠 *:*
 ➻ /song: Get song from youtube
 ➻ /telegraph: Upload file to telegraph
 ➻ /tgt: Upload text to telegraph
 ➻ /whois: get info from user
 ➻ /webss: Upload screenshot from web
 ➻ /tts: Convert text to voice
 ➻ /tl: Use /tl LANGUAGE_CODE
 ➻ /paste: Paste text
 ➻ /ban: Ban user in group
 ➻ /jav: Get jav idol image
 ➻ /cat: Get cat image
 '''

EXTRAHELP_HANDLER = CommandHandler("extrahelp", extrahelp)

dispatcher.add_handler(EXTRAHELP_HANDLER)
