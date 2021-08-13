
import os
import logging
from telegram.ext import Updater, CommandHandler


TOKEN = os.environ.get('TOKEN')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


StartMessage = '''
        Hello! How can I help you today?

        Use:
        ..test... mode... this bot.. is useless.... for now..
        
            /start  - To display this message
            /artist - To get my favorite artist
            /zoro ?
        '''


def start(update, context):
    update.message.reply_text(StartMessage)


def artist(update, context):
    update.message.reply_text('John mayer!')


def zoro(update, context):
    update.message.reply_text('عمي')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("artist", artist))
    dp.add_handler(CommandHandler("zoro", zoro))

    # log errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
