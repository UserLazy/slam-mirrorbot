import os

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file

from bot import app, dispatcher, telegraph
from telegram.ext import CommandHandler

@app.on_message(filters.command(['tgm']))
async def tgm(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        link = f"https://telegra.ph{response[0]})"
        markup = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Here Your Telegra.ph Link!', url=link)
        ]]
    )
        await message.reply_text(
            text=f"<b>🗣️ Request by {message.from_user.mention}</b>",
            reply_markup=markup,                 
            disable_web_page_preview=True,
        )
        
    finally:
        os.remove(download_location)


@app.on_message(filters.command(['tgt']))
async def tgt(_, message: Message):
    reply = message.reply_to_message

    if not reply or not reply.text:
        return await message.reply("Reply to a text")

    page_name = f"🤖 Bot Sep 21 Publik"
    page = telegraph.create_page(page_name, html_content=reply.text.html)
    url = f"{page['url']}"
    markup = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Here Your Telegra.ph Link!', url=url)
        ]]
    )
    return await message.reply_text(
        text=f"<b>🗣️ Request by {message.from_user.mention}</b>",
        reply_markup=markup,                 
        disable_web_page_preview=True,
    )
       
        
TGM_HANDLER = CommandHandler("tgmn", tgm)
TGT_HANDLER = CommandHandler("tgt", tgt)

dispatcher.add_handler(TGM_HANDLER)
dispatcher.add_handler(TGT_HANDLER)
