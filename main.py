import discord
import asyncio
from DayType import *
from Exercise import *
from models import *
from discord.ext import commands


# SQLAlchemy
userID = None
userName = None


# Base.metadata.create_all(bind=engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()



# class Users(Base):
#     __tablename__ = "users"
#     userid = Column("userid", Integer, primary_key=True)
#     daytypes = relationship("daytypes", backref='users')
#
#     def __init__(self, userid):
#         self.userid = userid
#
#     def __repr__(self):
#         return f"(UserID: {self.userid})"


# class DayTypes(Base):
#     __tablename__ = "dayTypes"
#     daytypeid = Column("daytypeid", Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('userid'))
#     daytype = Column("type", String)
#     date = Column("date", String)
#     exerciseid = relationship("exerciseid", backref='daytypes')
#
#
#     def __init__(self, daytypeid, daytype, date, exerciseid):
#         self.daytypeid = daytypeid
#         self.daytype = daytype
#         self.date = date
#         self.exerciseid = exerciseid
#
#     def __repr__(self):
#         return f"(DaytypeID: {self.daytypeid} DayType: {self.daytype} Date: {self.date} ExerciseID: {self.exerciseid})"


# class Exercises(Base):
#     __tablename__ = "exercises"
#     exerciseid = Column(Integer, ForeignKey('exerciseid'))
#     name = Column("name", String)
#     weight = Column("weight", Integer)
#     comment = Column("comment", String)
#
#     def __init__(self, exerciseid, name, weight, comment):
#         self.exerciseid = exerciseid
#         self.name = name
#         self.weight = weight
#         self.comment = comment
#
#     def __repr__(self):
#         return f"(ExerciseID: {self.exerciseid} Name: {self.name} Weight: {self.weight} Comment: {self.comment})"



# person = Person(12312, "Mike", "Smith", "m", 35)
# session.add(person)                             # this creates the person in the database
# session.commit()                                # same concept as git

# results = session.query(Person).all()                                   # query gets the data from the database
# results = session.query(Person).filter(Person.lastname == "Blue")       # we can filter our queries
# session.query(Person).filter(Person.lastname.in_(["Anna", "Mike"]))     # checks if in the query
# print(results)





# BOT CODE STARTS HERE
TOKEN = 'MTEyODc1NTM3Mzg0Nzg3MTU1MQ.Gin1bU.GIuYhXsEzftGrliZSvu8KBJNUROiF7LYp-YplU'

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!', intents=intents)              # Bot listens for commands if ! is typed
client.remove_command('help')

# Creates dayType exercises
push_dayType = {}
pull_dayType = {}
legs_dayType = {}


@client.event
async def on_ready():                                   # Bot is ready
    print("Bot is ready.")
    print("-----------------")


# Updates userID to sender upon message
@client.event
async def on_message(message):
    global userID
    global userName

    # ignores bot texts
    if message.author == client.user:
        await client.process_commands(message)

    else:
        userID = message.author.id
        userName = message.author

        # if userID is not in the database, register their userID to database

        user = Users(userID)
        session.add(user)
        session.commit()
        await client.process_commands(message)


# Displays all commands
@client.command()
async def help(ctx):
    await ctx.send("Commands: !hello")
    print(f"UserID: {userID}")


# Adds a new push dayType
@client.command()
async def newpush(ctx):             # ADD IF DAY EXISTS ALREADY
    if current_date() not in push_dayType:
        push_dayType[current_date()] = DayType("push")
        await ctx.send("New push day added to " + current_date())
    else:
        await ctx.send("Push day already exists for " + current_date())


# Adds a new pull dayType
@client.command()
async def newpull(ctx):
    if current_date() not in pull_dayType:
        pull_dayType[current_date()] = DayType("pull")
        await ctx.send("New pull day added to " + current_date())
    else:
        await ctx.send("Pull day already exists for " + current_date())


# Adds a new leg dayType
@client.command()
async def newlegs(ctx):
    if current_date() not in legs_dayType:
        legs_dayType[current_date()] = DayType("legs")
        await ctx.send("New leg day added to " + current_date())
    else:
        await ctx.send("Leg day already exists for " + current_date())


# Prints out push day's information
@client.command()
async def push(ctx):
    if current_date() not in push_dayType:
        await ctx.send("Push day for " + current_date() + " does not exist")
        return

    else:
        output = ">>> **Push Day" + "**\n**" + push_dayType[current_date()].get_date() + "**"
        for key in push_dayType[current_date()].get_push_exercises():
            # formatting purposes (if empty comment)
            if push_dayType[current_date()].get_push_exercises()[key].comment != "":
                output += "\n- " + key + " - " + str(push_dayType[current_date()].get_push_exercises()[key].weight) + " lbs - " + push_dayType[current_date()].get_push_exercises()[key].comment
            else:
                output += "\n- " + key + " - " + str(push_dayType[current_date()].get_push_exercises()[key].weight) + " lbs " + push_dayType[current_date()].get_push_exercises()[key].comment

        await ctx.send(output)


