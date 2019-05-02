import discord
from discord.ext import commands

import config as cfg

class Meme(commands.Cog, name='Memes'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='meme')
    async def getmeme(self, ctx, meme_type=None):
        if meme_type is None:
            meme_type = cfg.DEFAULT_MEME_TYPE

        
        
