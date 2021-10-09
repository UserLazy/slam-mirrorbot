import json
import html
import bs4
import requests
from bot import dispatcher
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update)
from telegram.ext import (
    CallbackContext,
    CommandHandler,
    CallbackQueryHandler)

info_btn = "More Information"
kaizoku_btn = "🤡 Kaizoku 🤡"
doujindesu_btn = "😍 Doujindesu 😍"
bakadame_btn = "👾 Bakadame 👾"
ganime_btn = "🤡 Ganime 🤡"
prequel_btn = "🤖 Prequel 👈🏻"
sequel_btn = "👉🏻 Sequel 🤖"
close_btn = "❌ Close ❌"


def site_search(update: Update, context: CallbackContext, site: str):
    message = update.effective_message
    args = message.text.strip().split(" ", 1)
    more_results = True

    try:
        search_query = args[1]
    except IndexError:
        message.reply_text("Give something to search")
        return

    if site == "kaizoku":
        search_url = f"https://animekaizoku.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "post-title"})

        if search_result:
            result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>KaizokuAnime</code>: \n"
            for entry in search_result:
                post_link = "https://animekaizoku.com/" + entry.a['href']
                post_name = html.escape(entry.text)
                result += f"• <a href='{post_link}'>{post_name}</a>\n"
        else:
            more_results = False
            result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>KaizokuAnime</code>"

    elif site == "doujindesu":
        search_url = f"https://doujindesu.id/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>DoujinDesu</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>DoujinDesu</code>"
                more_results = False
                break

            post_link = entry.a['href']
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"

    elif site == "bakadame":
        search_url = f"https://bakadame.com/?s={search_query}"
        html_text = requests.get(search_url).text
        soup = bs4.BeautifulSoup(html_text, "html.parser")
        search_result = soup.find_all("h2", {'class': "title"})

        result = f"<b>Search results for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>Bakadame</code>: \n"
        for entry in search_result:

            if entry.text.strip() == "Nothing Found":
                result = f"<b>No result found for</b> <code>{html.escape(search_query)}</code> <b>on</b> <code>Bakadame</code>"
                more_results = False
                break

            post_link = entry.a['href']
            post_name = html.escape(entry.text.strip())
            result += f"• <a href='{post_link}'>{post_name}</a>\n"
          

    buttons = [[InlineKeyboardButton("See all results", url=search_url)]]

    if more_results:
        message.reply_text(
            result,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True)
    else:
        message.reply_text(
            result, parse_mode=ParseMode.HTML, disable_web_page_preview=True)


def kaizoku(update: Update, context: CallbackContext):
    site_search(update, context, "kaizoku")


def doujindesu(update: Update, context: CallbackContext):
    site_search(update, context, "doujindesu")


def bakadame(update: Update, context: CallbackContext):
    site_search(update, context, "bakadame")

    
    
    
KAIZOKU_SEARCH_HANDLER = CommandHandler("kaizoku", kaizoku)
DOUJINDESU_SEARCH_HANDLER = CommandHandler("doujindesu", doujindesu)
BAKADAME_SEARCH_HANDLER = CommandHandler("bakadame", bakadame)

dispatcher.add_handler(KAIZOKU_SEARCH_HANDLER)
dispatcher.add_handler(DOUJINDESU_SEARCH_HANDLER)
dispatcher.add_handler(BAKADAME_SEARCH_HANDLER)
