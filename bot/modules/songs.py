import os
import aiohttp
from pyrogram import Client, filters
import youtube-dl
from youtube_search import YoutubeSearch
import requests

from bot import app, dispatcher
from telegram.ext import CommandHandler


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@app.on_message(filters.command(['song']))
def song(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 𝕄𝕖𝕟𝕔𝕒𝕣𝕚 𝕃𝕒𝕘𝕦...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('𝐅𝐨𝐮𝐧𝐝 𝐍𝐨𝐭𝐡𝐢𝐧𝐠. 𝐓𝐫𝐲 𝐂𝐡𝐚𝐧𝐠𝐢𝐧𝐠 𝐓𝐡𝐞 𝐒𝐩𝐞𝐥𝐥𝐢𝐧𝐠 𝐀 𝐋𝐢𝐭𝐭𝐥𝐞 😕')
            return
    except Exception as e:
        m.edit(
            "✖️ 𝐅𝐨𝐮𝐧𝐝 𝐍𝐨𝐭𝐡𝐢𝐧𝐠. 𝐒𝐨𝐫𝐫𝐲.\n\n𝐓𝐫𝐲 𝐀𝐧𝐨𝐭𝐡𝐞𝐫 𝐊𝐞𝐲𝐰𝐨𝐫𝐤 𝐎𝐫 𝐌𝐚𝐲𝐛𝐞 𝐒𝐩𝐞𝐥𝐥 𝐈𝐭 𝐏𝐫𝐨𝐩𝐞𝐫𝐥𝐲.\n\nEg.`/s Faded`"
        )
        print(str(e))
        return
    m.edit("🔎 𝐌𝐞𝐧𝐞𝐦𝐮𝐤𝐚𝐧 𝐥𝐚𝐠𝐮 🎶 ,𝐌𝐨𝐡𝐨𝐧 𝐭𝐮𝐧𝐠𝐠𝐮 📡 𝐔𝐧𝐭𝐮𝐤 𝐛𝐞𝐛𝐞𝐫𝐚𝐩𝐚 𝐝𝐞𝐭𝐢𝐤 [🗣️](https://telegra.ph/file/0bcdc99a139d0ba59c9b6.mp4)")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎙️ 𝐉𝐮𝐝𝐮𝐥 : [{title[:35]}]({link})\n⏰ 𝐃𝐮𝐫𝐚𝐬𝐢 : `{duration}`\n🎥 𝐒𝐮𝐦𝐛𝐞𝐫 : [Youtube](https://youtu.be/3pN0W4KzzNY)\n👤 𝐃𝐢𝐭𝐨𝐧𝐭𝐨𝐧 : `{views}`\n\n🤖 𝐁𝐲: @sepmirrorleech21_bot'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('❌ 𝐄𝐫𝐫𝐨𝐫\n\n Report This Erorr To Fix @uzumaki_naruto4backup ❤️')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
        
        
SONG_HANDLER = CommandHandler("song", song)

dispatcher.add_handler(SONG_HANDLER)
