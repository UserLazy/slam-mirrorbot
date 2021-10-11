import shutil, psutil
import signal
import os
import asyncio

from pyrogram import idle
from sys import executable

from telegram import ParseMode
from telegram.ext import CommandHandler
from telegraph import Telegraph
from wserver import start_server_async
from bot import bot, app, dispatcher, updater, botStartTime, IGNORE_PENDING_REQUESTS, IS_VPS, PORT, alive, web, OWNER_ID, AUTHORIZED_CHATS, telegraph_token
from bot.helper.ext_utils import fs_utils
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.ext_utils.bot_utils import get_readable_file_size, get_readable_time
from .helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper import button_build
from .modules import authorize, list, cancel_mirror, mirror_status, mirror, clone, watch, shell, eval, torrent_search, delete, speedtest, count, leech_settings, anime, weebify, stickers, animequotes, fun, nhentai, sitesearch, songs, telegraph, text, waifu, nsfw


def stats(update, context):
    currentTime = get_readable_time(time.time() - botStartTime)
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    stats = f'<b>💻 Waktu Aktif Bot ⏱ :</b> <code>{currentTime}</code>\n' \
            f'<b>🖥 Total Kapasitas Disk 🖥 :</b> <code>{total}</code>\n' \
            f'<b>💿 Penggunaan :</b> <code>{used}</code>\n' \
            f'<b>💾 Sisa :</b> <code>{free}</code>\n\n' \
            f'<b>🔺 Upload  :</b> <code>{sent}</code>\n' \
            f'<b>🔻 Download :</b> <code>{recv}</code>\n\n' \
            f'<b>💻 CPU :</b> <code>{cpuUsage}%</code> ' \
            f'<b>🧭 RAM :</b> <code>{memory}%</code> ' \
            f'<b>💿 DISK :</b> <code>{disk}%</code>\n' \
            f'<b>🤖 Name : @sepmirrorleech21_bot</b>'
    sendMessage(stats, context.bot, update)


def start(update, context):
    buttons = button_build.ButtonMaker()
    buttons.buildbutton("👤 Ouwner✅ -> ", "https://t.me/uzumaki_naruto4backup")
    buttons.buildbutton("🔰 Donate -> Clik Here ↗️", "https://telegra.ph/Donate-Here-09-25")
    reply_markup = InlineKeyboardMarkup(buttons.build_menu(2))
    if CustomFilters.authorized_user(update) or CustomFilters.authorized_chat(update):
        start_string = f'''
This bot can mirror all your links to Google Drive!
Type /{BotCommands.HelpCommand} to get a list of available commands
'''
        sendMarkup(start_string, context.bot, update, reply_markup)
    else:
        sendMarkup(
            'Oops! not a Authorized user.\nPlease deploy your own <b>slam-mirrorbot</b>.',
            context.bot,
            update,
            reply_markup,
        )


def restart(update, context):
    restart_message = sendMessage("Restarting, Please wait!", context.bot, update)
    # Save restart message object in order to reply to it after restarting
    with open(".restartmsg", "w") as f:
        f.truncate(0)
        f.write(f"{restart_message.chat.id}\n{restart_message.message_id}\n")
    fs_utils.clean_all()
    alive.terminate()
    web.terminate()
    os.execl(executable, executable, "-m", "bot")


def ping(update, context):
    start_time = int(round(time.time() * 1000))
    reply = sendMessage("Starting Ping", context.bot, update)
    end_time = int(round(time.time() * 1000))
    editMessage(f'{end_time - start_time} ms', reply)


def log(update, context):
    sendLogFile(context.bot, update)


