import sys
import sqlite3

def loadDB():
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    cur.executescript('''CREATE TABLE IF NOT EXISTS userdata
    (
    id INTEGER NOT NULL PRIMARY KEY UNIQUE, 
    firstname TEXT, 
    Name TEXT,
    Age TEXT,
    Address TEXT,
    Amount TEXT);'''
    )
    conn.commit()
    conn.close()

def checkUser(update, user_data):
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    if len(cur.execute('''SELECT id FROM userdata WHERE id = ?        
            ''', (update.message.from_user.id,)).fetchall())>0:
        c=cur.execute('''SELECT Name FROM userdata WHERE id = ?''', (update.message.from_user.id,)).fetchone()
        user_data['Name']=c[0]
        c=cur.execute('''SELECT Age FROM userdata WHERE id = ?''', (update.message.from_user.id,)).fetchone()
        user_data['Age']=c[0]
        c=cur.execute('''SELECT Address FROM userdata WHERE id = ?''', (update.message.from_user.id,)).fetchone()
        user_data['Address']=c[0]
        c=cur.execute('''SELECT Amount FROM userdata WHERE id = ?''', (update.message.from_user.id,)).fetchone()
        user_data['Amount']=c[0]
        print('Past user')
    else:
        cur.execute('''INSERT OR IGNORE INTO userdata (id, firstname) VALUES (?, ?)''', \
        (update.message.from_user.id, update.message.from_user.first_name,))
        print('New user')
    conn.commit()
    conn.close()

def updateUser(category, text, update):
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
   
    cur.execute('''UPDATE OR IGNORE userdata SET {} = ? WHERE id = ?'''.format(category), \
        (text, update.message.from_user.id,))
    conn.commit()
    conn.close() 

from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [['Name', 'Age'],
                  ['Address', 'Amount'],
                  ['Done']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])

def start(bot, update, user_data):
    update.message.reply_text(
        "Меня зовут Ольга. "
        "Расскажи что-нибудь о себе?",
        reply_markup=markup)
    checkUser(update, user_data)
    return CHOOSING

def regular_choice(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text(
        'Вы {}? Да, я бы с удовольствием послушала вас'.format(text.lower()))
    return TYPING_REPLY

def received_information(bot, update, user_data):
    text = update.message.text
    category = user_data['choice']
    user_data[category] = text
    updateUser(category, text, update)
    del user_data['choice']

    update.message.reply_text("Это вы мне уже говорили:"
                              "{}"
                              "Вы можете рассказать мне больше или изменить мое мнение об этом".format(
                                  facts_to_str(user_data)), reply_markup=markup)
    return CHOOSING

def done(bot, update, user_data):
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text("Я узнала эти факты о вас:"
                              "{}"
                              "В слудующий раз".format(facts_to_str(user_data)))

    user_data.clear()
    return ConversationHandler.END

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    
    updater = Updater("5881557278:AAG2BOrgW4fCCJO8Dk2mQl5vUfD-SGEUYqg")
    print("Установлено соедиение с Telegram, запуск бота")
   
    dp = updater.dispatcher

   
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start, pass_user_data=True)],
        
        states={
            CHOOSING: [RegexHandler('^(Name|Age|Address|Amount)$',
                                    regular_choice,
                                    pass_user_data=True),
                       ],

            TYPING_CHOICE: [MessageHandler(Filters.text,
                                           regular_choice,
                                           pass_user_data=True),
                            ],

            TYPING_REPLY: [MessageHandler(Filters.text,
                                          received_information,
                                          pass_user_data=True),
                           ],
        },

        fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
    )

    dp.add_handler(conv_handler)
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    loadDB()
    main()