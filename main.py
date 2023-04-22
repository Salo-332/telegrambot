@bot.callback_query_handler(func=lambda call: call.data == "button1")
def callback_function1(callback_obj):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button3 = telebot.types.InlineKeyboardButton(text="Программирование и информационные технологии",
                                                  callback_data="button3")
    button4 = telebot.types.InlineKeyboardButton(text="Медицинский", callback_data="button3")
    button5 = telebot.types.InlineKeyboardButton(text="Экономика и управление", callback_data="button3")
    button6 = telebot.types.InlineKeyboardButton(text="Строительство и энергетика", callback_data="button3")
    button7 = telebot.types.InlineKeyboardButton(text="Юриспруденция", callback_data="button3")
    button8 = telebot.types.InlineKeyboardButton(text="Реклама и СМИ", callback_data="button3")
    button9 = telebot.types.InlineKeyboardButton(text="Сервис и туризм", callback_data="button3")
    button10 = telebot.types.InlineKeyboardButton(text="Педагогика и психология", callback_data="button3")
    button11 = telebot.types.InlineKeyboardButton(text="Дизайн", callback_data="button3")
    button12 = telebot.types.InlineKeyboardButton(text="Анимация", callback_data="button3")
    button13 = telebot.types.InlineKeyboardButton(text="Актерское мастерство и искусство", callback_data="button3")
    button14 = telebot.types.InlineKeyboardButton(text="Лингвистика и переводоведение", callback_data="button3")
    keyboard.row(button3, button4, button5)
    keyboard.row(button6, button7, button8)
    keyboard.row(button9, button10, button11)
    keyboard.row(button12, button13, button14)
    bot.send_message(callback_obj.from_user.id, "Вы выбрали факультет.",
                     reply_markup=keyboard)
    bot.register_next_step_handler(bally_ege)
    bot.answer_callback_query(callback_query_id=callback_obj.id)         Это для ВУЗа
    
    
    
    
    
    
    
@bot.callback_query_handler(func=lambda call: call.data in ["button2"])
def callback_function2(callback_obj):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button15 = telebot.types.InlineKeyboardButton(text="Программирование и информационные технологии",
                                                  callback_data="button15")
    button16 = telebot.types.InlineKeyboardButton(text="Медицинский", callback_data="button16")
    button17 = telebot.types.InlineKeyboardButton(text="Экономика и управление", callback_data="button16")
    button18 = telebot.types.InlineKeyboardButton(text="Строительство и энергетика", callback_data="button16")
    button19 = telebot.types.InlineKeyboardButton(text="Юриспруденция", callback_data="button16")
    button20 = telebot.types.InlineKeyboardButton(text="Реклама и СМИ", callback_data="button16")
    button21 = telebot.types.InlineKeyboardButton(text="Сервис и туризм", callback_data="button16")
    button22 = telebot.types.InlineKeyboardButton(text="Педагогика и психология", callback_data="button16")
    button23 = telebot.types.InlineKeyboardButton(text="Дизайн", callback_data="button16")
    button24 = telebot.types.InlineKeyboardButton(text="Анимация", callback_data="button16")
    button25 = telebot.types.InlineKeyboardButton(text="Актерское мастерство и искусство", callback_data="button16")
    button26 = telebot.types.InlineKeyboardButton(text="Лингвистика и переводоведение", callback_data="button16")
    keyboard.row(button15, button16, button17)
    keyboard.row(button18, button19, button20)
    keyboard.row(button21, button22, button23)
    keyboard.row(button24, button25, button26)
    bot.send_message(callback_obj.from_user.id, "Вы  выбрали ПТУ, давайте выберем факультет.", reply_markup=keyboard)
    psg = bot.send_message(callback_obj.from_user.id, "Вы выбрали ПТУ, пожалуйста введите ваши баллы ОГЭ.", )
    bot.register_next_step_handler(psg, bally_oge)
    bot.answer_callback_query(callback_query_id=callback_obj.id)             Это для ПТУ
