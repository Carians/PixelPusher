import discord
import engine as cmd

# Settings
DEBUG = False
LOGGING = False
LOGGING_LEVEL = 'INFO'

# Discord
DISCORD_TOKEN = 'YOUR_TOKEN'
class DiscordBot:

    def __init__(self, name, token):
        if DEBUG:
            print('Initializing PixelPusher')
        self.name = name or 'PixelPusher'
        self.start(token)
    def start(self, DISCORD_TOKEN):
        self.client = discord.Client(intents=discord.Intents.default())
        self.client.run(DISCORD_TOKEN)


    async def on_message(self, message):
        if DEBUG:
            print('We have received a message from {0.author}: {0.content}'.format(message))
        if message.content.startswith in cmd.commands:
            await commands.execute(message.content, message)


if __name__ == '__main__':
    PixelPusher = DiscordBot('PixelPusher', DISCORD_TOKEN)