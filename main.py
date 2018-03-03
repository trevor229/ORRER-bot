import discord
from discord.ext.commands import Bot
import asyncio
import random
import urllib.request


#output_directory = '/home/megumin/discord_bots/ORRER-Bot'

client = Bot(command_prefix="$")

#####################################################################################
##               FOR FUCKS SAKE PLEASE REMOVE THE TOKEN BEFORE PUSHING!            ##
#####################################################################################

@client.command()	#help command with detailed descriptions
async def commandhelp(*args):
	print(args)
	helpList = ['```[ORRER} Help Menu - All commands prefixed by "$"',
			'hello - test message, returns "Hello!"',
			'ytho, myeyes, reee, butytho, eyebrows, whyyoulikethis, noneedtobeupset - general response images',
			'error - returns signature error message',
			'defcon - current DEF:CON status',
			'alex - reaction_images.png',
			'Add command to "$commandhelp" to recieve additional info on that command.',
			'EX: $commandhelp ytho',
			'Written by 16ajans#6893 and Maintained by DJ-TrainR3k#4812```']
	try:
		list(args)
		argsSTRING = str(args[0])
		print(argsSTRING)
		if argsSTRING == "ytho" or argsSTRING == "reee" or argsSTRING == "butytho" or argsSTRING == "eyebrows" or argsSTRING == "whyyoulikethis" or argsSTRING == "noneedtobeupset":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'ytho - links to http://imgur.com/gallery/yNlQWRM with high-res "y tho"' + "\n" + 'reee - links to http://imgur.com/Bog0DR1.gif with enraged pepe gif' + "\n" + 'butytho - links to custom made gif at http://i.imgur.com/fibCEus.gifv lovingly created by DJ-TrainR3k#4812' + "\n" + 'eyebrows - randomly selects between and links to https://i.imgur.com/YYnA64s.gif or https://i.imgur.com/M7HkE2t.gif' + "\n" + 'noneedtobeupset - links to https://www.youtube.com/watch?v=eY52Zsg-KVI 10 hour loop' + "\n" + 'whyyoulikethis - links to http://i.imgur.com/QhoSZWy.png```')
		elif argsSTRING == "hello":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'hello - test message, returns "Hello!" . . . what more is there to say?```')
		elif argsSTRING == "defcon":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'defcon - current DEF:CON status . . . what more is there to say?```')
		elif argsSTRING == "alex":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'Meme images.```')
		elif argsSTRING == "error":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'error - returns italicized "[ORRER}", lovingly inspired by DJ-TrainR3k#4812```')
		elif argsSTRING == "myeyes" or argsSTRING == "spam":
			await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' + "\n" + "\n" + 'myeyes - links to https://i.imgur.com/zlARfFy.gif with spongebob gif of burning eyeballs' + "\n" + 'can be duplicated up to five times to clear the visible chat of . . . unsavory images, using "$myeyes 1" through "$myeyes 5" for one through five images, respectively' + "\n" + 'also can be invoked using "$spam" with the same options, using "$spam 1" through "$spam 5" for one through five images, respectively```')
		else:
			await client.say('You fucked up.')
	except IndexError:
		await client.say(helpList[0] + "\n" + "\n" + helpList[1] + "\n" + helpList[2] + "\n" + helpList[3] + "\n" + "\n" + helpList[4] + "\n" + helpList[5] + "\n" + "\n" + helpList[6] + "\n" + helpList[7] + "\n" + "\n" + helpList[8] + "\n"+ "\n")

@client.command()	#test command
async def hello(*args):
    em = discord.Embed(title='My Embed Title', description='My Embed Content.', colour=0xDEADBF)
    em.set_author(name='Someone', icon_url='https://i.imgur.com/I1nzRe5.png')
    await client.say(embed=em)

@client.command()	#classic ytho response
async def ytho(*args):
	await client.say('http://i.imgur.com/yNlQWRM.jpg')

@client.command()	#reee
async def reee(*args):
	await client.say('http://imgur.com/Bog0DR1.gif')

@client.command()	#butytho
async def butytho(*args):
	await client.say('http://i.imgur.com/fibCEus.gifv')

