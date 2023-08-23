
import telebot
import requests


# res = requests.post('localhost:5000/api')
url = 'http://localhost:5000/api'
clearchat = 'http://localhost:5000/delete_chats'

TOKEN = '6542115754:AAHhB6sB1ehuAjXqgnV_RysvAP2o_9mbVvM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy,I'm Coach Care. Your personal Coach. How can I help you?")

@bot.message_handler(commands=['chat'])
def chat(message):
	
	print()
	user = message.from_user.username
	prompt = message.text
	myobj = {
	"user_id":user,
	"prompt": prompt
	}
	x = requests.post(url, json = myobj)
	print(x)
	ans = x.json()
	print("GPT ANSWER : ",ans)
	bot.reply_to(message, ans['message'])


@bot.message_handler(commands=['clear'])
def clear(message):
	
	print()
	user = message.from_user.username

	myobj = {
	"user_id":user,
	}
	x = requests.post(clearchat, json = myobj)
	print(x)
	ans = x.json()
	print("bot ANSWER : ",ans)
	return bot.reply_to(message, ans['message'])



@bot.message_handler(commands=['help'])
def help(message):
	string = "Hello! \nThis bot is developed to motivate you. \n\nBe Motivated :) "
	return bot.reply_to(message, string)

bot.infinity_polling()