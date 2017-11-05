"""Module containing the Discord bot functionality."""

import asyncio
from os import getenv

import discord
from discord.enums import ChannelType

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(
            message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!create.character'):
        if message.channel.type == ChannelType.private:
            await client.send_message(
                message.channel,
                "This would normally begin the character creation process, "
                "but the developer is tired and lazy")
        else:
            await client.send_message(
                message.channel,
                "You will be PM'd shortly to begin the character creation "
                "process.")
            await client.send_message(
                message.author,
                "This would normally begin the character creation process, "
                "but the developer is tired and lazy")

client.run(getenv('DISCORD_TOKEN'))
