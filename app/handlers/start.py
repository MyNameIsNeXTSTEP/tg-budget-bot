from telegram import Update
from telegram.ext import ContextTypes

from app.handlers.response import send_response
from app.templates import render_template
from app import config


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not (config.TELEGRAM_USER_ID == update.effective_user.id):
        await send_response(update, context, response=render_template("unauthorized-user.j2"))
    else:
        await send_response(update, context, response=render_template("start.j2"))
