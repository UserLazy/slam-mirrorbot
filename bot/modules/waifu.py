import requests
import nekos
from PIL import Image
import os

from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram import ParseMode
from telegram.ext import CommandHandler

from bot import dispatcher, updater


def is_user_in_chat(chat: Chat, user_id: int) -> bool:
    member = chat.get_member(user_id)
    return member.status not in ("left", "kicked")
    
    
    
def neko(update, context):
    msg = update.effective_message
    target = "neko"
    msg.reply_photo(nekos.img(target))


def lewd(update, context):
    msg = update.effective_message
    target = "lewd"
    msg.reply_photo(nekos.img(target))
    
    
def wallpaper(update, context):
    msg = update.effective_message
    target = "wallpaper"
    msg.reply_photo(nekos.img(target))
    
    
def tickle(update, context):
     msg = update.effective_message
     target = "tickle"
     msg.reply_video(nekos.img(target))
     
     
def feed(update, context):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))
  
  
def poke(update, context):
    msg = update.effective_message
    target = "poke"
    msg.reply_video(nekos.img(target))
    
    
def hentai(update, context):
    msg = update.effective_message
    target = "hentai"
    msg.reply_photo(nekos.img(target))
    
    
def baka(update, context):
    msg = update.effective_message
    target = "baka"
    msg.reply_video(nekos.img(target))
    
    
    
NEKO_HANDLER = CommandHandler("neko", neko)
LEWD_HANDLER = CommandHandler("lewd", lewd)
WALLPAPER_HANDLER = CommandHandler("wallpaper", wallpaper)
TICKLE_HANDLER = CommandHandler("tickle", tickle)
FEED_HANDLER = CommandHandler("feed", feed)
POKE_HANDLER = CommandHandler("poke", poke)
HENTAI_HANDLER = CommandHandler("hentai", hentai)
BAKA_HANDLER = CommandHandler("baka", baka)


dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(LEWD_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(HENTAI_HANDLER)
dispatcher.add_handler(BAKA_HANDLER)
    
