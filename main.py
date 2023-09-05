import discord
import asyncio
from datetime import date
from DayType import *
from Exercise import *
from discord.ext import commands

TOKEN = 'MTEyODc1NTM3Mzg0Nzg3MTU1MQ.Gnohtz._28nxfALhmriOD75pWRSpIuK6Ygj6yc1Dl8Iy4'

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


@client.command()
async def help(ctx):
    await ctx.send("Commands: !hello")



# Prints out the type of day and the current date
# TO DO - Print out the exercises too
@client.command()
async def push(ctx):
    counter = 1
    today = date.today()
    await ctx.send("-\n**" + dayTypeList[0].get_day_type() + "**\n**" + dayTypeList[0].get_date() + "**")

    for key in push_exercises:
        # formatting purposes (if empty comment)
        if push_exercises[key].comment != "":
            await ctx.send(str(counter) + ". " + key + " - " + str(push_exercises[key].weight) + " lbs - " +
                           push_exercises[key].comment)
        else:
            await ctx.send(str(counter) + ". " + key + " - " + str(push_exercises[key].weight) + " lbs " +
                           push_exercises[key].comment)
        counter += 1


# Prints out the type of day and the current date
# TO DO - Print out the exercises too
@client.command()
async def pull(ctx):
    counter = 1
    today = date.today()
    await ctx.send("-\n**" + dayTypeList[1].get_day_type() + "**\n**" + dayTypeList[1].get_date() + "**")

    # formatting purposes (if empty comment)
    for key in pull_exercises:
        if pull_exercises[key].comment != "":
            await ctx.send(str(counter) + ". " + key + " - " + str(pull_exercises[key].weight) + " lbs - " +
                           pull_exercises[key].comment)
        else:
            await ctx.send(str(counter) + ". " + key + " - " + str(pull_exercises[key].weight) + " lbs " +
                           pull_exercises[key].comment)
        counter += 1


# Prints out the type of day and the current date
# TO DO - Print out the exercises too
@client.command()
async def legs(ctx):
    counter = 1
    today = date.today()
    await ctx.send("-\n**" + dayTypeList[2].get_day_type() + "**\n**" + dayTypeList[2].get_date() + "**")

    # formatting purposes (if empty comment)
    for key in leg_exercises:
        if leg_exercises[key].comment != "":
            await ctx.send(str(counter) + ". " + key + " - " + str(leg_exercises[key].weight) + " lbs - " +
                           leg_exercises[key].comment)
        else:
            await ctx.send(str(counter) + ". " + key + " - " + str(leg_exercises[key].weight) + " lbs " +
                           leg_exercises[key].comment)
        counter += 1


# Adds exercises to current day
@client.command()
async def add(ctx):
    user_exercise_name = ""

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
                    # Creates an exercise object to store in the dictionary
                    push_exercises[user_exercise_name] = Exercise(user_exercise_name)

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


