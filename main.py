import discord
from datetime import date
from DayType import *
from Exercise import *
from discord.ext import commands

TOKEN = 'MTEyODc1NTM3Mzg0Nzg3MTU1MQ.GMzzUN.t5jHY0QH8jmzppkCt0VUw3Qs5DsWRp1qP3SS6E'

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)              # Bot listens for commands if ! is typed
client.remove_command('help')


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


@client.command()
async def legs(ctx):
    today = date.today()

    day = DayType("Legs")
    await ctx.send(day.get_day_type() + "\n" + day.get_date())


@client.command()
async def push(ctx):
    today = date.today()

    day = DayType("Push")
    await ctx.send(day.get_day_type() + "\n" + day.get_date())


@client.command()
async def pull(ctx):
    today = date.today()

    day = DayType("Pull")
    await ctx.send(day.get_day_type() + "\n" + day.get_date())



@client.command()
async def add(ctx):
    await ctx.send("Add to \"Push\", \"Pull\", or \"Legs\"?")

    user_input = ""

    # This will make sure that the response will only be registered if the following
    # conditions are met:
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
            msg.content.lower() in ["push", "pull", "legs"]

    msg = await client.wait_for("message", check=check)
    if msg.content.lower() == "push":
        await ctx.send("Enter an exercise to add to push:")


        user_input = await client.wait_for("message", check=None)
        ctx.send(user_input)

    elif msg.content.lower() == "pull":
        await ctx.send("Enter an exercise to add to pull:")

    elif msg.content.lower() == "legs":
        await ctx.send("Enter an exercise to add to legs:")

    else:
        await ctx.send("Please enter only \"Push\", \"Pull\", or \"Legs\".")


# @client.command()
#     async def remove(ctx):





client.run(TOKEN)