import random
import string
import telebot
from telebot import types

# Reemplaza 'TOKEN' con tu token proporcionado por BotFather
TOKEN = 'TU_TOKEN_AQUI'

# Crear un objeto bot
bot = telebot.TeleBot(TOKEN)

# Manejar el comando /start
@bot.message_handler(commands=['start'])
def start(message):
    # Crear un teclado personalizado
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item_generar_contrasena = types.KeyboardButton('Generar Contraseña')
    markup.add(item_generar_contrasena)

    # Enviar mensaje de bienvenida con el teclado personalizado
    bot.send_message(message.chat.id, '¡Bienvenido! Pulsa en el botón de abajo:', reply_markup=markup)

# Manejar la opción Generar Contraseña
@bot.message_handler(func=lambda message: message.text == 'Generar Contraseña')
def generar_contrasena(message):
    try:
        # Obtener la longitud de la contraseña del usuario
        msg = bot.send_message(message.chat.id, "Por favor, ingresa la longitud de la contraseña con números:")
        bot.register_next_step_handler(msg, obtener_longitud)
    except Exception as e:
        bot.send_message(message.chat.id, 'Ha ocurrido un error.')

# Función para obtener la longitud de la contraseña
def obtener_longitud(message):
    try:
        longitud = int(message.text.strip())
        # Caracteres para generar la contraseña
        caracteres = string.ascii_letters + string.digits + string.punctuation

        # Generar la contraseña
        passwd = "".join(random.choice(caracteres) for i in range(longitud))

        # Enviar la contraseña al usuario
        bot.send_message(message.chat.id, "La contraseña generada es:\n")
        bot.send_message(message.chat.id, passwd)

    except ValueError:
        bot.send_message(message.chat.id, 'Por favor, ingresa un número válido para la longitud de la contraseña.')

# Manejar errores
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        pass
    except Exception as e:
        bot.send_message(message.chat.id, 'Ha ocurrido un error.')

# Iniciar el bot
bot.polling()
