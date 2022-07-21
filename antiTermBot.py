import discord
from discord.ext import commands
from colorama import Fore, init

init()

client = commands.Bot(command_prefix="_")

configObject = open('config.txt', "r")
config = configObject.read().splitlines()
configObject.close()

fileObject = open('blacklist.txt', "r")
words = fileObject.read().splitlines()
fileObject.close()

tokenObject = open('token.txt', "r")
token = tokenObject.read()
tokenObject.close()
if (config[0] == "true"):
    Logging = True



@client.event
async def on_ready():
    print(Fore.GREEN + "Bot is up and running!")
    print(Fore.WHITE + "----------------------")
    print(Fore.GREEN + "Loaded blacklisted words: \n" + str(words))
    print(Fore.WHITE + "----------------------")



@client.event
async def on_message(message):
    if message.content in words:
        await message.delete()
        if Logging:
            print(Fore.BLUE + "[LOG] " + str(message.author) + " tried to send blacklisted word: " + Fore.RED + message.content)


client.run(token)


