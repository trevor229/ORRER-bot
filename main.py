import discord
from discord.ext.commands import Bot
import asyncio
import random
import urllib.request

with open('key.txt', 'r') as myfile:
    TOKEN = myfile.read()

client = Bot(command_prefix="$")


@client.command()  # help command with detailed descriptions
async def commandhelp(*args):
    print(args)
    helpList = ['```[ORRER} Help Menu - All commands prefixed by "$"',
                'hello - test message, returns "Hello!"\n',
                'ytho, myeyes, reee, butytho, eyebrows, whyyoulikethis, noneedtobeupset - general response images\n',
                'error - returns signature error message',
                'defcon - current DEF:CON status\n',
                'alex - reaction_images.png',
				'trevor - reaction_images.png part deux',
                'weather - weather forecast/current conditions [WIP]'
                'Add command to "$commandhelp" to recieve additional info on that command.',
                'EX: $commandhelp ytho',
                'Written by 16ajans#6893 and Maintained by DJ-TrainR3k#4812```']
    try:
        list(args)
        argsSTRING = str(args[0])
        print(argsSTRING)
        if argsSTRING == "ytho" or argsSTRING == "reee" or argsSTRING == "butytho" or argsSTRING == "eyebrows" or argsSTRING == "whyyoulikethis" or argsSTRING == "noneedtobeupset" or argsSTRING == "alex" or argsSTRING == "trevor" or argsSTRING == "noneedtobeupset" or argsSTRING == "weather":
            await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' +
            "\n" + "\n" + 'ytho - links to http://imgur.com/gallery/yNlQWRM with high-res "y tho"' +
            "\n" + 'reee - links to http://imgur.com/Bog0DR1.gif with enraged pepe gif' +
            "\n" + 'butytho - links to custom made gif at http://i.imgur.com/fibCEus.gifv lovingly created by DJ-TrainR3k#4812' +
            "\n" + 'eyebrows - randomly selects between and links to https://i.imgur.com/YYnA64s.gif or https://i.imgur.com/M7HkE2t.gif' +
            "\n" + 'noneedtobeupset - links to https://www.youtube.com/watch?v=eY52Zsg-KVI 10 hour loop' +
            "\n" + 'whyyoulikethis - links to http://i.imgur.com/QhoSZWy.png' +
			"\n" + 'trevor - random trevor face. selectivity not implemented.' +
            "\n" + 'alex - random alex face. selectivity not yet implemented.' +
            "\n" + 'weather - weather forecast/current conditions [WIP].```')
        elif argsSTRING == "hello":
            await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' +
            "\n" + "\n" + 'hello - test message, returns "Hello!" . . . what more is there to say?```')
        elif argsSTRING == "defcon":
            await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' +
            "\n" + "\n" + 'defcon - current DEF:CON status . . . what more is there to say?```')
        elif argsSTRING == "alex":
            await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' +
            "\n" + "\n" + 'Meme images of the great King Autismonius.```')
        elif argsSTRING == "trevor":
            await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' +
            "\n" + "\n" + 'Meme images of Mr Autism Likely.```')
        elif argsSTRING == "weather":
            await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' +
            "\n" + "\n" + 'Weather conditions and other cool stuff. [WIP] ADD USAGE HERE```')
        elif argsSTRING == "error":
            await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' +
            "\n" + "\n" + 'error - returns italicized "[ORRER}", lovingly inspired by DJ-TrainR3k#4812```')
        elif argsSTRING == "myeyes" or argsSTRING == "spam":
            await client.say('```[ORRER} Help Menu - All commands prefixed by "$"' +
            "\n" + "\n" + 'myeyes - links to https://i.imgur.com/zlARfFy.gif with spongebob gif of burning eyeballs' +
            "\n" + 'can be duplicated up to five times to clear the visible chat of . . . unsavory images, using "$myeyes 1" through "$myeyes 5" for one through five images, respectively' +
            "\n" + 'also can be invoked using "$spam" with the same options, using "$spam 1" through "$spam 5" for one through five images, respectively```')
        else:
            await client.say('You fucked up. Use $commandhelp you tard.')
    except IndexError:
        await client.say(helpList[0] + "\n" + "\n" + helpList[1] + "\n" + helpList[2] + "\n" + helpList[3] + "\n" + "\n" + helpList[4] + "\n" + helpList[5] + "\n" + "\n" + helpList[6] + "\n" + helpList[7] + "\n" + "\n" + helpList[8] + "\n" + "\n" + helpList[9] + "\n" + "\n")


@client.command()  # test command
async def hello(*args):
    em = discord.Embed(title='My Embed Title',
                       description='My Embed Content.', colour=0xDEADBF)
    em.set_author(name='Someone', icon_url='https://i.imgur.com/I1nzRe5.png')
    await client.say(embed=em)


@client.command(pass_context=True)  # classic ytho response
async def ytho(ctx):
    await client.send_file(ctx.message.channel, 'pics/ytho.jpg')


@client.command(pass_context=True)  # reee
async def reee(ctx):
    await client.send_file(ctx.message.channel, 'pics/ree.gif')


@client.command(pass_context=True)  # butytho
async def butytho(ctx):
    await client.send_file(ctx.message.channel, 'pics/butytho.gif')


