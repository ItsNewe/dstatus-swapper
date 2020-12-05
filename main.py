import json
from time import sleep
import discord
from discord.ext import tasks

t=None
client = discord.Client()
statusList=[]

with open("./config.json", "r") as f:
	jsonRaw= json.load(f)
	t=jsonraw["token"]

	for i in jsonRaw["statuses"]:
		statusList.append((i[0], i[1]))

@tasks.loop(seconds=1)
async def status():
	print("Status loop: Index 0")
	for i in statusList:
		print(f"Defining status: {i[0]")
		await client.change_presence(status=discord.Status.idle, activity=discord.Activity(name="Custom status", type=4, state=i[0]))
		sleep(int(i[1]))

@client.event
async def on_ready():
	print('Ready')
	status.start()
	
client.run(t, bot=False)