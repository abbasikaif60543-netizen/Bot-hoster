import telebot
import subprocess
import os

# Aapka Data
API_TOKEN = '8795803232:AAGOi6ab7q64qu8BnvknxJJ2JNjceB5LFNo'
ADMIN_ID = 8599256964

bot = telebot.TeleBot(API_TOKEN)
processes = {}

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "✅ Manager Bot Active!\n\nAb apni asli bot wali (.py) file mujhe Document ke taur par bhejiye.")
    else:
        bot.reply_to(message, "❌ Access Denied!")

@bot.message_handler(content_types=['document'])
def handle_file(message):
    if message.from_user.id == ADMIN_ID:
        if message.document.file_name.endswith('.py'):
            file_name = message.document.file_name
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            
            with open(file_name, 'wb') as f:
                f.write(downloaded_file)
            
            if file_name in processes:
                processes[file_name].terminate()
            
            try:
                process = subprocess.Popen(['python3', file_name])
                processes[file_name] = process
                bot.send_message(ADMIN_ID, f"🚀 `{file_name}` Railway par live hai!")
            except Exception as e:
                bot.reply_to(message, f"❌ Error: {str(e)}")

bot.polling(none_stop=True)
          
