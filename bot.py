import discord

TOKEN = 'insert-your-discord-bot-token'

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('!lightshot'):
        msg = str(message.channel)
        randomurlString = string.ascii_lowercase + string.digits
        randomizing = ''.join(random.choice(randomurlString) for i in range(6))
        url = "https://prnt.sc/" + str(randomizing)
        await message.channel.send(url)

client.run(TOKEN)
