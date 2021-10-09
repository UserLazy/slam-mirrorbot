import html
import random
import time
import requests

from telegram import ParseMode, Update, ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext, CommandHandler
from telegram.utils.helpers import mention_html
from telegram.error import BadRequest

import bot.modules.fun_strings as fun_strings
from bot import dispatcher


GIF_ID = 'CgACAgUAAx0EVmwfqQACElhfo3yZv1njCC11INcQSAi4UlN8vwACqwADg_8wVeGSv41OYU6zHgQ'

PHOTO = 'https://telegra.ph/file/1d77962382170772a14d1.jpg'


def runs(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))



def truth(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.TRUTH_STRINGS))


def insult(update: Update, _):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(random.choice(fun_strings.INSULT_STRINGS))


def dare(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.DARE_STRINGS))


def roll(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(range(1, 7)))



def toss(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(fun_strings.TOSS))



def shrug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    reply_text(r"¯\_(ツ)_/¯")



def rlg(update: Update, context: CallbackContext):
    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)



def decide(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.DECIDE))



def table(update: Update, context: CallbackContext):
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text(random.choice(fun_strings.TABLE))


def funhelp(update, context):
    help_string = '''
  ✙ 🤖 *Fitur saat bosan* 🤪 *:*
 ➻ `/runs`*:* Reply a random string from an array of replies
 ➻ `/shrug`*:* Get shrug XD
 ➻ `/table`*:* Get flip/unflip :v
 ➻ `/rlg`*:* Join ears,nose,mouth and create an emo ;-;
 ➻ `/weebify <text>`*:* Returns a weebified text
 ➻ `/textbulet <text>`*:* Returns a bulet text
  ═ ═ ═ ═ ═ ═ ═ ═ ═ ═
 ✙ 🤖 *Games* 👾 *:*
 ➻ `/truth`*:* Get ready to reveal a surprising truth🤫
 ➻ `/dare`*:* A dare is on way 😈
 ➻ `/insult`*:* Insult the person
 ➻ `/decide`*:* Randomly answers yes/no/maybe/idk
 ➻ `/toss`*:* Tosses A coin
 ➻ `/roll`*:* Roll a dice & get you a number
  ═ ═ ═ ═ ═ ═ ═ ═ ═ ═
 ✙ 🧨 *Fitur Xtra* 💠 *:*
 ➻ `/song`*:* Get song from youtube
 ➻ `/tgm`*:* Upload file to telegraph
 ➻ `/tgt`*:* Upload text to telegraph
 ➻ `/kata`*:* Dapatkan text keren
 '''
    update.effective_message.reply_photo("https://telegra.ph/file/6b6d2675626aa90f67bce.jpg", help_string, parse_mode=ParseMode.MARKDOWN)


RUNS_HANDLER = CommandHandler("runs", runs)
TRUTH_HANDLER = CommandHandler("truth", truth)
DARE_HANDLER = CommandHandler("dare", dare)
INSULT_HANDLER = CommandHandler("insult", insult)
ROLL_HANDLER = CommandHandler("roll", roll)
TOSS_HANDLER = CommandHandler("toss", toss)
SHRUG_HANDLER = CommandHandler("shrug", shrug)
RLG_HANDLER = CommandHandler("rlg", rlg)
DECIDE_HANDLER = CommandHandler("decide", decide)
TABLE_HANDLER = CommandHandler("table", table)
FUNHELP_HANDLER = CommandHandler("funyhelp", funhelp)


dispatcher.add_handler(INSULT_HANDLER)
dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(FUNHELP_HANDLER)
