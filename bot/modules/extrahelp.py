import textwrap

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler


from bot import dispatcher

def extrahelp(update, context):
    help_string = '''
  ✙ 📛 *𝐄𝐱𝐭𝐫𝐚* 📛 *:*
 ➻ `/movie`*:* for search film informations from imdb
 ➻ `/paste`*:* Paste text to pasty
 ➻ `/song`*:* Get song from youtube
 ➻ `/tgm`*:* Upload File to Telegraph
 ➻ `/tgt`*:* Upload Text to Telegraph
 ➻ `/tts`*:* Convert text to voice
 ➻ `/tl`*:* Use /tl [LANGUAGE_CODE]
 ➻ `/whois`*:* get info from user
 ➻ `/webss`*:* Upload screenshot from web
 '''
    update.effective_message.reply_photo("https://telegra.ph/file/1d77962382170772a14d1.jpg", help_string, parse_mode=ParseMode.MARKDOWN)


MENUEXTRA_HANDLER = CommandHandler("menuextra", extrahelp)

dispatcher.add_handler(MENUEXTRA_HANDLER)
