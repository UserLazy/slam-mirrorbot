import pyrogram
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import User, Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.helper.omdb import get_movie_info
from bot import app


            
@app.on_message(filters.command(["movie"]))
async def imdbcmd(client, message):
    movie_name = message.text.split(" ", 1)[1]
    movie_info = get_movie_info(movie_name)
    if movie_info:
                  poster = movie_info["pimage"]
                  urlid = movie_info['imdb_id']
                  buttons=[[InlineKeyboardButton('🎟 𝖨𝖬𝖣𝖻', url=f"https://www.imdb.com/title/{urlid}")]] 
                                                     
                  text=f"""📀 𝖳𝗂𝗍𝗅𝖾 : <b>{movie_info['title']}</b>
                            
⏱️ 𝖱𝗎𝗇𝗍𝗂𝗆𝖾 : <b>{movie_info['duration']}</b>
🌟 𝖱𝖺𝗍𝗂𝗇𝗀 : <b>{movie_info['imdb_rating']}/10</b>
🗳️ 𝖵𝗈𝗍𝖾𝗌 : <b>{movie_info['votes']}</b>

📆 𝖱𝖾𝗅𝖾𝖺𝗌𝖾 : <b>{movie_info['release']}</b>
🎭 𝖦𝖾𝗇𝗋𝖾 : <b>{movie_info['genre']}</b>
🎙 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <b>{movie_info['language']}</b>
🌐 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 : <b>{movie_info['country']}</b>

🎥 𝖣𝗂𝗋𝖾𝖼𝗍𝗈𝗋𝗌 : <b>{movie_info['director']}</b>
📝 𝖶𝗋𝗂𝗍𝖾𝗋𝗌 : <b>{movie_info['writer']}</b>
🔆 𝖲𝗍𝖺𝗋𝗌 : <b>{movie_info['actors']}</b>

🗒 𝖯𝗅𝗈𝗍 : <code>{movie_info['plot']}</code>"""
                  
                  if poster.startswith("https"):
                                                m = await message.reply_text("𝖥𝗂𝗇𝖽𝗂𝗇𝗀 𝖣𝖾𝗍𝖺𝗂𝗅𝗌..")
                                                await message.reply_photo(photo=poster.replace("_SX300","_"), caption=text, reply_markup=InlineKeyboardMarkup(buttons))
                                                await m.delete()
                  else:
                       m = await message.reply_text("𝖲𝗈𝗋𝗋𝗒,\n𝖨 𝖢𝖺𝗇'𝗍 𝖥𝗂𝗇𝖽 𝖯𝗈𝗌𝗍𝖾𝗋𝗌.\n𝖲𝖾𝗇𝖽𝗂𝗇𝗀 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖣𝖾𝗍𝖺𝗂𝗅𝗌..")
                       await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
                       await sleep(4)
                       await m.delete()
    else:
        omdbbuttons=[[InlineKeyboardButton('🔍 𝖲𝖾𝖺𝗋𝖼𝗁 𝖮𝗇 𝖦𝗈𝗈𝗀𝗅𝖾.', url=f'https://google.com/search?q={movie_name.replace(" ","+")}')]]
        await message.reply_text(text="𝖢𝗈𝗎𝗅𝖽𝗇'𝗍 𝖥𝖾𝗍𝖼𝗁 𝖣𝖾𝗍𝖺𝗂𝗅𝗌\n𝖳𝗋𝗒 𝖳𝗈 𝖢𝗁𝖾𝖼𝗄 𝖸𝗈𝗎𝗋 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀.", reply_markup=InlineKeyboardMarkup(omdbbuttons))       


