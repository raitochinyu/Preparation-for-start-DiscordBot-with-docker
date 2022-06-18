import asyncio
import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ["TOKEN"]


class Bot(commands.Bot):
  def __init__(self):
    intents = discord.Intents.default()
    intents.message_content = True
    super().__init__(
      command_prefix="r:", intents=intents
    )

  def on_ready(self):
    print(f"{self.bot.user.name}#{self.bot.user.discriminator}")


bot = Bot()

bot.command()
async def test(ctx):
  await ctx.send('動いてるよ')


async def Main():
  async with bot:
    await bot.start(TOKEN)


if __name__ == "__main__":
  asyncio.run(Main())
