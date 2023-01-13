import discord
from discord.ext import commands
from engine import commands as cmd

# Settings
DEBUG = True

# Discord
DISCORD_TOKEN = 'YOUR_TOKEN'
class DiscordBot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.commands = cmd.commands()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author == self.user:
            return "pain"

        if message.content in self.commands.commands:
            await self.send_message(message.channel, self.commands.commands[message.content]())
            print("Command executed: " + message.content)

    def send_message(self, channel, message):
        return channel.send(message)

if __name__ == '__main__':
    intends = discord.Intents.default()
    intends.message_content = True
    PixelPusher = DiscordBot(intents=intends)
    PixelPusher.run(str(DISCORD_TOKEN))