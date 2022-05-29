import os, discord, asyncio
from discord.ext import commands
from keep_alive import keep_alive

keep_alive()

intents = discord.Intents.default()
intents.members = True


description = "Hello hello!"

bot = commands.Bot(
    command_prefix="?",  # prefix to use the command (etc ?chance)
    description=description,
    intents=intents,
    case_insensitive=True,
)


dictOfScores = {
    "A*": 56,
    "AS": 56,
    "A": 48,
    "B": 40,
    "C": 32,
    "D": 24,
    "E": 16,
    "F": 8,
    "f": 8,
    "U": 0,
}

SecretBotToken = os.environ[".env"]  # Discord bot token stored in repl.it secrets


@bot.event
async def on_ready():  # checks bot is running
    print("test")
    print(bot.user.name)


def calcgcseavg(resultMapping):
    average = 368  # assumes average 4 AS 3 A
    resultMappingReturned = resultMapping
    percentageDifference = (
        (float(average) - resultMappingReturned) / resultMappingReturned
    ) * 100
    HighlowBoolean = "lower"
    if resultMappingReturned > 368:
        HighlowBoolean = "higher"

    return f"Your GCSE results are {round(percentageDifference, 2) * -1 }% {HighlowBoolean} then the average offer."


def CalculateALevelAverage(resultMapping2):
    average = 152  # Using A* A A average
    resultMappingReturned = resultMapping2
    percentageDifference = (
        (float(average) - resultMappingReturned) / resultMappingReturned
    ) * 100
    HighlowBoolean = "lower"
    if resultMappingReturned > 152:
        HighlowBoolean = "higher"

    return f"Your A-level results are {round(percentageDifference, 2) * -1 }% {HighlowBoolean} then the average offer."


def matavg(score):
    if type(score) == int or type(score) == float:
        if score < 47:
            return 6.43
        elif score > 47 and score < 60:
            return 39.3
        elif score > 61 and score < 88:
            return 76.6
        elif score > 88:
            return 100
        return 0
    else:
        return 0


@bot.command(name="myOxbridgeChances")
async def myOxbridgeChances(ctx, gcses):
    await ctx.send(
        "Please make sure you use the correct format (eg AS,A,A) (no spaces)"
    )
    await ctx.send("Due to a discord quirk, please use AS instead of A*")
    gcses = gcses.upper()
    gcsesList = gcses.split(",")
    for i in range(0, len(gcses)):
        tempCheck = gcsesList[i]
        tempCheck = str(tempCheck)
        if tempCheck == "A*":
            tempCheck == str("AS")
            print(tempCheck)
        if tempCheck.isalpha() == False:
            await ctx.send(
                "Invalid input - maybe you put a number? - please convert 9-1 system to grades, 8/9 both considered AS"
            )
            break
        else:
            for i in range(len(gcsesList)):
                resultMapping = sum(
                    map(lambda x: dictOfScores.get(x, 0), gcsesList)
                )  # maps user input in gcsesList into a dictionary and returns a numerical value (total sum of all key:value pairs given by user)
            print(f"resultMapping: {resultMapping}")

            await ctx.send(calcgcseavg(resultMapping))  # sends user result

            def check_response(m):
                return m.channel == ctx.channel and m.author == ctx.author

            try:
                await ctx.send(
                    "Input your A-Level scores: (remember to seperate them out - etc A,A,B) - type N/A if none"
                )
                msg = await bot.wait_for(
                    "message", check=check_response, timeout=15
                )  # Timeout feature - waits 15 seconds
                await ctx.send(f"You have: {msg.content}")  # checks user result
                msg.content = msg.content.upper()
                aLevelsList = msg.content.split(",")
                for i in range(len(aLevelsList)):
                    if i == "A*":
                        i == "AS"
                    resultMapping2 = sum(
                        map(lambda x: dictOfScores.get(x, 0), aLevelsList)
                    )

                await ctx.send(CalculateALevelAverage(resultMapping2))

                try:
                    await ctx.send("Input MAT Score: ")
                    msg = await bot.wait_for(
                        "message", check=check_response, timeout=15
                    )  # same as line 93
                    await ctx.send(f"You said: {msg.content}.")
                    a = msg.content.isalpha()
                    if msg.content == "N/A" or a == "N/a" or a == "n/a" or a == "n/A":
                        MATScore = 0
                    if a == False:
                        MATScore = matavg(float(msg.content))
                    else:
                        await ctx.send(
                            f"Something is wrong. Please try again. (did you put letters in?)"
                        )

                    averageCambridgeScore = 1295.24
                    UserAlvlScore = resultMapping2
                    UserGCSEScore = resultMapping

                    print(f"UserAL - {UserAlvlScore}")
                    print(f"UserGCSE - {UserGCSEScore}")
                    print(f"UserMAT - {MATScore}")
                    userFinalAverage = (float(UserGCSEScore) * 1)(
                        float(UserAlvlScore) * 6
                    )(MATScore * 3) / 10
                    print(f"userfinal{userFinalAverage}")

                    percentageDifference = (
                        (float(averageCambridgeScore) - float(userFinalAverage))
                        / userFinalAverage
                    ) * 100
                    print(percentageDifference)

                    if percentageDifference < 0:
                        percentageDifference = percentageDifference * -1

                    await ctx.send(
                        f"You have a {round(percentageDifference, 2)}% chance of getting into an Oxbridge university"
                    )

                    break

                except asyncio.TimeoutError:
                    pass
            except asyncio.TimeoutError:  # wait_for raises an exception when timeout is reached
                pass


token = SecretBotToken
bot.run(token, bot=True, reconnect=True)
