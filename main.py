import discord
import os

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('hi cribot'):
		await message.channel.send('leave me alone im not ready yet')

client.run(os.environ.get('DISCORD_TOKEN'))