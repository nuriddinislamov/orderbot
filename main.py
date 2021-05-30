from telegram import *
from telegram.ext import *
from texts import *
from configs import *
from api_token import API_TOKEN
import datetime


def start(update, context):
    user = update.message
    telegram_id = user.chat_id
    buttons = [
        [InlineKeyboardButton(KOTEX_BTN, callback_data=KOTEX),
         InlineKeyboardButton(BELLA_BTN, callback_data=BELLA)],
        [InlineKeyboardButton(ALWAYS_BTN, callback_data=ALWAYS),
         InlineKeyboardButton(LIBRESSE_BTN, callback_data=LIBRESSE)]
    ]
    context.user_data.clear()
    if telegram_id != ADMIN_id:
        context.bot.send_message(chat_id=telegram_id,
                                 text=start_text,
                                 reply_markup=InlineKeyboardMarkup(buttons),
                                 parse_mode='HTML')
        payload = {
            'user':
                {
                    'user_id': telegram_id,
                    'username': user.from_user.username,
                    'first_name': user.from_user.first_name,
                    'last_name': user.from_user.last_name
                }
        }
        context.user_data.update(payload)
        return ABSORBANCE
    else:
        update.message.reply_text('Вы админ')
        return ConversationHandler.END


def absorbance(update, context):
    query = update.callback_query
    data = query.data
    context.bot.delete_message(chat_id=query.message.chat.id,
                               message_id=query.message.message_id)
    payload = {
        'brand': data
    }
    context.user_data.update(payload)
    context.bot.send_photo(chat_id=query.message.chat.id,
                           photo=logos[data],
                           caption=absorbance_caption,
                           reply_markup=InlineKeyboardMarkup(
                               absorbance_buttons[data]),
                           parse_mode='HTML')
    return QUANTITY


def quantity(update, context):
    query = update.callback_query
    data = query.data
    payload = {
        'absorbance': data
    }
    context.user_data.update(payload)
    user_data = context.user_data
    brand = user_data['brand']
    absorbance_choice = user_data['absorbance']
    context.bot.delete_message(chat_id=user_data['user']['user_id'],
                               message_id=query.message.message_id)
    context.bot.send_photo(chat_id=user_data['user']['user_id'],
                           photo=photos[brand][absorbance_choice],
                           caption=quantity_caption.format(
                               brand, absorbance_choice, pcs[brand][absorbance_choice]),
                           reply_markup=InlineKeyboardMarkup(quantity_buttons),
                           parse_mode='HTML')
    return FREQUENCY


def frequency(update, context):
    query = update.callback_query
    data = query.data
    payload = {
        'quantity': data
    }
    context.user_data.update(payload)
    user_data = context.user_data
    context.bot.delete_message(chat_id=user_data['user']['user_id'],
                               message_id=query.message.message_id)
    context.bot.send_message(chat_id=user_data['user']['user_id'],
                             text=frequency_text,
                             reply_markup=InlineKeyboardMarkup(
                                 frequency_buttons),
                             parse_mode='HTML')
    return CHECKOUT


def checkout(update, context):
    query = update.callback_query
    data = query.data
    payload = {
        'frequency': data
    }
    context.user_data.update(payload)
    user_data = context.user_data
    context.bot.delete_message(chat_id=user_data['user']['user_id'],
                               message_id=query.message.message_id)
    total = int(user_data['quantity']) * \
        int(prices[user_data['brand']][user_data['absorbance']])
    raw_list = list(str(total))
    raw_list.insert(-3, ' ')
    formatted_total = "".join(i for i in raw_list)
    context.bot.send_message(chat_id=user_data['user']['user_id'],
                             text=checkout_text.format(
                                 user_data['quantity'], user_data['brand'], user_data['absorbance'],
                                 pcs[user_data['brand']][user_data['absorbance']],
                                 frequency_translate[user_data['frequency']],
                                 formatted_total
    ),
        reply_markup=InlineKeyboardMarkup(
                                 checkout_buttons),
        parse_mode='HTML')
    return CONTACT_NAME


