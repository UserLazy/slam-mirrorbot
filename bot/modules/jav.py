import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, CommandHandler
from telegram.error import BadRequest

import bot.modules.jav_strings as jav_strings

from bot import dispatcher


def jav_image(update: Update, context: CallbackContext):
    message = update.effective_message
    name = message.reply_to_message.from_user.first_name if message.reply_to_message else message.from_user.first_name
    reply_photo = message.reply_to_message.reply_photo if message.reply_to_message else message.reply_photo
    reply_photo(
        random.choice(jav_strings.JAV_IMG))


JAV_HANDLER = CommandHandler("jav", jav_image)

dispatcher.add_handler(JAV_HANDLER)