#Diemart
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime
from discord.utils import get
from discord.utils import find
import time
import os
import sys
import random
import string
import aiohttp
import aiofiles

class MyClient(discord.Client):
	async def on_ready(self):	
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')
		game = discord.Game("Flinchless Moony Doo")
		await self.change_presence(status=discord.Status.online, activity=game)
			
	# don't do drugs kids
	async def on_message(self, message):
		if isinstance(message.channel,discord.DMChannel):
			await message.channel.send("You hit yourself. Why, you may ask? Why not.")
		else:	
			if message.content.upper().startswith("!PING"):
				before = time.monotonic()
				origMsg = await message.channel.send("Pong!")
				ping = (time.monotonic() - before) * 1000
				await origMsg.edit(content="Pong! Took "+str(ping)+"ms to respond.")
			if message.content.upper().startswith("!MOONBALL"):
				if('office' in message.channel.name):
					rChance = random.randint(1,100)
					if(rChance >= 70):
						await message.channel.send("**BOING** <@"+str(message.author.id)+">'s moonball didn't hit anyone.")
					else:
						if(rChance < 70 and rChance >= 69):
							rChanceT = random.randint(1,100)
							if(rChanceT >= 66):
								await message.channel.send("**CRASH** <@"+str(message.author.id)+"> HAS BROKEN A LIGHT!")
								await message.channel.send(file=discord.File("C:\\Users\\UltraTechX\\Documents\\MOONBALL_BOT\\GavinReact.gif"))
							if(rChanceT >= 33 and rChanceT < 66):
								await message.channel.send("**CRASH** <@"+str(message.author.id)+"> HAS BROKEN A TV!")
								await message.channel.send(file=discord.File("C:\\Users\\UltraTechX\\Documents\\MOONBALL_BOT\\GavinReact.gif"))
							if(rChanceT < 33):
								await message.channel.send("**CRASH** <@"+str(message.author.id)+"> HAS BROKEN A MICROPHONE!")
								await message.channel.send(file=discord.File("C:\\Users\\UltraTechX\\Documents\\MOONBALL_BOT\\GavinReact.gif"))
						else:
							if(rChance < 69 and rChance >= 65):
								await message.channel.send("**OW** <@"+str(message.author.id)+"> has hit the developers! <@143478947621896192> and <@152573896732835840>")
							else:
								usercount = message.guild.members
								thuser = usercount[random.randint(0,len(usercount)-1)]
								while True:
									thuser = usercount[random.randint(0,len(usercount)-1)]
									if str(thuser.id) != "526491603930578965":
										if ("outside the office" in [y.name.lower() for y in thuser.roles]) == False:
											break
								if message.author.id == thuser.id:
									await message.channel.send("**THUNK** <@"+str(message.author.id)+"> hit themselves with a moonball!")
								else:
									await message.channel.send("**THUNK** <@"+str(message.author.id)+"> hit <@"+str(thuser.id)+"> with a moonball!")
			if message.content.upper().startswith("!CUMBALL"):
				if('office' in message.channel.name):
					rChance = random.randint(1,100)
					if(rChance >= 99):
						await message.channel.send("***disguisting***")
						await message.channel.send(file=discord.File("C:\\Users\\UltraTechX\\Documents\\MOONBALL_BOT\\CumBall.gif"))
					else:
						if(rChance >= 95 and rChance < 99):
							await message.channel.send("*ew*")
							await message.channel.send(file=discord.File("C:\\Users\\UltraTechX\\Documents\\MOONBALL_BOT\\GavinCum.png"))
						else:
							await message.channel.send("You sick fuck.")
			if message.content.upper().startswith("!MOONPROTECT"):
				if('office' in message.channel.name):
					if "outside the office" in [y.name.lower() for y in message.author.roles]:
						role = get(message.guild.roles, name='Outside The Office')
						if not role:
							await message.channel.send("Moonball opt-out role not found, please contact an administrator")
						else:
							await message.author.remove_roles(role, reason="Opted out of moonball bot")
							await message.channel.send("Re-opted into moonball bot pings")
					else:
						role = get(message.guild.roles, name='Outside The Office')
						if not role:
							await message.channel.send("Moonball opt-out role not found, please contact an administrator")
						else:
							await message.author.add_roles(role, reason="Opted into moonball bot")
							await message.channel.send("opted out of moonball bot pings")
		
client = MyClient()
client.run("TokenHere")