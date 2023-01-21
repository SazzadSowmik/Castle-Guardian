import discord
import asyncio
from discord.ext import commands

class taskFormat_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    
  @commands.command(name="task", help="--Sire, I'll help you to rearrange your task in a arranged formate.")
  async def tsk(self, ctx):
    taskNumber = 0
    taskDict = []
    while True:
      taskNumber = taskNumber + 1
      individualTask = []
      await ctx.send("Task Name?")
      ###############---Taking message and waiting for timeout---#################
      def check(m: discord.Message):
          return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
      try:
        msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
        if msg.content == "close":
          total_hour = 0
          total_minutes = 0
          await ctx.send("Generating your Report...\n---------------------------------------------------------------")
          for task in taskDict:
            for idx in task:
              for i in idx:
                if i == "Task Name":
                  await ctx.send("Task Name         :  {}".format(idx[i]))
                  # await ctx.send("{0}          : {1}".format(i,idx[i]))
                if i == "Agenda":
                  await ctx.send("Agenda               :  {}".format(idx[i]))
                if i == "Outcome":
                  await ctx.send("Outcome            :  {}".format(idx[i]))
                if i == "Hours":
                  hr = int(idx[i])
                if i == "Minutes":
                  min = int(idx[i])
                  if min >= 60:
                    hr = hr+int(min/60)
                    min = min%60
                  total_hour = total_hour + hr
                  total_minutes = total_minutes + min
                  await ctx.send("Hours of Work  :  {} hour(s) {} minute(s)".format(hr,min))
                if i == "Status":
                  await ctx.send("Status                  :  {}".format(idx[i]))
                if i == "Issue":
                  await ctx.send("Issue                    :  {}".format(idx[i]))
                if i == "Percent":
                  await ctx.send("Completed         :  {}% of this work".format(idx[i]))
                
                  
              # await ctx.send("Task Name    :  {}".format(idx[i]))
              # await ctx.send("Hours of Work: {}".format(idx["Hours"]))
              # await ctx.send("Hours of Work: {} hours {} minutes".format(idx["Hours"], idx["Minutes"]))
              
              # await ctx.send("Agenda: {}".format(idx["Agenda"]))
            await ctx.send("---------------------------------------------------------------")
            #await ctx.send()
          #await ctx.send(taskDict)
          if total_minutes >= 60:
            total_hour = total_hour+int(total_minutes/60)
            total_minutes = total_minutes%60
          await ctx.send("Total Hours          : {} hour(s) {} minute(s)".format(total_hour, total_minutes))
          
          return
      except asyncio.TimeoutError: 
        await ctx.send(f"**{ctx.author}**, No Task Name has input in given time. Timeout!")
        return
      ############################---Done taking message---####################################
        
      else:
        individualTask.append({"Task Name": msg.content})
        task = msg.content
        task = task.lower()
        term = "meeting"
        
        taskName = task.split() 

        if term in taskName: 
          await ctx.send("Agenda?")

          ###############---Taking message and waiting for timeout---#################
          def check(m: discord.Message):
              return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
          try:
            msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
          except asyncio.TimeoutError: 
            await ctx.send(f"**{ctx.author}**, No Agenda of meeting has input in given time. Timeout!")
            return
          else:
            individualTask.append({"Agenda": msg.content})
            await ctx.send(f"**{ctx.author}**, Your agenda was {msg.content}!")
          ############################---Done taking message---####################################

          await ctx.send("Outcome?")
          
          ###############---Taking message and waiting for timeout---#################
          def check(m: discord.Message):
              return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
          try:
            msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
          except asyncio.TimeoutError: 
            await ctx.send(f"**{ctx.author}**, No outcome of meeting has input in given time. Timeout!")
            return
          else:
            individualTask.append({"Outcome": msg.content})
            await ctx.send(f"**{ctx.author}**, Your outcome was {msg.content}!")
          ############################---Done taking message---####################################

          await ctx.send("Hours?")

          ###############---Taking message and waiting for timeout---#################
          def check(m: discord.Message):
              return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
          try:
            msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
          except asyncio.TimeoutError: 
            await ctx.send(f"**{ctx.author}**, No Hours has input in given time. Timeout!")
            return
          else:
            individualTask.append({"Hours": msg.content})
            await ctx.send(f"**{ctx.author}**, Total hour of this work is {msg.content}!")
          ############################---Done taking message---####################################

          await ctx.send("Minutes? (0-60)")

          ###############---Taking message and waiting for timeout---#################
          def check(m: discord.Message):
              return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
          try:
            msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
          except asyncio.TimeoutError: 
            await ctx.send(f"**{ctx.author}**, No Minutes has input in given time. Timeout!")
            return
          else:
              individualTask.append({"Minutes": msg.content})
              await ctx.send(f"**{ctx.author}**, Total minutes of this work is {msg.content}!")
          ############################---Done taking message---####################################


          await ctx.send("Status? If Done press 1, press 0 otherwise.")

          ###############---Taking message and waiting for timeout---#################
          def check(m: discord.Message):
              return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
          try:
            msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
          except asyncio.TimeoutError: 
            await ctx.send(f"**{ctx.author}**, No Status has input in given time. Timeout!")
            return
          else:
              if msg.content == '1': 
                await ctx.send("The work is Done!")
                individualTask.append({"Status": "Done"})
              else:
                await ctx.send("Issue?")

                ###############---Taking message and waiting for timeout---#################
                def check(m: discord.Message):
                    return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
                try:
                  msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
                except asyncio.TimeoutError: 
                  await ctx.send(f"**{ctx.author}**, No issues has input in given time. Timeout!")
                  return
                else:
                  await ctx.send(f"**{ctx.author}**, The issue behind this in progress work is : {msg.content}!")
                  individualTask.append({"Issue": msg.content})
                ############################---Done taking message---####################################

                await ctx.send("Parcentage of completion?")

                ###############---Taking message and waiting for timeout---#################
                def check(m: discord.Message):
                    return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
                try:
                  msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
                except asyncio.TimeoutError: 
                  await ctx.send(f"**{ctx.author}**, No parcentage has input in given time. Timeout!")
                  return
                else:
                    await ctx.send(f"**{ctx.author}**,  {msg.content}% of work has done!")
                    individualTask.append({"Percent": msg.content})
                ############################---Done taking message---####################################
          ############################---Done taking message---####################################
        else:
          await ctx.send("It is not a meeting")

          await ctx.send("Hours?")

          ###############---Taking message and waiting for timeout---#################
          def check(m: discord.Message):
              return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
          try:
            msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
          except asyncio.TimeoutError: 
            await ctx.send(f"**{ctx.author}**, No Hours has input in given time. Timeout!")
            return
          else:
            await ctx.send(f"**{ctx.author}**, Total hour of this work is {msg.content}!")
            individualTask.append({"Hours": msg.content})
          ############################---Done taking message---####################################

          await ctx.send("Minutes? (0-60)")

          ###############---Taking message and waiting for timeout---#################
          def check(m: discord.Message):
              return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
          try:
            msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
          except asyncio.TimeoutError: 
            await ctx.send(f"**{ctx.author}**, No Minutes has input in given time. Timeout!")
            return
          else:
              await ctx.send(f"**{ctx.author}**, Total minutes of this work is {msg.content}!")
              individualTask.append({"Minutes": msg.content})
          ############################---Done taking message---####################################


          await ctx.send("Status? If Done press 1, press 0 otherwise.")

          ###############---Taking message and waiting for timeout---#################
          def check(m: discord.Message):
              return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
          try:
            msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
          except asyncio.TimeoutError: 
            await ctx.send(f"**{ctx.author}**, No Status has input in given time. Timeout!")
            return
          else:
              if msg.content == '1': 
                await ctx.send("The work is Done!")
                individualTask.append({"Status":"Done"})
              else:
                await ctx.send("Issue?")

                ###############---Taking message and waiting for timeout---#################
                def check(m: discord.Message):
                    return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
                try:
                  msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
                except asyncio.TimeoutError: 
                  await ctx.send(f"**{ctx.author}**, No issues has input in given time. Timeout!")
                  return
                else:
                    await ctx.send(f"**{ctx.author}**, The issue behind this in progress work is : {msg.content}!")
                    individualTask.append({"Issue": msg.content})
                ############################---Done taking message---####################################

                await ctx.send("Parcentage of completion?")

                ###############---Taking message and waiting for timeout---#################
                def check(m: discord.Message):
                    return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 
                try:
                  msg = await self.bot.wait_for('message', check = check, timeout = 60.0)
                except asyncio.TimeoutError: 
                  await ctx.send(f"**{ctx.author}**, No parcentage has input in given time. Timeout!")
                  return
                else:
                    await ctx.send(f"**{ctx.author}**,  {msg.content}% of work has done!")
                    individualTask.append({"Percent": msg.content})
                ############################---Done taking message---####################################
          ############################---Done taking message---####################################
          

          
        await ctx.send(f"**{ctx.author}**, you responded with {msg.content} Program close!")
        taskDict.append(individualTask)
        

    
    
  