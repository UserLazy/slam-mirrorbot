import httpx

from pyrogram import Client, filters
from pyrogram.types import Message

from bot import app, dispatcher
from telegram.ext import CommandHandler

@app.on_message(filters.command(['cat']))
async def cat(c: Client, m: Message):
    http = httpx.AsyncClient(http2=True)
    r = await http.get("https://api.thecatapi.com/v1/images/search")
    rj = r.json()
    
    await m.reply_photo(rj[0]["url"], caption=f"meow")

       
CAT_HANDLER = CommandHandler("cat", cat)

dispatcher.add_handler(CAT_HANDLER)