from bot import app, dispatcher
from pyrogram import filters
from telegram.ext import CommandHandler


@app.on_message(filters.command(['id']))
def ids(_,message):
  reply = message.reply_to_message
  if reply:
    message.reply_text(f"**Your ID**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ID**: `{reply.from_user.id}`\n**Chat ID**: `{message.chat.id}`")
  else:
    message.reply(f"**Your id**: `{message.from_user.id}`\n**chat id**: `{message.chat.id}`")

ID_HANDLER = CommandHandler("id", ids)

dispatcher.add_handler(ID_HANDLER)