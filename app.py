import discord
import yaml
import aiohttp

config = yaml.safe_load(open('./config.yaml'))
channel_ids = [ids.get('id') for ids in config['channels']]
channel_webhooks = [ids.get('webhook') for ids in config['channels']]

intents = discord.Intents(messages=True, message_content=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('bot is ready.')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id in channel_ids:
        msg_guild_index = channel_ids.index(message.channel.id)
        webhooks = [i for i in channel_webhooks]
        del webhooks[msg_guild_index]

        for url in webhooks:
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(url, session=session)
                await webhook.send(message.content, username=message.author.name, avatar_url=message.author.display_avatar.url)

client.run(config['discord_token'])
