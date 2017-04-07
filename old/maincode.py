import discord
from discord.ext.commands import Bot
import asyncio
import random

client = Bot(command_prefix="$")

@client.command()	#help command with detailed descriptions 
async def commandhelp(*args):
	print(args)
	helpList = ['```[ORRER} Help Menu - All commands prefixed by "$"', 
			'hello - test message, returns "Hello!"', 
			'ytho, myeyes, reee, butytho, eyebrows - general response images', 
			'error - returns signature error message', 
			'Add command to "$commandhelp" to recieve additional info on that command.', 
			'EX: $commandhelp ytho', 
			'Written by 16ajans#6893```']
	try:
		list(args)
		argsSTRING = str(args[0])
		print(argsSTRING)
		if argsSTRING == "ytho" or argsSTRING == "reee" or argsSTRING == "butytho" or argsSTRING == "eyebrows":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'ytho - links to http://imgur.com/gallery/yNlQWRM with high-res "y tho"' + "\n" + 'reee - links to http://imgur.com/Bog0DR1.gif with enraged pepe gif' + "\n" + 'butytho - links to custom made gif at http://i.imgur.com/fibCEus.gifv lovingly created by DJ-TrainR3k#4812' + "\n" + 'eyebrows - randomly selects between and links to https://i.imgur.com/YYnA64s.gif or https://i.imgur.com/M7HkE2t.gif```')
		elif argsSTRING == "hello":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'hello - test message, returns "Hello!" . . . what more is there to say?```')
		elif argsSTRING == "error":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'error - returns italicized "[ORRER}", lovingly inspired by DJ-TrainR3k#4812```')
		elif argsSTRING == "myeyes" or argsSTRING == "spam":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'myeyes - links to https://i.imgur.com/zlARfFy.gif with spongebob gif of burning eyeballs' + "\n" + 'can be duplicated up to five times to clear the visible chat of . . . unsavory images, using "$myeyes 1" through "$myeyes 5" for one through five images, respectively' + "\n" + 'also can be invoked using "$spam" with the same options, using "$spam 1" through "$spam 5" for one through five images, respectively```')
		else:
			await client.say('You fucked up.')
	except IndexError:
		await client.say(helpList[0] + "\n" + "\n" + helpList[1] + "\n" + helpList[2] + "\n" + helpList[3] + "\n" + "\n" + helpList[4] + "\n" + helpList[5] + "\n" + "\n" + helpList[6])

@client.command()	#test command
async def hello(*args):
	await client.say('Hello!')

@client.command()	#classic ytho response
async def ytho(*args):
	await client.say('http://i.imgur.com/yNlQWRM.jpg')

@client.command()	#reee
async def reee(*args):
	await client.say('http://imgur.com/Bog0DR1.gif')
	
@client.command()	#bytho
async def butytho(*args):
	await client.say('http://i.imgur.com/fibCEus.gifv')
	
@client.command()	#noneedtobeupset
async def noneedtobeupset(*args):
	await client.say('https://www.youtube.com/watch?v=eY52Zsg-KVI')

@client.command()	#trevor's bit
async def error(*args):
	await client.say("*[ORRER}*")
	
@client.command()	#eyebrows
async def eyebrows(*args):
	randomNum = random.random()
	if randomNum <= 0.5:
		await client.say('https://i.imgur.com/YYnA64s.gif')
	else:
		await client.say('https://i.imgur.com/M7HkE2t.gif')

count = 0

@client.command(aliases=['spam'])	#myeyes/spam response
async def myeyes(*args):
	print(args)
	global count
	try:
		list(args)
		argsINT = int(args[0])
		print(args)
		if argsINT <= 5:
			while count < argsINT:
				await client.say("https://i.imgur.com/zlARfFy.gif")
				count += 1
				print(count)
			else:
				count = 0
		else:
			await client.say("Too much!")
	except IndexError:
		await client.say("https://i.imgur.com/zlARfFy.gif")
		count = 0

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name="$commandhelp for help"))
	
client.run('client token here')