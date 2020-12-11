from time import sleep
import discord
import asyncio
from config import configDict

client = discord.Client()

async def status():
	for i in configDict["statuses"]:
		print(f"Defining status: {i[0]} : {i[1]}")
		
		await client.change_presence(status=discord.Status.idle, activity=discord.Activity(name="Custom Status", type=4, state=i[1], emoji={"name":i[0], "animated":False}))
		await asyncio.sleep(i[2])

@client.event
async def on_ready():
	print('Ready')
	while 1:
		await status()
	
client.run(configDict["token"], bot=False)