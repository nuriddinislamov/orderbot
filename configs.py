from main import *
KOTEX, BELLA, ALWAYS, LIBRESSE = ('KOTEX', 'BELLA', 'ALWAYS', 'LIBRESSE')
KOTEX_BTN, BELLA_BTN, ALWAYS_BTN, LIBRESSE_BTN = (
    '🍒 KOTEX', '🦋 BELLA', '🌊️ ALWAYS', '🌸 LIBRESSE')
ABSORBANCE, QUANTITY, FREQUENCY, CHECKOUT, CONTACT_NAME, CONTACT_PHONE, CONTACT_ADDRESS, CONTACT_COMMENTS,\
    CONTACT_PAYMENT_TYPE, FINAL = map(chr, range(10))
ADMIN_id = 361516746

# LOGOS #
logos = {'KOTEX': 'https://telegra.ph/logo-kotex-03-21',
         'BELLA': 'https://telegra.ph/logo-bella-03-21',
         'ALWAYS': 'https://telegra.ph/logo-always-03-21',
         'LIBRESSE': 'https://telegra.ph/logo-libresse-03-21'}

absorbance_buttons = {
    'KOTEX': [
        [InlineKeyboardButton('4 💧', callback_data='4'),
         InlineKeyboardButton('5 💧', callback_data='5'),
         InlineKeyboardButton('6 💧', callback_data='6')]
    ],
    'BELLA': [
        [InlineKeyboardButton('3 💧', callback_data='3'),
         InlineKeyboardButton('4 💧', callback_data='4'),
         InlineKeyboardButton('5 💧', callback_data='5'),
         InlineKeyboardButton('6 💧', callback_data='6')]
    ],
    'ALWAYS': [
        [InlineKeyboardButton('3 💧', callback_data='3'),
         InlineKeyboardButton('4 💧', callback_data='4'),
         InlineKeyboardButton('5 💧', callback_data='5'),
         InlineKeyboardButton('6 💧', callback_data='6'),
         InlineKeyboardButton('7 💧', callback_data='7')]
    ],
    'LIBRESSE': [
        [InlineKeyboardButton('4 💧', callback_data='4'),
         InlineKeyboardButton('5 💧', callback_data='5'),
         InlineKeyboardButton('6 💧', callback_data='6')]
    ],
}
quantity_buttons = [
    [InlineKeyboardButton('1', callback_data='1'),
     InlineKeyboardButton('2', callback_data='2'),
     InlineKeyboardButton('3', callback_data='3')],
    [InlineKeyboardButton('4', callback_data='4'),
     InlineKeyboardButton('5', callback_data='5'),
     InlineKeyboardButton('6', callback_data='6')],
    [InlineKeyboardButton('7', callback_data='7'),
     InlineKeyboardButton('8', callback_data='8'),
     InlineKeyboardButton('9', callback_data='9')]
]
photos = {
    'KOTEX': {
        '4': 'https://telegra.ph/4-kotex-03-21',
        '5': 'https://telegra.ph/5-kotex-03-21',
        '6': 'https://telegra.ph/6-kotex-03-21'
    },
    'BELLA': {
        '3': 'https://telegra.ph/3-bella-03-21',
        '4': 'https://telegra.ph/4-bella-03-21',
        '5': 'https://telegra.ph/5-bella-03-21',
        '6': 'https://telegra.ph/6-bella-03-21'

    },
    'ALWAYS': {
        '3': 'https://telegra.ph/3-always-03-21',
        '4': 'https://telegra.ph/4-always-03-21',
        '5': 'https://telegra.ph/5-always-03-21',
        '6': 'https://telegra.ph/6-always-03-21',
        '7': 'https://telegra.ph/7-always-03-21',

    },
    'LIBRESSE': {
        '4': 'https://telegra.ph/4-always-03-21',
        '5': 'https://telegra.ph/5-always-03-21',
        '6': 'https://telegra.ph/6-always-03-21'
    }
}

pcs = {
    'KOTEX': {
        '4': '10',
        '5': '8',
        '6': '7'
    },
    'BELLA': {
        '3': '10',
        '4': '10',
        '5': '8',
        '6': '7'
    },
    'ALWAYS': {
        '3': '10',
        '4': '10',
        '5': '8',
        '6': '7',
        '7': '6'
    },
    'LIBRESSE': {
        '4': '10',
        '5': '8',
        '6': '8'
    }
}
prices = {
    'KOTEX': {
        '4': '13590',
        '5': '13590',
        '6': '13590'
    },
    'BELLA': {
        '3': '11890',
        '4': '12890',
        '5': '12890',
        '6': '12890'
    },
    'ALWAYS': {
        '3': '11000',
        '4': '11000',
        '5': '12000',
        '6': '12000',
        '7': '13000'
    },
    'LIBRESSE': {
        '4': '14000',
        '5': '14000',
        '6': '15000'
    }
}

frequency_buttons = [
    [InlineKeyboardButton('Единоразово', callback_data='onetime')],
    [InlineKeyboardButton('Раз в месяц', callback_data='once-a-month')],
    [InlineKeyboardButton('Раз в два месяца',
                          callback_data='once-in-two-months')],
    [InlineKeyboardButton('Раз в три месяца',
                          callback_data='once-in-three-months')]
]
checkout_buttons = [
    [InlineKeyboardButton('✅ Далее', callback_data='confirm')],
    [InlineKeyboardButton('❌ Отменяю', callback_data='cancel-order')]
]

frequency_translate = {
    'onetime': 'Единоразово',
    'once-a-month': 'Раз в месяц',
    'once-in-two-months': 'Раз в два месяца',
    'once-in-three-months': 'Раз в три месяца'
}
payment_type_translate = {
    'cash': 'Наличные',
    'payme': 'PayMe',
    'click': 'Click',
    'uzcard': 'UzCard'
}
phone_button = [
    [KeyboardButton('📲 Отправить мой номер телефона', request_contact=True)]
]
payment_type_buttons = [
    [InlineKeyboardButton('Наличные', callback_data='cash')],
    [InlineKeyboardButton('PayMe', callback_data='payme'),
     InlineKeyboardButton('Сlick', callback_data='click')],
    [InlineKeyboardButton('UzCard', callback_data='uzcard')]
]
final_buttons = [
    [InlineKeyboardButton('Заказываю', callback_data='confirm')],
    [InlineKeyboardButton('Отменяю', callback_data='cancel')]
]
