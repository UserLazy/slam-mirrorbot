import os
from pyrogram import Client, filters
from pyrogram.types import Message, User, InlineKeyboardButton, InlineKeyboardMarkup
from bot import app


@app.on_message(filters.new_chat_members)
async def welcome(bot,message):
	chatid = message.chat.id
	markup = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⚙ Contact Owner ⚙', url='https://telegram.me/OdierBambi')
        ]]
    )
	await bot.send_message(text=f"<b> Hallo {message.from_user.mention}\n Your ID: <code>{message.from_user.id}</code>\n Selamat Datang Di Grup {message.chat.title}\n\n Klik /cmdhelp untuk menampilkan menu perintah</b>", chat_id=chatid, reply_markup=markup)
	
@app.on_message(filters.left_chat_member)
async def goodbye(bot,message):
	chatid= message.chat.id
	await bot.send_message(text=f"<b> Selamat jalan\n {message.from_user.mention}\n Semoga harimu menyenangkan😁</b>", chat_id=chatid)