# Prints out pull day's information
@client.command()
async def pull(ctx):
    if current_date() not in pull_dayType:
        await ctx.send("Pull day for " + current_date() + " does not exist.")
        return

    else:
        output = ">>> **Pull Day" + "**\n**" + pull_dayType[current_date()].get_date() + "**"
        for key in pull_dayType[current_date()].get_pull_exercises():
            # formatting purposes (if empty comment)
            if pull_dayType[current_date()].get_pull_exercises()[key].comment != "":
                output += "\n- " + key + " - " + str(pull_dayType[current_date()].get_pull_exercises()[key].weight) + " lbs - " + pull_dayType[current_date()].get_pull_exercises()[key].comment
            else:
                output += "\n- " + key + " - " + str(pull_dayType[current_date()].get_pull_exercises()[key].weight) + " lbs " + pull_dayType[current_date()].get_pull_exercises()[key].comment

        await ctx.send(output)


# Prints out leg day's information
@client.command()
async def legs(ctx):
    if current_date() not in legs_dayType:
        await ctx.send("Leg day for " + current_date() + " does not exist.")
        return

    else:
        output = ">>> **Leg Day" + "**\n**" + legs_dayType[current_date()].get_date() + "**"
        for key in legs_dayType[current_date()].get_legs_exercises():
            # formatting purposes (if empty comment)
            if legs_dayType[current_date()].get_legs_exercises()[key].comment != "":
                output += "\n- " + key + " - " + str(legs_dayType[current_date()].get_legs_exercises()[key].weight) + " lbs - " + legs_dayType[current_date()].get_legs_exercises()[key].comment
            else:
                output += "\n- " + key + " - " + str(legs_dayType[current_date()].get_legs_exercises()[key].weight) + " lbs " + legs_dayType[current_date()].get_legs_exercises()[key].comment

        await ctx.send(output)


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
            # if the day does not exist
            if current_date() not in push_dayType:
                await ctx.send("Push day for " + current_date() + " does not exist.")
                return

            else:
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
                    if user_exercise_name in push_dayType[current_date()].get_push_exercises():
                        await ctx.send("Duplicate exercise, please enter a new exercise")
                        return

                    else:
                        # Creates an exercise object to store in the dictionary
                        push_dayType[current_date()].get_push_exercises()[user_exercise_name] = Exercise(user_exercise_name)

                        await ctx.send("You've added " + user_exercise_name + " to push day.")

        # Pull case
        elif message.content.lower() == "pull":
            # if the day does not exist
            if current_date() not in pull_dayType:
                await ctx.send("Pull day for " + current_date() + " does not exist.")
                return

            else:
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
                    if user_exercise_name in pull_dayType[current_date()].get_pull_exercises():
                        await ctx.send("Duplicate exercise, please enter a new exercise")
                        return

                    else:
                        # Creates an exercise object to store in the dictionary
                        pull_dayType[current_date()].get_pull_exercises()[user_exercise_name] = Exercise(
                            user_exercise_name)

                        await ctx.send("You've added " + user_exercise_name + " to pull day.")

        # Legs case
        elif message.content.lower() == "legs":
            # if the day does not exist
            if current_date() not in legs_dayType:
                await ctx.send("Leg day for " + current_date() + " does not exist.")
                return

            else:
                await ctx.send("Enter the name of an exercise to add to push:")

                # Adds leg exercises
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
                    if user_exercise_name in legs_dayType[current_date()].get_legs_exercises():
                        await ctx.send("Duplicate exercise, please enter a new exercise")
                        return

                    else:
                        # Creates an exercise object to store in the dictionary
                        legs_dayType[current_date()].get_legs_exercises()[user_exercise_name] = Exercise(
                            user_exercise_name)

                        await ctx.send("You've added " + user_exercise_name + " to leg day.")
        else:
            await ctx.send("Invalid Input")


# Removes an exercise
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
            if current_date() not in push_dayType:
                await ctx.send("Push day for " + current_date() + " does not exist.")
                return

            else:
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
                    if user_exercise_name in push_dayType[current_date()].get_push_exercises():
                        del push_dayType[current_date()].get_push_exercises()[user_exercise_name]
                        await ctx.send("Removed " + user_exercise_name + " from push day")
                        return

                    else:
                        await ctx.send("Exercise does not exist, please enter an existing exercise")
                        return

        # Pull case
        elif message.content.lower() == "pull":
            if current_date() not in pull_dayType:
                await ctx.send("Pull day for " + current_date() + " does not exist.")
                return

            else:
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
                    if user_exercise_name in pull_dayType[current_date()].get_pull_exercises():
                        del pull_dayType[current_date()].get_pull_exercises()[user_exercise_name]
                        await ctx.send("Removed " + user_exercise_name + " from pull day")
                        return

                    else:
                        await ctx.send("Exercise does not exist, please enter an existing exercise")
                        return

        # Legs case
        elif message.content.lower() == "legs":
            if current_date() not in legs_dayType:
                await ctx.send("Leg day for " + current_date() + " does not exist.")
                return

            else:
                await ctx.send("Enter the name of an exercise to remove:")

                # Removes leg exercises
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
                    if user_exercise_name in legs_dayType[current_date()].get_legs_exercises():
                        del legs_dayType[current_date()].get_legs_exercises()[user_exercise_name]
                        await ctx.send("Removed " + user_exercise_name + " from leg day")
                        return

                    else:
                        await ctx.send("Exercise does not exist, please enter an existing exercise")
                        return

        else:
            await ctx.send("Invalid Input")


