import discord
import asyncio
from datetime import date
from DayType import *
from Exercise import *
from discord.ext import commands

TOKEN = 'MTEyODc1NTM3Mzg0Nzg3MTU1MQ.Gjh3aA.NGHBGWYBuhAhH_0vzJbasMqwEIBzdiwEZ5Rsd0'

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)              # Bot listens for commands if ! is typed
client.remove_command('help')

# Creates Relevant DayType Objects
pushDay = DayType("Push")
pullDay = DayType("Pull")
legDay = DayType("Legs")

# Exercises Dictionary
push_exercises = {}
pull_exercises = {}
leg_exercises = {}


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
    user_exercise_name = ""
    user_exercise_weight = 0
    user_exercise_comment = ""

    await ctx.send("Add to \"Push\", \"Pull\", or \"Legs\"?")

    # Checks conditions for message output
    try:
        message = await client.wait_for("message", check=lambda msg: msg.author == ctx.author and
                                                                     msg.channel == ctx.channel, timeout=30.0)

    # Timeout condition
    except asyncio.TimeoutError:
        await ctx.send("User Timed Out")

    # Checks the messages if no errors
    else:

        # Push Case
        if message.content.lower() == "push":
            await ctx.send("Enter the name of an exercise to add to push:")

            # Adds push exercises
            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            # Timeout condition
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            # Takes user_input
            else:
                # Gets user_input for exercise data and creates an object to store in dictionary
                user_exercise_name = message.content

                # If exercise exists                                (IS CASE SENSITIVE, IMPROVE LATER)
                if user_exercise_name in push_exercises:
                    await ctx.send("Duplicate exercise, please enter a new exercise")
                    return

                else:
                    push_exercises[user_exercise_name] = Exercise(user_exercise_name)

                    # Creates an exercise object to store in the dictionary
                    await ctx.send("You've added " + push_exercises[user_exercise_name].get_name() + " to push day.")

        # Pull case
        elif message.content.lower() == "pull":
            await ctx.send("Enter the name of an exercise to add to pull:")

            # Adds pull exercises
            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            # Timeout condition
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            # Takes user_input
            else:
                # Gets user_input for exercise data and creates an object to store in dictionary
                user_exercise_name = message.content

                # If exercise exists                                (IS CASE SENSITIVE, IMPROVE LATER)
                if user_exercise_name in pull_exercises:
                    await ctx.send("Duplicate exercise, please enter a new exercise")
                    return

                else:
                    pull_exercises[user_exercise_name] = Exercise(user_exercise_name)

                    # Creates an exercise object to store in the dictionary
                    await ctx.send("You've added " + pull_exercises[user_exercise_name].get_name() + " to pull day.")

        # Legs case
        elif message.content.lower() == "legs":
            await ctx.send("Enter the name of an exercise to add to legs:")

            # Adds legs exercises
            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            # Timeout condition
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            # Takes user_input
            else:
                # Gets user_input for exercise data and creates an object to store in dictionary
                user_exercise_name = message.content

                # If exercise exists                                (IS CASE SENSITIVE, IMPROVE LATER)
                if user_exercise_name in leg_exercises:
                    await ctx.send("Duplicate exercise, please enter a new exercise")
                    return

                else:
                    leg_exercises[user_exercise_name] = Exercise(user_exercise_name)

                    # Creates an exercise object to store in the dictionary
                    await ctx.send("You've added " + leg_exercises[user_exercise_name].get_name() + " to leg day.")

        else:
            await ctx.send("Invalid Input")

client.run(TOKEN)
