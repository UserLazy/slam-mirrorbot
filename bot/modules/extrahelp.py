import textwrap

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler


from bot import dispatcher

def extrahelp(update, context):
    help_string = '''
   ✙ 🧨 *Menu Xtra* 💠 *:*
 ➻ /song:Dapatkan lagu dari youtube
 ➻ /tgm:Upload file ke telegraph
 ➻ /tgt:Upload text ke telegraph
 ➻ /whois:Dapatkan info dari pengguna
 ➻ /tts:Ubah text ke suara
 ➻ /tl:Use /tl LANGUAGE_CODE
 ➻ /ban:Ban pengguna dari grup
 ➻ /jav:Dapatkan Gambar JAV idol
 '''
    update.effective_message.reply_photo("https://telegra.ph/file/1d77962382170772a14d1.jpg", help_string, parse_mode=ParseMode.MARKDOWN)


EXTRAHELP_HANDLER = CommandHandler("extrahelp", extrahelp)

dispatcher.add_handler(EXTRAHELP_HANDLER)