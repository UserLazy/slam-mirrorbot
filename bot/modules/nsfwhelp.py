import textwrap

from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler


from bot import dispatcher


def nsfwhelp(update, context):
    help_string = '''
  • Menu Anu 18+ :
❍ `/neko`
❍ `/feet`
❍ `/yuri`
❍ `/trap`
❍ `/futanari`
❍ `/hololewd`
❍ `/lewdkemo`
❍ `/sologif`
❍ `/cumgif`
❍ `/erokemo`
❍ `/lesbian`
❍ `/lewdk`
❍ `/ngif`
❍ `/tickle`
❍ `/lewd`
❍ `/feed`
❍ `/eroyuri`
❍ `/eron`
❍ `/cum`
❍ `/bjgif`
❍ `/bj`
❍ `/nekonsfw`
❍ `/solo`
❍ `/kemonomimi`
❍ `/avatarlewd`
❍ `/gasm`
❍ `/poke`
❍ `/anal`
❍ `/hentai`
❍ `/avatar`
❍ `/erofeet`
❍ `/holo`l
❍ `/tits`
❍ `/pussygif`
❍ `/holoero`
❍ `/pussy`
❍ `/hentaigif`
❍ `/classic`
❍ `/kuni`
❍ `/waifu`
❍ `/kiss`
❍ `/femdom`
❍ `/cuddle`
❍ `/erok`
❍ `/foxgirl`
❍ `/titsgif`
❍ `/ero`
❍ `/smug`
❍ `/baka`
❍ `/wallpaper`
'''
    update.effective_message.reply_photo("https://telegra.ph/file/1d77962382170772a14d1.jpg", help_string, parse_mode=ParseMode.MARKDOWN)


NSFWHELP_HANDLER = CommandHandler("nsfwhelp", nsfwhelp)

dispatcher.add_handler(NSFWHELP_HANDLER)