@client.command()  # defcon
async def defcon(*args):
    # Found from doing a little APK decompiling. Returns single byte.
    req = urllib.request.Request('http://www.defconwarningsystem.com/code.dat')
    with urllib.request.urlopen(req) as response:
        dcon = response.read().decode('utf-8')
        if dcon == "5":
            em = discord.Embed(
                description='There are no known imminent nuclear threats against the United States.', colour=0x00ff11)
            em.set_author(name='The current defcon status is 5. Condition Green',
                          icon_url='https://imgur.com/vua9XAP.png')
            await client.say(embed=em)
        else:
            if dcon == "4":
                em = discord.Embed(
                    description='No imminent nuclear threats to the US at this time, however, certain events are occuring in the world theater right now that require closer observation.', colour=0x002aff)
                em.set_author(name='The current defcon status is 4. Condition Blue',
                              icon_url='https://imgur.com/NXdWNNv.png')
                await client.say(embed=em)
            else:
                if dcon == "3":
                    em = discord.Embed(
                        description='Events of concern are occuring in the world theatre. There is no known immediate nuclear threat against the United States, however the situation is considered fluid.', colour=0xfffc00)
                    em.set_author(name='The current defcon status is 3. Condition Yellow',
                                  icon_url='https://imgur.com/kYQyX4D.png')
                    await client.say(embed=em)
                else:
                    if dcon == "2":
                        em = discord.Embed(
                            description='Hostilities have or are about to break out. There is the possibility of a nuclear strike against the United States.', colour=0xff6c00)
                        em.set_author(name='The current defcon status is 2. Condition Orange',
                                      icon_url='https://imgur.com/04Qc3yc.png')
                        await client.say(embed=em)
                        await client.say("PLEASE TAKE TIME TO READ AND PRINT THIS GUIDE TO NUCLEAR SURVIVAL: http://www.ki4u.com/guide.pdf")
                    else:
                        if dcon == "1":
                            em = discord.Embed(description='A nuclear attack against the United States is in progress or is considered to be highly likely. It is planned for the Alert level to go to Red before an actual attack. This will introduce a possibility of error, but will also give the most warning. You must decide for yourself whether to act upon it or not. Updates will be given at 7 A.M and 7 P.M Pacific Time with immediate updates issued as the situation warrants. Post-attack, radiation levels will be given for the Stevens and Ferry County areas as well as any other areas if possible. Updates for radiation will also be given at 7 A.M. and 7 P.M. Pacific Time. Immediate updates will be issued as the situation warrents.', colour=0xff0000)
                            em.set_author(name='The current defcon status is 1. Condition RED',
                                          icon_url='https://i.imgur.com/I1nzRe5.png')
                            await client.say(embed=em)
                            await client.say("IMMEDIATELY READ AND PRINT THIS GUIDE TO NUCLEAR SURVIVAL: http://www.ki4u.com/guide.pdf")


@client.command()  # noneedtobeupset
async def noneedtobeupset(*args):
    await client.say('https://www.youtube.com/watch?v=eY52Zsg-KVI')


@client.command(pass_context=True)  # trevor's bit
async def error(ctx):
    await client.say("*[ORRER}*")
    await client.send_file(ctx.message.channel, 'test.jpg')


@client.command(pass_context=True)  # why are you like this
async def whyyoulikethis(ctx):
    await client.send_file(ctx.message.channel, 'pics/why.jpg')


@client.command(pass_context=True)  # eyebrows
async def eyebrows(ctx):
    randNum = random.randint(0, 1)
    if randNum == 0:
        await client.send_file(ctx.message.channel, 'pics/eyebrows1.gif')
    else:
        await client.send_file(ctx.message.channel, 'pics/eyebrows2.gif')


@client.command(pass_context=True) # alex
async def alex(ctx, alexNum=0):
        picNum = int(alexNum)
        if picNum == 0:
            randNum = random.randint(3, 72)
            await client.send_file(ctx.message.channel, '16ajans/Picture_%s.jpg' % randNum)
            await client.say('<@!144973321749004289>')
        elif picNum >= 3 and picNum <= 72:
                await client.send_file(ctx.message.channel, '16ajans/Picture_%s.jpg' % picNum)
                await client.say('<@!144973321749004289>')
        else:
            await client.say("Invalid Picture Number! Valid Numbers Are 3 through 72")


@client.command(pass_context=True) # trevor
async def trevor(ctx, *, trevorNum=0):
    picNum2 = int(trevorNum)
    if picNum2 == 0:
        randNum = random.randint(1, 24)
        await client.send_file(ctx.message.channel, 'trevor/%s.jpg' % randNum)
        await client.say('<@!144962858503897089>')
    elif picNum2 >= 1 and picNum2 <= 24:
            await client.send_file(ctx.message.channel, 'trevor/%s.jpg' % picNum2)
            await client.say('<@!144962858503897089>')
    else:
        await client.say("Invalid Picture Number! Valid Numbers Are 1 through 24")


count = 0
@client.command(aliases=['spam'])  # myeyes/spam response
async def myeyes(*args):
    print(args)
    global count
    try:
        list(args)
        argsINT = int(args[0])
        print(args)
        if argsINT <= 5:  # for mild fuck ups

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


@client.group(pass_context=True)
async def weather(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say('Work in progress.')

#@weather.command()
#async def push(remote: str, branch: str):
#    await bot.say('Pushing to {} {}'.format(remote, branch))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="$commandhelp for help"))

client.run(TOKEN)
