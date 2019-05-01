import sys
import os

from discord.ext import commands
import discord

class Util_commands(commands.Cog, name='Utility commands'): 
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def die(self, ctx):
        """- Kill the process."""
        await ctx.send("My websocket connection will be closed, disconnecting me from the world, before `sys.exit()` rips me from existence. I hope this is what you wanted. Goodbye.")
        sys.exit()

    @commands.command()
    async def restart(self, ctx):
        """- Restart the process"""
        await ctx.send("I will now kill myself and reincarnate as a (hopefully) better bot. See you in a few seconds!")
        await self.bot.change_presence(status=discord.Status.idle)
        #await self.bot.close()
        os.execl(sys.executable, sys.executable, * sys.argv) 