def cancel_order(update, context):
    query = update.callback_query
    user_data = context.user_data
    context.bot.delete_message(chat_id=user_data['user']['user_id'],
                               message_id=query.message.message_id)
    context.bot.send_message(chat_id=user_data['user']['user_id'],
                             text=canceled_text,
                             parse_mode='HTML')
    return ConversationHandler.END


def name(update, context):
    query = update.callback_query
    user_data = context.user_data
    context.bot.delete_message(chat_id=user_data['user']['user_id'],
                               message_id=query.message.message_id)
    context.bot.send_message(chat_id=user_data['user']['user_id'],
                             text=request_name,
                             parse_mode='HTML')
    return CONTACT_PHONE


def phone(update, context):
    user_input = update.message.text
    payload = {
        'input_name': user_input
    }
    context.user_data.update(payload)
    update.message.reply_html(request_phone.format(user_input),
                              reply_markup=ReplyKeyboardMarkup(phone_button, resize_keyboard=True))
    return CONTACT_ADDRESS


def address(update, context):
    user_input = update.message.text
    if user_input is None:
        user_phone = update.message.contact.phone_number
        payload = {
            'input_phone': user_phone
        }
        context.user_data.update(payload)
    else:
        payload = {
            'input_phone': user_input
        }
        context.user_data.update(payload)
    update.message.reply_html(request_address,
                              reply_markup=ReplyKeyboardRemove())
    return CONTACT_PAYMENT_TYPE


def payment_type(update, context):
    address_input = update.message.text
    payload = {
        'input_address': address_input
    }
    context.user_data.update(payload)
    user_data = context.user_data
    context.bot.send_message(chat_id=user_data['user']['user_id'],
                             text=payment_type_text,
                             reply_markup=InlineKeyboardMarkup(
                                 payment_type_buttons),
                             parse_mode='HTML')
    return CONTACT_COMMENTS


def comments(update, context):
    query = update.callback_query
    data = query.data
    payload = {
        'input_payment_type': data
    }
    context.user_data.update(payload)
    user_data = context.user_data
    context.bot.delete_message(chat_id=user_data['user']['user_id'],
                               message_id=query.message.message_id)
    context.bot.send_message(chat_id=user_data['user']['user_id'],
                             text=request_comments,
                             parse_mode='HTML')
    return FINAL


def final_decision(update, context):
    comment = update.message.text
    payload = {
        'input_comments': comment
    }
    context.user_data.update(payload)
    user_data = context.user_data
    total = int(user_data['quantity']) * \
        int(prices[user_data['brand']][user_data['absorbance']])
    raw_list = list(str(total))
    raw_list.insert(-3, ' ')
    formatted_total = "".join(i for i in raw_list)
    context.bot.send_message(chat_id=user_data['user']['user_id'],
                             text=final_text.format(
                                 user_data['input_name'], user_data['input_phone'], user_data['input_address'],
                                 payment_type_translate[user_data['input_payment_type']],
                                 user_data['input_comments'],
                                 user_data['quantity'], user_data['brand'], user_data['absorbance'],
                                 pcs[user_data['brand']][user_data['absorbance']],
                                 frequency_translate[user_data['frequency']],
                                 formatted_total
    ),
        reply_markup=InlineKeyboardMarkup(final_buttons),
        parse_mode='HTML')


def order_complete(update, context):
    query = update.callback_query
    user_data = context.user_data
    context.bot.delete_message(chat_id=user_data['user']['user_id'],
                               message_id=query.message.message_id)
    context.bot.send_message(chat_id=user_data['user']['user_id'],
                             text=order_complete_text,
                             parse_mode='HTML')
    total = int(user_data['quantity']) * \
        int(prices[user_data['brand']][user_data['absorbance']])
    raw_list = list(str(total))
    raw_list.insert(-3, ' ')
    formatted_total = "".join(i for i in raw_list)
    uzbekistan_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5)
    uz_time_formatted = uzbekistan_time.strftime("%Y-%m-%d %H:%M:%S")
    context.bot.send_message(chat_id=ADMIN_id,
                             text=order_admin.format(
                                 uz_time_formatted,
                                 user_data['input_name'], user_data['input_phone'], user_data['input_address'],
                                 payment_type_translate[user_data['input_payment_type']],
                                 user_data['input_comments'],
                                 user_data['user']['username'],
                                 user_data['user']['first_name'],
                                 user_data['user']['last_name'],
                                 user_data['quantity'],
                                 user_data['brand'],
                                 user_data['absorbance'],
                                 pcs[user_data['brand']][user_data['absorbance']],
                                 frequency_translate[user_data['frequency']],
                                 formatted_total
                             ),
                             parse_mode='HTML')
    return ConversationHandler.END