@client.command()	#defcon
async def defcon(*args):
    req = urllib.request.Request('http://www.defconwarningsystem.com/code.dat') # Found from doing a little APK decompiling. Returns single byte.
    with urllib.request.urlopen(req) as response:
        dcon = response.read().decode('utf-8')
        if dcon == "5":
            em = discord.Embed(description='There are no known imminent nuclear threats against the United States.', colour=0x00ff11)
            em.set_author(name='The current defcon status is 5. Condition Green', icon_url='https://imgur.com/vua9XAP.png')
            await client.say(embed=em)
        else:
            if dcon == "4":
                em = discord.Embed(description='No imminent nuclear threats to the US at this time, however, certain events are occuring in the world theater right now that require closer observation.', colour=0x002aff)
                em.set_author(name='The current defcon status is 4. Condition Blue', icon_url='https://imgur.com/NXdWNNv.png')
                await client.say(embed=em)
            else:
                if dcon == "3":
                    em = discord.Embed(description='Events of concern are occuring in the world theatre. There is no known immediate nuclear threat against the United States, however the situation is considered fluid.', colour=0xfffc00)
                    em.set_author(name='The current defcon status is 3. Condition Yellow', icon_url='https://imgur.com/kYQyX4D.png')
                    await client.say(embed=em)
                else:
                    if dcon == "2":
                        em = discord.Embed(description='Hostilities have or are about to break out. There is the possibility of a nuclear strike against the United States.', colour=0xff6c00)
                        em.set_author(name='The current defcon status is 2. Condition Orange', icon_url='https://imgur.com/04Qc3yc.png')
                        await client.say(embed=em)
                        await client.say("PLEASE TAKE TIME TO READ AND PRINT THIS GUIDE TO NUCLEAR SURVIVAL: http://www.ki4u.com/guide.pdf")
                    else:
                        if dcon == "1":
                            em = discord.Embed(description='A nuclear attack against the United States is in progress or is considered to be highly likely. It is planned for the Alert level to go to Red before an actual attack. This will introduce a possibility of error, but will also give the most warning. You must decide for yourself whether to act upon it or not. Updates will be given at 7 A.M and 7 P.M Pacific Time with immediate updates issued as the situation warrants. Post-attack, radiation levels will be given for the Stevens and Ferry County areas as well as any other areas if possible. Updates for radiation will also be given at 7 A.M. and 7 P.M. Pacific Time. Immediate updates will be issued as the situation warrents.', colour=0xff0000)
                            em.set_author(name='The current defcon status is 1. Condition RED', icon_url='https://i.imgur.com/I1nzRe5.png')
                            await client.say(embed=em)
                            await client.say("IMMEDIATELY READ AND PRINT THIS GUIDE TO NUCLEAR SURVIVAL: http://www.ki4u.com/guide.pdf")

@client.command(pass_context=True)
async def alex(ctx):
    await client.send_message(ctx.message.user, 'Watchout for that truck!')

@client.command()	#noneedtobeupset
async def noneedtobeupset(*args):
	await client.say('https://www.youtube.com/watch?v=eY52Zsg-KVI')

@client.command()	#trevor's bit
async def error(*args):
	await client.say("*[ORRER}*")

@client.command()	#why are you like this
async def whyyoulikethis(*args):
	await client.say("http://i.imgur.com/QhoSZWy.png")

@client.command()	#eyebrows
async def eyebrows(*args):
	randNum = random.randint(0, 1)
	if randNum == 0:
		await client.say('https://i.imgur.com/YYnA64s.gif')
	else:
		await client.say('https://i.imgur.com/M7HkE2t.gif')

#@client.command() #trevor's random anime command
#async def anime(*args):
#	print(random

count = 0

@client.command(aliases=['spam'])	#myeyes/spam response
async def myeyes(*args):
	print(args)
	global count
	try:
		list(args)
		argsINT = int(args[0])
		print(args)
<<<<<<< HEAD
<<<<<<< HEAD
		if argsINT <= 5:
=======
		if argsINT <= 5: #for mild fuck ups
>>>>>>> 3ec3bd0827aee67811c0758408d8dee92109075b
=======
		if argsINT <= 5: #for mild fuck ups
>>>>>>> 3ec3bd0827aee67811c0758408d8dee92109075b
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