@client.command()
async def remove(ctx):
    user_exercise_name = ""
    await ctx.send("Remove from \"Push\", \"Pull\", or \"Legs\"?")

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
            await ctx.send("Enter the name of an exercise to remove:")

            # Removes push exercises
            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            # Timeout condition
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            else:
                # Gets key for exercise from user to remove from dictionary
                user_exercise_name = message.content

                # If exercise exists                                (IS CASE SENSITIVE, IMPROVE LATER)
                if user_exercise_name in push_exercises:
                    del push_exercises[user_exercise_name]
                    await ctx.send("Removed " + user_exercise_name + " from push day")
                    return

                else:
                    await ctx.send("Exercise does not exist, please enter an existing exercise")
                    return

        # Pull case
        elif message.content.lower() == "pull":
            await ctx.send("Enter the name of an exercise to remove:")

            # Removes pull exercises
            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            # Timeout condition
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            else:
                # Gets key for exercise from user to remove from dictionary
                user_exercise_name = message.content

                # If exercise exists                                (IS CASE SENSITIVE, IMPROVE LATER)
                if user_exercise_name in pull_exercises:
                    del pull_exercises[user_exercise_name]
                    await ctx.send("Removed " + user_exercise_name + " from pull day")
                    return

                else:
                    await ctx.send("Exercise does not exist, please enter an existing exercise")
                    return

        # Legs case
        elif message.content.lower() == "legs":
            await ctx.send("Enter the name of an exercise to remove:")

            # Removes pull exercises
            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            # Timeout condition
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            else:
                # Gets key for exercise from user to remove from dictionary
                user_exercise_name = message.content

                # If exercise exists                                (IS CASE SENSITIVE, IMPROVE LATER)
                if user_exercise_name in leg_exercises:
                    del leg_exercises[user_exercise_name]
                    await ctx.send("Removed " + user_exercise_name + " from leg day")
                    return

                else:
                    await ctx.send("Exercise does not exist, please enter an existing exercise")
                    return

        else:
            await ctx.send("Invalid Input")


