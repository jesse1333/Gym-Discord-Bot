import discord
import asyncio
from datetime import date
from DayType import *
from Exercise import *
from discord.ext import commands

TOKEN = 'MTEyODc1NTM3Mzg0Nzg3MTU1MQ.GmIiPn.x1xGWz4nqvLUVJgLd4TW3m5tibeue2yomAlYRc'

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)              # Bot listens for commands if ! is typed
client.remove_command('help')

# Creates Relevant DayType Objects
pushDay = DayType("Push")
pullDay = DayType("Pull")
legDay = DayType("Legs")

# Exercises Dictionary
exercises = {}

# Contains dayType objects
dayTypeList = [pushDay, pullDay, legDay]

@client.event
async def on_ready():                                   # Bot is ready
    print("Bot is ready.")
    print("-----------------")


@client.command()                                       # ASD;FLJASD;LFJALS;DFJ NEED TO ADD HELP COMMANDS!!!!
async def help(ctx):
    await ctx.send("Commands: !hello")


@client.command()
async def hello(ctx):                                   # ctx just takes the input from discord
    await ctx.send("Hello, I am a discord bot!")        # when someone types !hello, it will print this out


# Prints out the type of day and the current date
# TO DO - Print out the exercises too
@client.command()
async def push(ctx):
    today = date.today()
    await ctx.send(dayTypeList[0].get_day_type() + "\n" + dayTypeList[0].get_date())


# Prints out the type of day and the current date
# TO DO - Print out the exercises too
@client.command()
async def pull(ctx):
    today = date.today()
    await ctx.send(dayTypeList[1].get_day_type() + "\n" + dayTypeList[1].get_date())


# Prints out the type of day and the current date
# TO DO - Print out the exercises too
@client.command()
async def legs(ctx):
    today = date.today()
    await ctx.send(dayTypeList[2].get_day_type() + "\n" + dayTypeList[2].get_date())


# Adds exercises to current day
@client.command()
async def add(ctx):
    await ctx.send("Add to \"Push\", \"Pull\", or \"Legs\"?")

    user_exercise_name = ""
    user_exercise_weight = 0
    user_exercise_comment = ""

    # Checks conditions for message output
    try:
        message = await client.wait_for("message", check=lambda msg: msg.author == ctx.author and
                                                                     msg.channel == ctx.channel, timeout=30.0)

    # Timeout condition
    except asyncio.TimeoutError:
        await ctx.send("User Timed Out")

    # Checks the messages if no errors
    else:
        if message.content.lower() == "push":
            await ctx.send("Enter an exercise to add to push:")

            # Adds push exercises
            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            # Takes user_input
            else:
                # Creates exercise object with name
                user_exercise_name = message.content
                exercises[user_exercise_name] = Exercise(user_exercise_name)

                await ctx.send("You've added " + exercises[user_exercise_name].get_name() + " to push day.")













        elif message.content.lower() == "pull":
            await ctx.send("Enter an exercise to add to pull:")

        elif message.content.lower() == "legs":
            await ctx.send("Enter an exercise to add to legs:")

        else:
            await ctx.send("Invalid Input.")






    # # This will make sure that the response will only be registered if the following
    # # conditions are met:
    # def check(msg):
    #     return msg.author == ctx.author and msg.channel == ctx.channel and \
    #         msg.content.lower() in ["push", "pull", "legs"]
    #
    # msg = await client.wait_for("message", check=check)
    # if msg.content.lower() == "push":
    #     await ctx.send("Enter an exercise to add to push:")
    #
    #
    #     user_input = await client.wait_for("message", check=None)
    #     ctx.send(user_input)
    #
    # elif msg.content.lower() == "pull":
    #     await ctx.send("Enter an exercise to add to pull:")
    #
    # elif msg.content.lower() == "legs":
    #     await ctx.send("Enter an exercise to add to legs:")
    #
    # else:
    #     await ctx.send("Please enter only \"Push\", \"Pull\", or \"Legs\".")


# @client.command()
#     async def remove(ctx):





client.run(TOKEN)