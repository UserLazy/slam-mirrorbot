import textwrap

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler


from bot import dispatcher

def menuextrahelp(update, context):
    help_string = '''
  ✙ *𝐄𝐱𝐭𝐫𝐚* ☠️ *:*
 ➻ `/song`*:* Get song from youtube
 ➻ `/tgm`*:* Upload file to telegraph
 ➻ `/tgt`*:* Upload text to telegraph
 ➻ `/whois`*:* get info from user
 ➻ `/webss`*:* Upload screenshot from web
 ➻ `/tts`*:* Convert text to voice
 ➻ `/tl`*:* Use /tl [LANGUAGE_CODE]
 ➻ `/ban`*:* Ban user in Group
 '''
    update.effective_message.reply_photo("https://telegra.ph/file/6b6d2675626aa90f67bce.jpg", help_string, parse_mode=ParseMode.MARKDOWN)


MENUEXTRAHELP_HANDLER = CommandHandler("menuextrahelp", menuextrahelp)

dispatcher.add_handler(MENUEXTRAHELP_HANDLER)