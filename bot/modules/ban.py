import pyrogram
import os
from pyrogram import filters
from pyrogram.types import Message, User

from bot import app, dispatcher
from telegram.ext import CommandHandler

@app.on_message(filters.command(["ban"]))
async def ban(bot, message):
    chatid = message.chat.id
    if message.reply_to_message:
        admins_list = await bot.get_chat_members(
            chat_id=chatid, filter="administrators"
        )
        admins = []
        for admin in admins_list:
            id = admin.user.id
            admins.append(id)
        userid = message.from_user.id
        if userid in admins:
            user_to_ban = message.reply_to_message.from_user.id
            if user_to_ban in admins:
                await message.reply(text="📛 Dia admin digrup ini,dia punya angelcard")
            else:
                try:
                    await bot.kick_chat_member(chat_id=chatid, user_id=user_to_ban)
                    await message.reply_text(
                         f"<b>Banned User {message.reply_to_message.from_user.mention}</b>\n <b>UserID</b>: <code>{message.from_user.id}</code>"
                    )
                except Exception as error:
                    await message.reply_text(f"{error}")
        else:
            await message.reply_text("⛔️ Kamu bukan admin di sini,apa yang kamu lakukan?")
            return
 
@app.on_message(filters.command(["unban"]))

async def unban(bot, message):

    chatid = message.chat.id

    if message.reply_to_message:

        admins_list = await bot.get_chat_members(

            chat_id=chatid, filter="administrators"

        )

        admins = []

        for admin in admins_list:

            id = admin.user.id

            admins.append(id)

        userid = message.from_user.id

        if userid in admins:

            user_to_unban = message.reply_to_message.from_user.id

            if user_to_unban in admins:

                await message.reply(text="📛 Dia admin digrup ini,tidak mungkin bisa diban")

            else:

                try:

                    await bot.unban_chat_member(chat_id=chatid, user_id=user_to_unban)

                    await message.reply_text(

                        f"<b>Unbanned User {message.reply_to_message.from_user.mention}</b>\n <b>UserID</b>: <code>{message.from_user.id}</code>"

                    )

                except Exception as error:

                    await message.reply_text(f"{error}")

        else:

            await message.reply_text("Anda Tidak memiliki hak untuk perintah ini..")

            return


BAN_HANDLER = CommandHandler("ban", ban)
UNBAN_HANDLER = CommandHandler("unban", unban)

dispatcher.add_handler(BAN_HANDLER)
dispatcher.add_handler(UNBAN_HANDLER)
