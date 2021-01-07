from telegram import Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext


def voice_message_handler(update: Update, context: CallbackContext) -> None:
    try:
        update.message.delete()
    except BadRequest:
        context.bot.send_message(update.message.chat_id, text='Видимо у бота нет прав удалять сообщения(')
        return
    context.bot.send_message(update.message.chat_id, text=f'Пиши буквами падла @{update.message.from_user.username}')
