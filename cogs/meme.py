import random
import urllib.request
import json
import discord
from discord.ext import commands

import config as cfg

class Meme(commands.Cog, name='Memes'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='meme')
    async def getmeme(self, ctx, meme_type=None):
        """[google] - Fetch a meme from the internet."""
        message = ""
        if meme_type is None:
            message += "Meme type not specified. Defaulting to `{}` ".format(cfg.DEFAULT_MEME_TYPE)
            meme_type = cfg.DEFAULT_MEME_TYPE

        if meme_type == 'google':
            q = random.choice(cfg.GOOGLE_MEME_SEARCH_QUERIES)
            num = 1
            start = random.randint(1, 100)
            api_url = "https://www.googleapis.com/customsearch/v1?searchType=image&imgSize=medium&q={q}&num={num}&start={start}&key={key}&cx={cx}"
            formatted_url = api_url.format(q=q, num=num, start=start, key=cfg.GOOGLE_CUSTOM_SEARCH_KEY, cx=cfg.GOOGLE_CUSTOM_SEARCH_ID)
            req = urllib.request.Request(formatted_url)
            res = urllib.request.urlopen(req).read()
            data = json.loads(res.decode('utf-8'))
            image_url = data['items'][0]['link']
            message += image_url
             
        else:
            message +=" `{}` is not a supported meme type. ".format(meme_type)

        await ctx.send(message)

        
