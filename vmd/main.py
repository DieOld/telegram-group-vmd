import os
import logging

from telegram.ext import (
    Updater,
    Filters,
    MessageHandler
)

from src import handlers

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    updater = Updater(token=os.environ['TELEGRAM_BOT_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.voice | Filters.video_note, handlers.voice_message_handler))
    updater.start_polling()
    updater.idle()