# Updates name, comment, or weight of exercise
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
            if current_date() not in push_dayType:
                await ctx.send("Push day for " + current_date() + " does not exist.")
                return

            else:
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

                    if user_exercise_name in push_dayType[current_date()].get_push_exercises():

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
                                if user_exercise_name in push_dayType[current_date()].get_push_exercises():
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
                                        push_dayType[current_date()].get_push_exercises()[user_input] = (
                                            push_dayType[current_date()].get_push_exercises())[user_exercise_name]
                                        del push_dayType[current_date()].get_push_exercises()[user_exercise_name]

                                        # updates name
                                        (push_dayType[current_date()].get_push_exercises()[user_input].
                                         change_name(user_input))
                                        await ctx.send("Exercise name updated successfully")

                            # Updates weight
                            elif user_choice.lower() == "weight":
                                # Finds exercise to update
                                if user_exercise_name in push_dayType[current_date()].get_push_exercises():
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
                                        (push_dayType[current_date()].get_push_exercises()[user_exercise_name].
                                         change_weight(int(user_input)))
                                        await ctx.send("Exercise weight updated successfully")

                            # Updates comment
                            elif user_choice.lower() == "comment":
                                # Finds exercise to update
                                if user_exercise_name in push_dayType[current_date()].get_push_exercises():
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
                                        (push_dayType[current_date()].get_push_exercises()[user_exercise_name].
                                         change_comment(user_input))
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
            if current_date() not in pull_dayType:
                await ctx.send("Pull day for " + current_date() + " does not exist.")
                return

            else:
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

                    if user_exercise_name in pull_dayType[current_date()].get_pull_exercises():

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
                                if user_exercise_name in pull_dayType[current_date()].get_pull_exercises():
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
                                        pull_dayType[current_date()].get_pull_exercises()[user_input] = (
                                            pull_dayType[current_date()].get_pull_exercises())[user_exercise_name]
                                        del pull_dayType[current_date()].get_pull_exercises()[user_exercise_name]

                                        # updates name
                                        (pull_dayType[current_date()].get_pull_exercises()[user_input].
                                         change_name(user_input))
                                        await ctx.send("Exercise name updated successfully")

                            # Updates weight
                            elif user_choice.lower() == "weight":
                                # Finds exercise to update
                                if user_exercise_name in pull_dayType[current_date()].get_pull_exercises():
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
                                        (pull_dayType[current_date()].get_pull_exercises()[user_exercise_name].
                                         change_weight(int(user_input)))
                                        await ctx.send("Exercise weight updated successfully")

                            # Updates comment
                            elif user_choice.lower() == "comment":
                                # Finds exercise to update
                                if user_exercise_name in pull_dayType[current_date()].get_pull_exercises():
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
                                        (pull_dayType[current_date()].get_pull_exercises()[user_exercise_name].
                                         change_comment(user_input))
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
            if current_date() not in legs_dayType:
                await ctx.send("Leg day for " + current_date() + " does not exist.")
                return

            else:
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

                    if user_exercise_name in legs_dayType[current_date()].get_legs_exercises():

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
                                if user_exercise_name in legs_dayType[current_date()].get_legs_exercises():
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
                                        legs_dayType[current_date()].get_legs_exercises()[user_input] = (
                                            legs_dayType[current_date()].get_legs_exercises())[user_exercise_name]
                                        del legs_dayType[current_date()].get_legs_exercises()[user_exercise_name]

                                        # updates name
                                        (legs_dayType[current_date()].get_legs_exercises()[user_input].
                                         change_name(user_input))
                                        await ctx.send("Exercise name updated successfully")

                            # Updates weight
                            elif user_choice.lower() == "weight":
                                # Finds exercise to update
                                if user_exercise_name in legs_dayType[current_date()].get_legs_exercises():
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
                                        (legs_dayType[current_date()].get_legs_exercises()[user_exercise_name].
                                         change_weight(int(user_input)))
                                        await ctx.send("Exercise weight updated successfully")

                            # Updates comment
                            elif user_choice.lower() == "comment":
                                # Finds exercise to update
                                if user_exercise_name in legs_dayType[current_date()].get_legs_exercises():
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
                                        (legs_dayType[current_date()].get_legs_exercises()[user_exercise_name].
                                         change_comment(user_input))
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


# Gets current date (Helper Function)
def current_date():
    str_date = datetime.now().strftime("%m-%d-%Y")
    return str_date



client.run(TOKEN)