def admin(update, context):
    user_name = update.message.from_user.username
    telegram_id = update.message.chat_id
    if telegram_id == ADMIN_id:
        update.message.reply_html(f'Привет, мой админ <b>{user_name}</b> !')
    else:
        pass


def main():
    updater = Updater(token=API_TOKEN, workers=20)
    dispatcher = updater.dispatcher

    conversation = ConversationHandler(
        entry_points=[CommandHandler('start', start, run_async=True),
                      CommandHandler('order', start, run_async=True)],
        states={
            ABSORBANCE: [
                CallbackQueryHandler(absorbance, pattern=KOTEX),
                CallbackQueryHandler(absorbance, pattern=BELLA),
                CallbackQueryHandler(absorbance, pattern=ALWAYS),
                CallbackQueryHandler(absorbance, pattern=LIBRESSE),
            ],
            QUANTITY: [
                CallbackQueryHandler(quantity, pattern='3'),
                CallbackQueryHandler(quantity, pattern='4'),
                CallbackQueryHandler(quantity, pattern='5'),
                CallbackQueryHandler(quantity, pattern='6'),
                CallbackQueryHandler(quantity, pattern='7')
            ],
            FREQUENCY: [
                CallbackQueryHandler(frequency, pattern='1'),
                CallbackQueryHandler(frequency, pattern='2'),
                CallbackQueryHandler(frequency, pattern='3'),
                CallbackQueryHandler(frequency, pattern='4'),
                CallbackQueryHandler(frequency, pattern='5'),
                CallbackQueryHandler(frequency, pattern='6'),
                CallbackQueryHandler(frequency, pattern='7'),
                CallbackQueryHandler(frequency, pattern='8'),
                CallbackQueryHandler(frequency, pattern='9')
            ],
            CHECKOUT: [
                CallbackQueryHandler(checkout, pattern='onetime'),
                CallbackQueryHandler(checkout, pattern='once-a-month'),
                CallbackQueryHandler(checkout, pattern='once-in-two-months'),
                CallbackQueryHandler(checkout, pattern='once-in-three-months')
            ],
            CONTACT_NAME: [
                CallbackQueryHandler(name, pattern='confirm'),
                CallbackQueryHandler(cancel_order, pattern='cancel-order')
            ],
            CONTACT_PHONE: [
                MessageHandler(Filters.text, phone)
            ],
            CONTACT_ADDRESS: [
                MessageHandler(Filters.contact, address),
                MessageHandler(Filters.text, address)
            ],
            CONTACT_PAYMENT_TYPE: [
                MessageHandler(Filters.text, payment_type)
            ],
            CONTACT_COMMENTS: [
                CallbackQueryHandler(comments, pattern='cash'),
                CallbackQueryHandler(comments, pattern='payme'),
                CallbackQueryHandler(comments, pattern='click'),
                CallbackQueryHandler(comments, pattern='uzcard')
            ],
            FINAL: [
                MessageHandler(Filters.text, final_decision),
                CallbackQueryHandler(order_complete, pattern='confirm'),
                CallbackQueryHandler(cancel_order, pattern='cancel')
            ]
        },
        fallbacks=[
            CommandHandler('start', start, run_async=True),
            CommandHandler('order', start, run_async=True)
        ]
    )

    dispatcher.add_handler(conversation),
    dispatcher.add_handler(MessageHandler(Filters.all, admin))

    updater.start_polling()
    updater.idle()
