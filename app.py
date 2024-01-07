import discord
from discord.ext import commands
import serial

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable the Message Content intent

client = commands.Bot(command_prefix='/', intents=intents)

serialcomm = serial.Serial('COM3', 9600)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


#FIRST RELAY COMMAND SERIAL COMMUNICATION
@client.command(name='rog')#ON COMMAND
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention} ROG ON!")
    x = "rog"
    i = x.strip()
    serialcomm.write(i.encode())
@client.command(name='ror')#OFF COMMAND
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention} ROG OFF!")
    x = "ror"
    i = x.strip()
    serialcomm.write(i.encode())

#SECOND RELAY COMMAND
@client.command(name='rng')#ON COMMAND
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention} RNG ON!")
    # Serial communication
    x = "rng"
    i = x.strip()
    serialcomm.write(i.encode())
@client.command(name='rnr')#OFF COMMAND
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention} RNG OFF!")
    # Serial communication
    x = "rnr"
    i = x.strip()
    serialcomm.write(i.encode())
#THIRD RELAY COMMAND
@client.command(name='rsg')#ON COMMAND
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention} RSG ON!")
    # Serial communication
    x = "rsg"
    i = x.strip()
    serialcomm.write(i.encode())
@client.command(name='rsr')#OFF COMMAND
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention} RSG OFF!")
    # Serial communication
    x = "rsr"
    i = x.strip()
    serialcomm.write(i.encode())

#HELP COMMAND 
@client.command(name='chelp', description='Display information about available commands.')
async def help_command(ctx):
    """Command to display help about available commands."""
    embed = discord.Embed(title="Bot Commands", description="List of available commands:")

#Add information about the /rog command
    embed.add_field(name="/rog", value="relay 1 on (lamp)", inline=False)
    embed.add_field(name="/ror", value="relay 1 off (lamp)", inline=False)
    embed.add_field(name="/rng", value="relay 2 on", inline=False)
    embed.add_field(name="/rnr", value="relay 2 off", inline=False)
    embed.add_field(name="/rsg", value="relay 3 on", inline=False)
    embed.add_field(name="/rsr", value="relay 3 off", inline=False)

    await ctx.send(embed=embed)


client.run("DISCORD_TOKEN_HERE")
