import os
from pyrogram import Client, filters
from googletrans import Translator
from bot import app, dispatcher
from telegram.ext import CommandHandler


@app.on_message(filters.command(["tl"]))
async def left(client,message):
	if (message.reply_to_message):
		try:
			lgcd = message.text.split("/tl")
			lg_cd = lgcd[1].lower().replace(" ", "")
			tr_text = message.reply_to_message.text
			translator = Translator()
			translation = translator.translate(tr_text,dest = lg_cd)
			try:
				for i in list:
					if list[i]==translation.src:
						fromt = i
					if list[i] == translation.dest:
						to = i 
				await message.reply_text(f"Translated from **{fromt.capitalize()}** To **{to.capitalize()}**\n\n```{translation.text}```")
			except:
			   	await message.reply_text(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```")
      			
				
			
		except :
			print("error")
	else:
			 ms = await message.reply_text("You can Use This Command by using reply to message")
			 await ms.delete()

TL_HANDLER = CommandHandler("tl", left)

dispatcher.add_handler(TL_HANDLER)