help_string_telegraph = f'''<br>
<b>/{BotCommands.HelpCommand}</b>: To get help menu for this bot (Sorry I Use Indonesian Language)
<br><br>
<b>/{BotCommands.MirrorCommand}</b> [download_url][magnet_link]: Mulai mirroring tautan ke Google Drive.
<br><br>
<b>/{BotCommands.TarMirrorCommand}</b> [download_url][magnet_link]: Mulai mirroring & upload versi unduhan (.tar) dari unduhan
<br><br>
<b>/{BotCommands.ZipMirrorCommand}</b> [download_url][magnet_link]: Mulai mirroring & upload versi arsip (.zip) dari unduhan
<br><br>
<b>/{BotCommands.UnzipMirrorCommand}</b> [download_url][magnet_link]: Mulai mirroring file yang berformat arsip (.tar/.zip) , ekstrak ke Google Drive
<br><br>
<b>/{BotCommands.QbMirrorCommand}</b> [magnet_link]: Mulai Mencerminkan menggunakan qBittorrent, Use <b>/{BotCommands.QbMirrorCommand} s</b> untuk memilih file sebelum mengunduh
<br><br>
<b>/{BotCommands.QbTarMirrorCommand}</b> [magnet_link]: Mulai mirroring menggunakan qBittorrent & upload versi unduhan (.tar) dari unduhan
<br><br>
<b>/{BotCommands.QbZipMirrorCommand}</b> [magnet_link]: Mulai mirroring menggunakan qBittorrent & upload versi arsip (.zip) dari unduhan
<br><br>
<b>/{BotCommands.QbUnzipMirrorCommand}</b> [magnet_link]: Mulai mirroring menggunakan qBittorrent & jika file yang diunduh yang berformat arsip (.tar/.zip) , ekstrak ke Google Drive
<br><br>
<b>/{BotCommands.LeechCommand}</b> [download_url][magnet_link]: Mulai upload ke Telegram, Use <b>/{BotCommands.LeechCommand} s</b> untuk pilih file sebelum upload
<br><br>
<b>/{BotCommands.TarLeechCommand}</b> [download_url][magnet_link]:  Mulai upload ke Telegram dengan format (.tar)
<br><br>
<b>/{BotCommands.ZipLeechCommand}</b> [download_url][magnet_link]: Mulai upload ke Telegram dengan format (.zip)
<br><br>
<b>/{BotCommands.UnzipLeechCommand}</b> [download_url][magnet_link]: Mulai mengekstrak jika formatnya (.tar / .zip), lalu menguploadnya ke Telegeram
<br><br>
<b>/{BotCommands.QbLeechCommand}</b> [magnet_link]: Start leeching to Telegram using qBittorrent, Use <b>/{BotCommands.QbLeechCommand} s</b> to select files before leeching
<br><br>
<b>/{BotCommands.QbTarLeechCommand}</b> [magnet_link]: Start leeching to Telegram using qBittorrent and upload it as (.tar)
<br><br>
<b>/{BotCommands.QbZipLeechCommand}</b> [magnet_link]: Start leeching to Telegram using qBittorrent and upload it as (.zip)
<br><br>
<b>/{BotCommands.QbUnzipLeechCommand}</b> [magnet_link]: Start leeching to Telegram using qBittorrent and if downloaded file is any archive, extracts it to Telegram
<br><br>
<b>/{BotCommands.CloneCommand}</b> [drive_url]: Ganda file/folder ke Google Drive (Refensi jika link yang anda tuju kehabisan limit pada saat anda buka)
<br><br>
<b>/{BotCommands.CountCommand}</b> [drive_url]: Hitung file/folder Dari Link Google Drive
<br><br>
<b>/{BotCommands.DeleteCommand}</b> [drive_url]: Hapus file Dari Google Drive Bot Ini (Only Owner & Sudo)
<br><br>
<b>/{BotCommands.WatchCommand}</b> [youtube-dl supported link]: Mirror through youtube-dl. Click <b>/{BotCommands.WatchCommand}</b> for more help
<br><br>
<b>/{BotCommands.TarWatchCommand}</b> [youtube-dl supported link]: Mirror through youtube-dl and tar before uploading
<br><br>
<b>/{BotCommands.ZipWatchCommand}</b> [youtube-dl supported link]: Mirror through youtube-dl and zip before uploading
<br><br>
<b>/{BotCommands.LeechWatchCommand}</b> [youtube-dl supported link]: Leech through youtube-dl 
<br><br>
<b>/{BotCommands.LeechTarWatchCommand}</b> [youtube-dl supported link]: Leech through youtube-dl and tar before uploading 
<br><br>
<b>/{BotCommands.LeechZipWatchCommand}</b> [youtube-dl supported link]: Leech through youtube-dl and zip before uploading 
<br><br>
<b>/{BotCommands.LeechSetCommand}</b>: Pengaturan Leech
<br><br>
<b>/{BotCommands.SetThumbCommand}</b>: Reply photo untuk mengatur Thumbnail
<br><br>
<b>/{BotCommands.CancelMirror}</b>: Reply to the message by which the download was initiated and that download will be cancelled
<br><br>
<b>/{BotCommands.CancelAllCommand}</b>: Batalkan semua proses yang sedang berjalan
<br><br>
<b>/{BotCommands.ListCommand}</b> [search term]: Mencari Folder/File pada Google Drive (Database Bot)
<br><br>
<b>/{BotCommands.StatusCommand}</b>: Menampilkan Proses unduhan berjalan pada Bot
<br><br>
<b>/{BotCommands.StatsCommand}</b>: Menampilkan Waktu aktif Bot
'''
help = Telegraph(access_token=telegraph_token).create_page(
        title='List Perintah Bot Sep 21 Publik',
        author_name='Bot Sep 21 Publik - [No Bokep]',
        author_url='https://t.me/sepmirrorleech21_bot',
        html_content=help_string_telegraph,
    )["path"]

