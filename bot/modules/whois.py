import os

from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from bot.helper.extract_user import extract_user
from bot.helper.last_online_hlpr import last_online

import time

from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message, User
from bot import app

@app.on_message(filters.command(['whois']))
async def who_is(client, message):
    
    # https://github.com/SpEcHiDe/PyroGramBot/blob/master/pyrobot/plugins/admemes/whois.py#L19
    status_message = await message.reply_text(
        "🔍 Info sedang di salin , mohon tunggu"
    )
    await status_message.edit(
        "`🌐 Memproses mengunggah info profil`"
    )
    from_user = None
    from_user_id, _ = extract_user(message)
    try:
        from_user = await client.get_users(from_user_id)
    except Exception as error:
        await status_message.edit(str(error))
        return
    if from_user is None:
        await status_message.edit("no valid user_id / message specified")
    else:
        message_out_str = ""
        message_out_str += f"<b>🔍 User ID :</b> <code>{from_user.id}</code>\n"
        username = from_user.username or "<b>None</b>"
        message_out_str += f"<b>👾 User Name :</b> @{username}\n\n"
        message_out_str += f"<b>👤 First Name :</b> {from_user.first_name}\n"
        last_name = from_user.last_name or "<b>None</b>"
        message_out_str += f"<b>✅ Last Name :</b> {last_name}\n\n"
        message_out_str += f"<b>⏱ Last Online :</b> {from_user.status}\n\n"
        dc_id = from_user.dc_id or "[User Doesnt Have A Valid DP]"
        message_out_str += f"<b>🌐 Data Centre :</b> <code>{dc_id}</code>\n"
        message_out_str += f"<b>🔗 User 𝖫𝗂𝗇𝗄 :</b> <a href='tg://user?id={from_user.id}'><b>Di Sini</b></a>\n"
        if message.chat.type in (("supergroup", "channel")):
            try:
                chat_member_p = await message.chat.get_member(from_user.id)
                joined_date = datetime.fromtimestamp(
                    chat_member_p.joined_date or time.time()
                ).strftime("%d %b %Y at %I:%M %p")
                message_out_str += (
                    "<b>👥 Bergabung Di Grup :</b> <code>"
                    f"{joined_date}"
                    "</code>\n"
                )
            except UserNotParticipant:
                pass
        chat_photo = from_user.photo
        if chat_photo:
            local_user_photo = await client.download_media(
                message=chat_photo.big_file_id
            )
             uname = from_user.username
             link = f"https://telegram.me/{uname}"
             button = [[
                 InlineKeyboardButton('❌ Tutup', callback_data='close'),
                 InlineKeyboardButton('↪️ Kirim pesan', url=link)
                 ]]
            reply_markup = InlineKeyboardMarkup(button)

            await message.reply_photo(
                photo=local_user_photo,
                quote=True,
                reply_markup=reply_markup,
                caption=message_out_str,
                parse_mode="html",
                disable_notification=True
            )
            os.remove(local_user_photo)
            
        else:
             await message.reply_photo(
                photo=local_user_photo,
                quote=True,
                reply_markup=reply_markup,
                caption=message_out_str,
                parse_mode="html",
                disable_notification=True
            )
             uname = from_user.username
             link = f"https://telegram.me/{uname}"
             button = [[
                 InlineKeyboardButton('❌ Tutup', callback_data='close'),
                 InlineKeyboardButton('↪️ Kirim pesan', url=link)
            ]]
            reply_markup = InlineKeyboardMarkup(button)

            await message.reply_text(
                text=message_out_str,
                quote=True,
                reply_markup=reply_markup,
                parse_mode="html",
                disable_notification=True
            )
        await status_message.delete()

@app.on_callback_query() # callbackQuery()
async def cbclose(bot, update):  
    if update.data == "close":
        
        await status_message.delete()
