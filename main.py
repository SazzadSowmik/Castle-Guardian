import os
import discord
import nacl
from discord.ext import commands
from keep_alive import keep_alive
import youtube_dl
from music_bot import YTDLSource
from music_cog import music_cog
from taskFormat_cog import taskFormat_cog

#intents = discord.Intents().all()
# client = discord.Client()

Client = discord.client
bot = commands.Bot(command_prefix="m@a ")
Clientdiscord = discord.Client()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


#just a simple bot response
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # Simple Command here
    if message.content == 'm@a':
        if message.author.name == 'Capt_Sazzz':
            res = 'Yes ' + message.author.name + ' the Great , your majesty!'
            await message.channel.send(res)
        else:
            res = 'Yes ' + message.author.name + ' , How can I help you?'
            await message.channel.send(res)

    await bot.process_commands(message)
  

# for Join the channel which also checks messanger is connected a voice or not
@bot.command(name='join', help="--To connect me with your voice channel")
async def join(message):
  if not message.author.voice:
    await message.channel.send("{}, please have a seat somewhere, Sire! I'll join there.".format(message.author.name))
  else:
    channel = message.author.voice.channel
    voice = discord.utils.get(message.guild.voice_channels, name=channel.name)
    voice_client = discord.utils.get(bot.voice_clients,guild=message.guild)
    if voice_client == None:
      await voice.connect()
      await message.channel.send("Joined! Pleasure to join with you.")
    else:
      await voice_client.move_to(channel)
      await message.channel.send("Settle down! I am here.")


# voice disconnected
@bot.command(name='leave', help="--Am I disturbing? Let me leave you alone.")
async def leave(message):
    if message.author.voice:
        voice_client = discord.utils.get(bot.voice_clients,
                                         guild=message.guild)
        if voice_client != None:
            await voice_client.disconnect()
            await message.channel.send("Farewell.")
        else:
            await message.channel.send("Haven't joined with you, Sire!")

    elif not message.author.voice:
        await message.channel.send("Sire, Haven't seen any party yet!")



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
      await ctx.send("Pardon, I am not suppose to do that, Sire. Use 'm@a help' commad to see my work!")
    elif isinstance(error, commands.CommandOnCooldown):
      await ctx.send(f'This command is on cooldown. Please wait {error.retry_after:.2f}s')
    elif isinstance(error, commands.MissingPermissions):
      await ctx.send('You do not have the permissions to use this command.')
    elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please fulfil the command your highness!')
      

@bot.command(name='type', help='--want me to type something?use quotation for space separated sentence')
async def type(ctx, arg):
    await ctx.send(arg)


#bot.add_cog(music_cog(bot))
bot.add_cog(taskFormat_cog(bot))


keep_alive()
bot.run(os.environ['TOKEN'])