@client.command()
async def update(ctx):
    user_exercise_name = ""
    user_choice = ""
    user_input = ""
    await ctx.send("Update from \"Push\", \"Pull\", or \"Legs\"?")

    # Checks conditions for message output
    try:
        message = await client.wait_for("message", check=lambda msg: msg.author == ctx.author and
                                                                     msg.channel == ctx.channel, timeout=30.0)

    # Timeout condition
    except asyncio.TimeoutError:
        await ctx.send("User Timed Out")

    # Checks the messages if no errors
    else:
        # Updates push exercises
        if message.content.lower() == "push":
            await ctx.send("Enter the name of an exercise to update:")

            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            # Timeout condition
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            else:
                # Gets key for exercise from user to update
                user_exercise_name = message.content

                if user_exercise_name in push_exercises:

                    await ctx.send("Update \"name\", \"weight\", or \"comment\"?")

                    try:
                        message = await client.wait_for("message",
                                                        check=lambda msg:
                                                        msg.author == ctx.author and
                                                        msg.channel == ctx.channel,
                                                        timeout=30.0)
                    # Timeout condition
                    except asyncio.TimeoutError:
                        await ctx.send("User Timed Out")

                    else:
                        user_choice = message.content

                        # Updates name
                        if user_choice.lower() == "name":

                            # Finds exercise to update
                            if user_exercise_name in push_exercises:
                                await ctx.send("Enter a new name for " + user_exercise_name + ": ")

                                try:
                                    message = await client.wait_for("message",
                                                                    check=lambda msg:
                                                                    msg.author == ctx.author and
                                                                    msg.channel == ctx.channel,
                                                                    timeout=30.0)
                                # Timeout condition
                                except asyncio.TimeoutError:
                                    await ctx.send("User Timed Out")

                                else:
                                    user_input = message.content

                                    # updates dictionary key
                                    push_exercises[user_input] = push_exercises[user_exercise_name]
                                    del push_exercises[user_exercise_name]

                                    # updates name
                                    push_exercises[user_input].change_name(user_input)
                                    await ctx.send("Exercise name updated successfully")

                        # Updates weight
                        elif user_choice.lower() == "weight":
                            # Finds exercise to update
                            if user_exercise_name in push_exercises:
                                await ctx.send("Enter a new weight for " + user_exercise_name + ": ")

                                try:
                                    message = await client.wait_for("message",
                                                                    check=lambda msg:
                                                                    msg.author == ctx.author and
                                                                    msg.channel == ctx.channel,
                                                                    timeout=30.0)
                                # Timeout condition
                                except asyncio.TimeoutError:
                                    await ctx.send("User Timed Out")

                                else:
                                    user_input = message.content

                                    # updates weight
                                    push_exercises[user_exercise_name].change_weight(int(user_input))
                                    await ctx.send("Exercise weight updated successfully")

                        # Updates comment
                        elif user_choice.lower() == "comment":
                            # Finds exercise to update
                            if user_exercise_name in push_exercises:
                                await ctx.send("Enter a new comment for " + user_exercise_name + ": ")

                                try:
                                    message = await client.wait_for("message",
                                                                    check=lambda msg:
                                                                    msg.author == ctx.author and
                                                                    msg.channel == ctx.channel,
                                                                    timeout=30.0)
                                # Timeout condition
                                except asyncio.TimeoutError:
                                    await ctx.send("User Timed Out")

                                else:
                                    user_input = message.content

                                    # updates weight
                                    push_exercises[user_exercise_name].change_comment(user_input)
                                    await ctx.send("Exercise comment updated successfully")

                        else:
                            await ctx.send("Invalid input")
                            return
                # if user input exercise does not exist
                else:
                    await ctx.send("Exercise does not exist")
                    return

        # Updates pull exercises
        elif message.content.lower() == "pull":
            await ctx.send("Enter the name of an exercise to update:")

            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            # Timeout condition
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            else:
                # Gets key for exercise from user to update
                user_exercise_name = message.content

                if user_exercise_name in pull_exercises:

                    await ctx.send("Update \"name\", \"weight\", or \"comment\"?")

                    try:
                        message = await client.wait_for("message",
                                                        check=lambda msg:
                                                        msg.author == ctx.author and
                                                        msg.channel == ctx.channel,
                                                        timeout=30.0)
                    # Timeout condition
                    except asyncio.TimeoutError:
                        await ctx.send("User Timed Out")

                    else:
                        user_choice = message.content

                        # Updates name
                        if user_choice.lower() == "name":

                            # Finds exercise to update
                            if user_exercise_name in pull_exercises:
                                await ctx.send("Enter a new name for " + user_exercise_name + ": ")

                                try:
                                    message = await client.wait_for("message",
                                                                    check=lambda msg:
                                                                    msg.author == ctx.author and
                                                                    msg.channel == ctx.channel,
                                                                    timeout=30.0)
                                # Timeout condition
                                except asyncio.TimeoutError:
                                    await ctx.send("User Timed Out")

                                else:
                                    user_input = message.content

                                    # updates dictionary key
                                    pull_exercises[user_input] = pull_exercises[user_exercise_name]
                                    del pull_exercises[user_exercise_name]

                                    # updates name
                                    pull_exercises[user_input].change_name(user_input)
                                    await ctx.send("Exercise name updated successfully")

                        # Updates weight
                        elif user_choice.lower() == "weight":
                            # Finds exercise to update
                            if user_exercise_name in pull_exercises:
                                await ctx.send("Enter a new weight for " + user_exercise_name + ": ")

                                try:
                                    message = await client.wait_for("message",
                                                                    check=lambda msg:
                                                                    msg.author == ctx.author and
                                                                    msg.channel == ctx.channel,
                                                                    timeout=30.0)
                                # Timeout condition
                                except asyncio.TimeoutError:
                                    await ctx.send("User Timed Out")

                                else:
                                    user_input = message.content

                                    # updates weight
                                    pull_exercises[user_exercise_name].change_weight(int(user_input))
                                    await ctx.send("Exercise weight updated successfully")

                        # Updates comment
                        elif user_choice.lower() == "comment":
                            # Finds exercise to update
                            if user_exercise_name in pull_exercises:
                                await ctx.send("Enter a new comment for " + user_exercise_name + ": ")

                                try:
                                    message = await client.wait_for("message",
                                                                    check=lambda msg:
                                                                    msg.author == ctx.author and
                                                                    msg.channel == ctx.channel,
                                                                    timeout=30.0)
                                # Timeout condition
                                except asyncio.TimeoutError:
                                    await ctx.send("User Timed Out")

                                else:
                                    user_input = message.content

                                    # updates weight
                                    pull_exercises[user_exercise_name].change_comment(user_input)
                                    await ctx.send("Exercise comment updated successfully")
                        else:
                            await ctx.send("Invalid input")
                            return
                # if user input exercise does not exist
                else:
                    await ctx.send("Exercise does not exist")
                    return

        # Updates leg exercises
        elif message.content.lower() == "legs":
            await ctx.send("Enter the name of an exercise to update:")

            try:
                message = await client.wait_for("message",
                                                check=lambda msg:
                                                msg.author == ctx.author and
                                                msg.channel == ctx.channel,
                                                timeout=30.0)
            # Timeout condition
            except asyncio.TimeoutError:
                await ctx.send("User Timed Out")

            else:
                # Gets key for exercise from user to update
                user_exercise_name = message.content

                if user_exercise_name in leg_exercises:

                    await ctx.send("Update \"name\", \"weight\", or \"comment\"?")

                    try:
                        message = await client.wait_for("message",
                                                        check=lambda msg:
                                                        msg.author == ctx.author and
                                                        msg.channel == ctx.channel,
                                                        timeout=30.0)
                    # Timeout condition
                    except asyncio.TimeoutError:
                        await ctx.send("User Timed Out")

                    else:
                        user_choice = message.content

                        # Updates name
                        if user_choice.lower() == "name":

                            # Finds exercise to update
                            if user_exercise_name in leg_exercises:
                                await ctx.send("Enter a new name for " + user_exercise_name + ": ")

                                try:
                                    message = await client.wait_for("message",
                                                                    check=lambda msg:
                                                                    msg.author == ctx.author and
                                                                    msg.channel == ctx.channel,
                                                                    timeout=30.0)
                                # Timeout condition
                                except asyncio.TimeoutError:
                                    await ctx.send("User Timed Out")

                                else:
                                    user_input = message.content

                                    # updates dictionary key
                                    leg_exercises[user_input] = leg_exercises[user_exercise_name]
                                    del leg_exercises[user_exercise_name]

                                    # updates name
                                    leg_exercises[user_input].change_name(user_input)
                                    await ctx.send("Exercise name updated successfully")

                        # Updates weight
                        elif user_choice.lower() == "weight":
                            # Finds exercise to update
                            if user_exercise_name in leg_exercises:
                                await ctx.send("Enter a new weight for " + user_exercise_name + ": ")

                                try:
                                    message = await client.wait_for("message",
                                                                    check=lambda msg:
                                                                    msg.author == ctx.author and
                                                                    msg.channel == ctx.channel,
                                                                    timeout=30.0)
                                # Timeout condition
                                except asyncio.TimeoutError:
                                    await ctx.send("User Timed Out")

                                else:
                                    user_input = message.content

                                    # updates weight
                                    leg_exercises[user_exercise_name].change_weight(int(user_input))

                                    await ctx.send("Exercise weight updated successfully")

                        # Updates comment
                        elif user_choice.lower() == "comment":
                            # Finds exercise to update
                            if user_exercise_name in leg_exercises:
                                await ctx.send("Enter a new comment for " + user_exercise_name + ": ")

                                try:
                                    message = await client.wait_for("message",
                                                                    check=lambda msg:
                                                                    msg.author == ctx.author and
                                                                    msg.channel == ctx.channel,
                                                                    timeout=30.0)
                                # Timeout condition
                                except asyncio.TimeoutError:
                                    await ctx.send("User Timed Out")

                                else:
                                    user_input = message.content

                                    # updates weight
                                    leg_exercises[user_exercise_name].change_comment(user_input)
                                    await ctx.send("Exercise comment updated successfully")
                        else:
                            await ctx.send("Invalid input")
                            return
                # if user input exercise does not exist
                else:
                    await ctx.send("Exercise does not exist")
                    return

        else:
            await ctx.send("Invalid input")
            return




                    # elif user_choice.lower() == "comment":




client.run(TOKEN)