#@client.command()	#reddit copypasta insult, not in help list, requires argument, normally a mention
#async def ultinsult(*args):
#	print(args)
#	try:
#		list(args)
#		argsSTRING = str(args[0])
#		print(argsSTRING)
#		await client.say(argsSTRING + " You swine. You vulgar little maggot. You worthless bag of filth. I wager you couldn't empty a boot of excrement were the instructions on the heel. You are a canker. A sore that won't go away. I would rather kiss a lawyer than be seen with you. Try to edit your responses of unnecessary material before attempting to impress us with your insight. The evidence that you are a nincompoop will still be available to readers, but they will be able to access it more rapidly.")
#		await client.say(argsSTRING + " You snail-skulled little rabbit. Would that a hawk pick you up, drive its beak into your brain, and upon finding it rancid set you loose to fly briefly before spattering the ocean rocks with the frothy pink shame of your ignoble blood. May you choke on the queasy, convulsing nausea of your own trite, foolish beliefs. You are weary, stale, flat and unprofitable. You are grimy, squalid, nasty and profane. You are foul and disgusting. You're a fool, an ignoramus.")
#		await client.say(argsSTRING + " And what meaning do you expect your delusional self-important statements of unknowing, inexperienced opinion to have to us who think and reason? What fantasy do you hold that you would believe that your tiny-fisted tantrums would have more weight than that of a leprous desert rat, spinning rabidly in a circle, waiting for the bite of the snake? You are a waste of flesh.")
#		await client.say(argsSTRING + " You have no rhythm. You are ridiculous and obnoxious. You are the moral equivalent of a leech. You are a living emptiness, a meaningless void. You are sour and senile. You are a disease, you puerile one-handed slack-jawed , drooling meatslapper. You smarmy lagerlout git. You bloody woofter sod. Bugger off, pillock. You grotty wanking oik artless base-court apple-john. You clouted boggish foot-licking twit. You dankish clack-dish plonker. You gormless crook-pated tosser. You churlish boil-brained clotpole ponce. You cockered bum-bailey poofter. You gob-kissing gleeking flap-mouthed coxcomb. You dread-bolted fobbing beef-witted clapper-clawed flirt-gill.")
#		await client.say(argsSTRING + " You are a fiend and a coward, and you have bad breath. You are degenerate, noxious and depraved. I feel debased just for knowing you exist. I despise everything about you, and I wish you would go away. I cannot believe how incredibly stupid you are. I mean rock-hard stupid. Dehydrated-rock-hard stupid. Stupid so stupid that it goes way beyond the stupid we know into a whole different dimension of stupid. You are trans-stupid stupid. Meta-stupid. Some pure essence of a stupid so uncontaminated by anything else as to be beyond the laws of physics that we know. I'm sorry. I can't go on.")
#		await client.say(argsSTRING + " This is an epiphany of stupid for me. After this, you may not hear from me again for a while. I don't have enough strength left to deride your ignorant questions and half-baked comments about unimportant trivia, or any of the rest of this drivel. Duh. I mean, really, stringing together a bunch of insults among a load of babbling was hardly effective. True, these are rudimentary skills that many of us 'normal' people take for granted that everyone has an easy time of mastering. But we sometimes forget that there are 'challenged' persons in this world who find these things more difficult. If I had known, that this was your case then I would have never read your post. It just wouldn't have been 'right'. Sort of like parking in a handicap space. I wish you the best of luck in the emotional, and social struggles that seem to be placing such a demand on you.")
#		await client.say(argsSTRING + " You're an idiot. A moron of the highest order. You're so stupid it's a wonder and a pity you can remember to breath. Intelligent ideas bounce off your head as if it were coated with teflon. Creative thoughts take alternate transportation in order to avoid even being in the same state as you. If you had an original thought it would die of loneliness before the hour was out. On an intelligence scale of 1 to 10 (10 corresponding to the highest attainable IQ) you're rating is so far into negative numbers that one would need to travel into another quantum reality in order to even catch a distant glimpse of it.")
#		await client.say(argsSTRING + " Your personality is that of a rabid Chihuahua intent on destroying its own tail. Your powers of observation are akin to those of the bird that keeps slamming into the picture window trying to get that other bird it keeps seeing. You are walking, talking proof that you don't have to be sentient to survive, and that Barnum was thinking of you when he uttered his immortal phrase regarding the birth of a sucker. You are, at varying times, tedious, boring, and even occasionally earth shatteringly hilarious in your idiocy, routinely childish, moronic, pathetic, wretched, disgusting and pitiful.")
#		await client.say(argsSTRING + " You are wholly without any redeeming social grace or value. If God ever decides to give the planet an enema you'd better run like the wind because anywhere you stand is a suitable place for The Insertion. There is no animal so disgusting, so vile that it deserves comparison to you, for even the lowest, dirtiest, most parasitic member of the animal kingdom fills an ecological niche. You fill no niche. To call you a parasite would be injurious and defamatory to the thousands of honest parasitic species. You are worse than vermin, for vermin do not pretend to be what it is not. You are truly human garbage. You are a fraudulent, lying, predatory charlatan. You are of less worth than a burnt-out light bulb. You will forever live in shame.")
#		await client.say(argsSTRING + " You have nothing to say, and Godwin's Law does not apply when writing about you. You are the anti-Midas, for all that you touch becomes valueless and unusable. Mothers gather their children close when you appear. You are an aberration, a corruption, and a boil that needs to be lanced. You are a poison in need of being vomited. You are a tooth so rotten it infects the whole body. You are sperm that should have been captured in a condom and flushed down a toilet. I don't like you. I don't like anybody who has as little respect for others as you do. Go away, you swine. You're a putrescent mass, a walking vomit. You are a spineless little worm deserving nothing but the profoundest contempt. You are a jerk, a cad, and a weasel. Your life is a monument to stupidity. You are a stench, a revulsion, a big suck on a sour lemon. You are a curdled staggering mutant dwarf smeared richly with the effluvia and offal accompanying your alleged birth into this world. Meaningful to no one, abandoned by the puke-drooling, giggling beasts that sired you and then killed themselves in recognition of what they had done.")
#		await client.say(argsSTRING + " I will never get over the embarrassment of belonging to the same species as you. You are a monster, an ogre, a malformity. I wretch at the very thought of you. You have all the appeal of a paper cut. Lepers avoid you. You are vile, worthless, less than nothing. You are a weed, a fungus, and the dregs of this earth. And did I mention you smell? Monkeys look down on you. Even sheep won't have sex with you. You are unreservedly pathetic, starved for attention, and lost in a land that reality forgot. You are a waste of flesh. On a good day you're a halfwit. You are deficient in all that lends character. You have the personality of wallpaper. You are dank and filthy. You are asinine and benighted. You are the source of all unpleasantness. You spread misery and sorrow wherever you go.")
#		await client.say(argsSTRING + " You are a fiend and a coward, and you have bad breath. You are degenerate, noxious and depraved. I feel debased just for knowing you exist. I despise everything about you, and I wish you would go away. I cannot believe how incredibly stupid you are. The only thing worse than your logic is your manners. Maybe later in life, after you have learned to read, write, study, spell, and count, you will have more success. True, these are rudimentary skills that many of us 'normal' people take for granted that everyone has an easy time of mastering. It just wouldn't have been 'right'. Sort of like parking in a handicap space. I wish you the best of luck in the emotional, and social struggles that seem to be placing such a demand on you.")
#		await client.say(argsSTRING + " You are hypocritical, greedy, violent, malevolent, vengeful, cowardly, deadly, mendacious, meretricious, loathsome, despicable, belligerent, opportunistic, barratrous, contemptible, criminal, fascistic, bigoted, racist, sexist, avaricious, tasteless, idiotic, brain-damaged, imbecilic, insane, arrogant, deceitful, demented, lame, self-righteous, byzantine, conspiratorial, satanic, fraudulent, libellous, bilious, splenetic, spastic, ignorant, clueless, illegitimate, harmful, destructive, dumb, evasive, double-talking, devious, revisionist, narrow, manipulative, paternalistic, fundamentalist, dogmatic, idolatrous, unethical, cultic, diseased, suppressive, controlling, restrictive, malignant, deceptive, dim, crazy, weird, dystrophic, stifling, uncaring, plantigrade, grim, unsympathetic, jargon-spouting, censorious, secretive, aggressive, mind-numbing, abrasive, poisonous, flagrant, self-destructive, abusive, and socially-retarded. Shut up and go away lest you achieve the physical retribution your behaviour merits. Thank you for your kind attention to and expected cooperation in this matter.ï»¿")
#	except IndexError:
#		await client.say("Try again, idiot.")

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	await client.change_presence(game=discord.Game(name="$commandhelp for help"))

client.run('TOKEN')
