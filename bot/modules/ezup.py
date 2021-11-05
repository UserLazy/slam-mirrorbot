import os

from pyrogram import filters
from pyrogram.types import Message
from telegraph import upload_file

from bot import app, dispatcher, telegraph
from telegram.ext import CommandHandler

@app.on_message(filters.command(['telegraph']))
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
        await message.reply(
            f"[Here Your Telegra.ph Link!](https://telegra.ph{response[0]})",                  
            disable_web_page_preview=True,
        )
        
    finally:
        os.remove(download_location)


@app.on_message(filters.command(['telegraphtext']))
async def tgt(_, message: Message):
    reply = message.reply_to_message

    if not reply or not reply.text:
        return await message.reply("Balas ke pesan teks😌")

    page_name = f"Robot Gledek⚡"
    page = telegraph.create_page(page_name, html_content=reply.text.html)
    return await message.reply(
        f"[Here Your Telegra.ph Link!]({page['url']})",
        disable_web_page_preview=True,
    )
       
        
TELEGRAPH_HANDLER = CommandHandler("telegraph", tgm)
TELEGRAPHTEXT_HANDLER = CommandHandler("telegraphtext", tgt)

dispatcher.add_handler(TELEGRAPH_HANDLER)
dispatcher.add_handler(TELEGRAPHTEXT_HANDLER)