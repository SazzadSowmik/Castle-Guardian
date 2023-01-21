import discord
import asyncio
from discord.ext import commands
import os
import requests

class open_ai_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.api_key = os.environ['OPEN_AI_API']
    self.model = "text-davinci-003"
    
  @commands.command(name="bigbrain", help="--Sire, my Artificial Intelligent Mode is on @open_ai.")
  async def bigbrain(self, ctx):
    
    while True:
      ###############---Taking Promt and waiting for timeout---#################
      await ctx.send("What do you want to know Sire?")
      def check(m: discord.Message):
        return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
      try:
        msg = await self.bot.wait_for('message', check = check, timeout = 30.0)
        prompt = msg.content
        response = requests.post(
          f"https://api.openai.com/v1/engines/{self.model}/completions",
          headers={
              "Content-Type": "application/json",
              "Authorization": f"Bearer {self.api_key}",
          },
          json={
              "prompt": prompt,
              "max_tokens": 512,
          },
        )
  
        response_text = response.json()["choices"][0]["text"]
        await ctx.send(response_text)
        
      except asyncio.TimeoutError: 
        await ctx.send(f"**{ctx.author}**, No Question asked in given time. Timeout!")
        return
      ############################---Done taking promt---####################################
    
    
    