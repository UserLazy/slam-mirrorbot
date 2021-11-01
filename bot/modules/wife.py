import httpx

from pyrogram import Client, filters
from pyrogram.types import Message import Users

from bot import app, dispatcher
from telegram.ext import CommandHandler

@app.on_message(filters.command(['wife']))
async def waifu(c: Client, m: Message):

     http = httpx.AsyncClient(http2=True)
     r = await http.get("https://api.waifu.pics/sfw/waifu")
     rj = r.json()

     await m.reply_photo(rj["url"], caption=f"Ini waifumu 💙💙💙💙💙@{message.from_user.username}")


WIFE_HANDLER = CommandHandler("wife", waifu)

dispatcher.add_handler(WIFE_HANDLER)
