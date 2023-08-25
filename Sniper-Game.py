import discord
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")


intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
@tree.command(name = "commandname", description = "My first application Command", guild=discord.Object(id=12417128931))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=859295541103034378))
    print("Ready!")
client.run(TOKEN)