async def send_post(telegram_chat_id, bot, text, image):
    if image:
        message = await bot.send_photo(chat_id=telegram_chat_id, photo=image, caption=text)
    else:
        message = await bot.send_message(chat_id=telegram_chat_id, text=text)
    return message['message_id']


async def send_animation_image(telegram_chat_id, bot, image):
    message = await bot.sendAnimation(chat_id=telegram_chat_id, animation=image)
    return message['message_id']