help_string = f'''
/{BotCommands.AuthorizeCommand}: Otorisasi obrolan / pengguna untuk menggunakan bot (Hanya dapat dilakukan oleh Pemilik & Sudo bot)

/{BotCommands.PingCommand}: Periksa berapa lama waktu yang dibutuhkan untuk melakukan Ping pada Bot

/{BotCommands.UnAuthorizeCommand}: Batalkan otorisasi obrolan / pengguna untuk menggunakan bot (Hanya dapat dipanggil oleh Pemilik & Sudo bot)

/{BotCommands.AddSudoCommand}: Tambahkan pengguna Sudo (Hanya Pemilik)

/{BotCommands.AuthorizedUsersCommand}: Tampilkan obrolan yang telah di Otorisasi (Hanya Pemilik & Sudo)

/{BotCommands.RmSudoCommand}: Hapus pengguna Sudo (Hanya Pemilik)

/{BotCommands.RestartCommand}: Mulai ulang bot

/{BotCommands.LogCommand}: Dapatkan log file bot. untuk mendapatkan laporan kesalahan pada bot

/{BotCommands.SpeedCommand}: Periksa Kecepatan Internet (Host)

/{BotCommands.ShellCommand}: Run commands in Shell (Only Owner)

/{BotCommands.ExecHelpCommand}: Get help for Executor module (Only Owner)

/{BotCommands.TsHelpCommand}: Bantuan untuk pencarian Torrent

/weebhelp: Bantuan untuk anime, manga & character.

/funyhelp: Get fun help.

/stickerhelp: Bantuan Untuk module stickers.

/weebify: Dapatkan text font weebify.
'''

def bot_help(update, context):
    button = button_build.ButtonMaker()
    button.buildbutton("🕹 Other Commands", f"https://telegra.ph/{help}")
    reply_markup = InlineKeyboardMarkup(button.build_menu(1))
    sendMarkup(help_string, context.bot, update, reply_markup)

