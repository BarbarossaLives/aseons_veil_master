import discord
import random

TOKEN = "MTM3NzA2ODMyNjAzOTMyNjc0MQ.GYrwx-.uMozrfd-pzI9Yr7uhs02w14hWoR6mPTFElpFxQ"  

intents = discord.Intents.default()
intents.message_content = True 
client = discord.Client(intents=intents)

# Simple dice roller function
import re

def roll_dice(args):
    dice_pattern = re.compile(r"(\d+)d(\d+)")
    modifier = 0
    all_rolls = []
    total = 0

    for arg in args:
        if dice_match := dice_pattern.match(arg.lower()):
            num, die = map(int, dice_match.groups())
            rolls = [random.randint(1, die) for _ in range(num)]
            all_rolls.append(f"{num}d{die}: {rolls}")
            total += sum(rolls)
        elif arg.startswith("+") or arg.startswith("-"):
            try:
                modifier += int(arg)
            except ValueError:
                return f"Invalid modifier: {arg}"
        else:
            return f"Invalid input: {arg}"

    final_total = total + modifier
    return f"Rolls:\n" + "\n".join(all_rolls) + f"\nModifier: {modifier}\nTotal: {final_total}"


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!roll"):
        args = message.content.split()[1:]  # skip "!roll"
        if not args:
            await message.channel.send("Usage: !roll 2d6 1d4 +2")
            return

        result = roll_dice(args)
        await message.channel.send(result)


client.run(TOKEN)
