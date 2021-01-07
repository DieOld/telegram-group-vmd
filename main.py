import os
import logging

from telegram import Update
from telegram.error import BadRequest
from telegram.ext import (
    Updater,
    Filters,
    MessageHandler, CallbackContext
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def message_handler(update: Update, context: CallbackContext) -> None:
    try:
        update.message.delete()
    except BadRequest:
        context.bot.send_message(update.message.chat_id, text='Видимо у бота нет прав удалять сообщения(')
        return
    context.bot.send_message(update.message.chat_id, text='Пиши буквами падла')


if __name__ == '__main__':
    updater = Updater(token=os.environ['TELEGRAM_BOT_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.voice, message_handler))
    updater.start_polling()
    updater.idle()