'''
botcmds = [
        (f'{BotCommands.HelpCommand}','Get Detailed Help'),
        (f'{BotCommands.MirrorCommand}', 'Start Mirroring'),
        (f'{BotCommands.TarMirrorCommand}','Start mirroring and upload as .tar'),
        (f'{BotCommands.ZipMirrorCommand}','Start mirroring and upload as .zip'),
        (f'{BotCommands.UnzipMirrorCommand}','Extract files'),
        (f'{BotCommands.QbMirrorCommand}','Start Mirroring using qBittorrent'),
        (f'{BotCommands.QbTarMirrorCommand}','Start mirroring and upload as .tar using qb'),
        (f'{BotCommands.QbZipMirrorCommand}','Start mirroring and upload as .zip using qb'),
        (f'{BotCommands.QbUnzipMirrorCommand}','Extract files using qBitorrent'),
        (f'{BotCommands.CloneCommand}','Copy file/folder to Drive'),
        (f'{BotCommands.CountCommand}','Count file/folder of Drive link'),
        (f'{BotCommands.DeleteCommand}','Delete file from Drive'),
        (f'{BotCommands.WatchCommand}','Mirror Youtube-dl support link'),
        (f'{BotCommands.TarWatchCommand}','Mirror Youtube playlist link as .tar'),
        (f'{BotCommands.ZipWatchCommand}','Mirror Youtube playlist link as .zip'),
        (f'{BotCommands.CancelMirror}','Cancel a task'),
        (f'{BotCommands.CancelAllCommand}','Cancel all tasks'),
        (f'{BotCommands.ListCommand}','Searches files in Drive'),
        (f'{BotCommands.StatusCommand}','Get Mirror Status message'),
        (f'{BotCommands.LogCommand}','Get the Bot Log [owner/sudo only]'),
        (f'{BotCommands.PingCommand}','Ping the Bot'),
        (f'{BotCommands.RestartCommand}','Restart the bot [owner/sudo only]'),
        (f'{BotCommands.LogCommand}','Get the Bot Log [owner/sudo only]'),
        (f'{BotCommands.TsHelpCommand}','Get help for Torrent search module')
    ]
'''

def main():
    fs_utils.start_cleanup()
    if IS_VPS:
        asyncio.get_event_loop().run_until_complete(start_server_async(PORT))
    # Check if the bot is restarting
    if os.path.isfile(".restartmsg"):
        with open(".restartmsg") as f:
            chat_id, msg_id = map(int, f)
        bot.edit_message_text("Restarted successfully!", chat_id, msg_id)
        os.remove(".restartmsg")
    elif OWNER_ID:
        try:
            text = "<b>Bot Restarted!</b>"
            bot.sendMessage(chat_id=OWNER_ID, text=text, parse_mode=ParseMode.HTML)
            if AUTHORIZED_CHATS:
                for i in AUTHORIZED_CHATS:
                    bot.sendMessage(chat_id=i, text=text, parse_mode=ParseMode.HTML)
        except Exception as e:
            LOGGER.warning(e)
    # bot.set_my_commands(botcmds)
    start_handler = CommandHandler(BotCommands.StartCommand, start, run_async=True)
    ping_handler = CommandHandler(BotCommands.PingCommand, ping,
                                  filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    restart_handler = CommandHandler(BotCommands.RestartCommand, restart,
                                     filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
    help_handler = CommandHandler(BotCommands.HelpCommand,
                                  bot_help, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    stats_handler = CommandHandler(BotCommands.StatsCommand,
                                   stats, filters=CustomFilters.authorized_chat | CustomFilters.authorized_user, run_async=True)
    log_handler = CommandHandler(BotCommands.LogCommand, log, filters=CustomFilters.owner_filter | CustomFilters.sudo_user, run_async=True)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(ping_handler)
    dispatcher.add_handler(restart_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(stats_handler)
    dispatcher.add_handler(log_handler)
    updater.start_polling(drop_pending_updates=IGNORE_PENDING_REQUESTS)
    LOGGER.info("Bot Started!")
    signal.signal(signal.SIGINT, fs_utils.exit_clean_up)

app.start()
main()
idle()
