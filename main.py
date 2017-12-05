import discord
from discord.ext import commands


class Main:
    """General Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self):
        """Basic Ping Command"""
        await self.bot.say(':ping_pong: Pong!')


def setup(bot):
    bot.add_cog(Main(bot))
