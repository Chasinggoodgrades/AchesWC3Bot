import os
import discord
import commands
import asyncio
import wc3maps

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)


async def repeat():
    channel = bot.get_channel(1119036476311744622)
    msg = await channel.fetch_message(1119036957931077753)
    while (1):
        sleepSeconds = 30 
        print(f"sleep for {sleepSeconds} seconds")
        content = wc3maps.map_search("rkr")
        if (len(content) == 0):
          pass
        else:
          await msg.edit(content=content)
          await(asyncio.sleep(sleepSeconds))  # snooze till the magic number

async def sendMsg(msg, userMsg):
  try: 
    response = commands.handle(userMsg)
    await msg.channel.send(response)

  except Exception as e:
    print(e)
    await msg.channel.send('Sorry, I don\'t understand that commands')


def run():

  @bot.event
  async def on_ready():
    activity = discord.Game(name="Warcraft III", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    await repeat()
    
  
  @bot.event
  async def on_message(message):
    if message.author == bot.user:
      return

    user = str(message.author)
    channel = str(message.channel)
    userMsg = str(message.content)

    print(f"{user} said: '{userMsg}' ({channel})")

    if userMsg[0] == '?':
      userMsg = userMsg[1:]
      await sendMsg(message, userMsg)

    

  my_secret = os.environ['API_KEY']
  bot.run(my_secret)
  
run()