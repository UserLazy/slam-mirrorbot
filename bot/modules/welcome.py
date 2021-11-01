import os

from pyrogram import Client, filters

from pyrogram.types import Message, User, InlineKeyboardButton, InlineKeyboardMarkup

from bot import app





@app.on_message(filters.new_chat_members)

async def welcome(bot,message):

	chatid = message.chat.id

	markup = InlineKeyboardMarkup(

        [[

        InlineKeyboardButton('🤖 Contact Owner Jika Ingin Berdonasi 👤', url='https://t.me/uzumakinaruto4backup_bot')

        ]]

    )

	await bot.send_message(text=f"1<b> Hai,Apa Kabar? {message.from_user.mention}\n\n 
	(text=f"2<b> Your ID : <code>{message.from_user.id}</code>\n\n
	(text=f"3<b> 👥 Selamat Datang Di Grup , Klik /rules untuk melihat peraturan grup {message.chat.title}\n\n
	(text=f"4<b> Klik /help untuk menampilkan menu perintah</b>", chat_id=chatid, reply_markup=markup)

	

@app.on_message(filters.left_chat_member)

async def goodbye(bot,message):

	chatid= message.chat.id

	await bot.send_message(text=f"1<b> Hati-hati di jalan,titip gorengan & es teh\n\n {message.from_user.mention}\n\n 
	(text=f"2<b> ⏰ Jangan balik lagi 🧨</b>", chat_id=chatid)
