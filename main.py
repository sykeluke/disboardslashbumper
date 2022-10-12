import os
import asyncio
import random
import time
import sys
import threading

import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import file

try:
    __import__("discum")
    import discum
    from discum.utils.slash import SlashCommander
    from discum.utils.button import Buttoner
except ImportError:
    os.system(
        "python -m pip install --upgrade git+https://github.com/Merubokkusu/Discord-S.C.U.M.git#egg=discum"
    )
    import discum
    from discum.utils.slash import SlashCommander
    from discum.utils.button import Buttoner

intents = discord.Intents().all()
intents.members = True

token = os.environ["token"]
bot = commands.Bot(command_prefix='#!@#&^!!(@%$!&!@$!@%!@#%%^$#^&',
                   intents=intents,
                   self_bot=True)
disbot = discum.Client(token=token, log=False)
bot.remove_command("help")

guildID = os.environ["guild_id"]
channelID = os.environ["channel_id"]
botID = "302050872383242240"

def gtway():
    disbot.gateway.run()


def gtwaythread():
    x = threading.Thread(target=gtway)
    x.start()


@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.offline)
  print(f"\n{bot.user}\n")
  loop.start()

count = 0
data = None

@tasks.loop(minutes = random.randint(121,125))
async def loop():
  global count
  global data
  disbot.triggerSlashCommand(botID, channelID=channelID, guildID=guildID, data=data, sessionID=disbot.gateway.session_id)
  channel = await bot.fetch_channel(channelID)
  count+=1
  print(f"\n[ {count} ] Bump Sent in {channel.name}!\n")


def slashCommand(resp, guildID, channelID, botID):
  global data
  if resp.event.ready_supplemental:
    disbot.gateway.request.searchSlashCommands(guildID, limit=10, query="bump")
  if resp.event.guild_application_commands_updated:
    disbot.gateway.removeCommand(slashCommand)
    slashCmds = resp.parsed.auto()['application_commands']
    s = SlashCommander(slashCmds, application_id=botID)
    data = s.get(['bump'])



disbot.gateway.command(
	{
		"function": slashCommand,
		"params": {"guildID": guildID, "channelID": channelID, "botID": botID},
	}
)



if __name__ == "__main__":
    gtwaythread()
    bot.run(token, bot=False)
