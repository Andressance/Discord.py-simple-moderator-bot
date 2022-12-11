import discord # Main discord library
from discord.ext import commands # Commands extension
from discord import app_commands # Slash commands
import asyncio # Asyncio library for async functions
import random 
from discord.ext.commands import Bot # Bot extension
from discord.ui import View, button # Buttons
import matplotlib.pyplot as plt # Matplotlib for graphs
from datetime import timedelta # Datetime for time objects
from itertools import cycle # Cycle for bot status


# We create de bot with the prefix "!" and all the intents
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class abot(discord.Client):
    def __init__(self): # Init function
        super().__init__(intents=discord.Intents.default()) 
        self.synced = False 
        self.added = False 
       

    async def on_ready(self): # When the bot is ready do this
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
        self.synced = True
        print("Bot is online") 
    status = cycle([""]) # Introduce the status you want, The bot will appear playing the status

bot = abot() # We create the bot with the class abot
tree = app_commands.CommandTree(bot) 

@tree.command(name= "ping", description= "Ping a alguien", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def ping(interaction: discord.Integration): # We create the function ping
    await interaction.response.send_message(f"Pong") # The bot will send a message with the text pong

@tree.command(name="ban", description="Ban someone", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def ban(interaction: discord.Integration, member: discord.User): # We create the function ban
    if interaction.user.guild_permissions.administrator: # If the user has the administrator permission
        await interaction.guild.ban(member) # The bot bans the member
        await interaction.response.send_message(embed=discord.Embed(title=f"{member} has been baned", color=0x00ff00)) # The bot sends an embed with the member that has been baned
    else:

        # If the user doesn't have the administrator permission the bot will send an embed saying that the user doesn't have the permission
        await interaction.response.send_message(embed=discord.Embed(title="You don't have permissons to perform this action", description="This action requires the administrator permission", color=0xff771273493227634689))

@tree.command(name="unban", description="Unban someone", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def unban(interaction : discord.Integration, id:str): # We create the function unban
    id = int(id) # We convert the id to int
    if interaction.user.guild_permissions.administrator: # If the user has the administrator permission
        memeber = await bot.fetch_user(id)
        await interaction.guild.unban(memeber) # The bot unbans the member
        await interaction.response.send_message(embed=discord.Embed(title=f"{memeber} has been unbaned", color=0x00ff00)) # The bot sends an embed with the member that has been unbaned

@tree.command(name="kick", description="Kick someone", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def kick(interaction: discord.Integration, member: discord.User): # We create the function kick
    if interaction.user.guild_permissions.administrator: # If the user has the administrator permission
        await interaction.guild.kick(member) # The bot kicks the member
        await interaction.response.send_message(embed=discord.Embed(title=f"{member} has been kicked", color=0x00ff00)) # The bot sends an embed with the member that has been kicked
    else:
            
            # If the user doesn't have the administrator permission the bot will send an embed saying that the user doesn't have the permission
            await interaction.response.send_message(embed=discord.Embed(title="You don't have permissons to perform this action", description="This action requires the administrator permission", color=0xff771273493227634689))


# We create a command to timeout someone for one minute in a funny way
@tree.command(name="shoot", description="Shoot someone", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def shoot(interaction: discord.Integration, member: discord.User): # We create the function shoot
    election = random.randint(0, 1) # We create a random number between 0 and 1



    # We create a list with the gifs that we want to use, you can add more using a comma
    rocks = ['https://media.tenor.com/9jAemic43UMAAAAC/sponge-bob-brick.gif', 'https://media.tenor.com/1IEfn4frHZUAAAAd/rock-with.gif']
    shoots = ['https://media.tenor.com/5LQFz4CpTmsAAAAC/pull-the-trigger-fire.gif', 'https://media.tenor.com/724IYPq3pZUAAAAC/gun-shoot.gif']

    if interaction.user.guild_permissions.administrator: # If the user has the administrator permission
        
        if election == 0:

            message = (f"{interaction.user.display_name} has shooted {member.display_name}.")
            reason = "You have been shooted"
            url = random.choice(shoots)
            text=f"He will be back in a minute."

        if election == 1:

            message = f"{interaction.user.display_name} has thrawn a rock to {member.display_name} and he is unconscious."
            reason = "The rock has hit you"
            url = random.choice(rocks)
            text = f"He will be back in a minute."
            
        await member.edit(timed_out_until=discord.utils.utcnow() + timedelta(seconds=60)) # The bot will timeout the member for 60 seconds
    
    else:
        message = "You don't have permissons to perform this action"
        url = 'https://media.tenor.com/9gCRjhzkjBAAAAAC/beta-sigma-male.gif'
        text = f"Return when you have the administrator permission."

    embed = discord.Embed(title=f"{message}" ,color=0x00ff00)
    embed.set_image(url=url)
    embed.set_footer(text=text)


    await interaction.response.send_message(embed=embed) # We send the final message with the embed

@tree.command(name="mute", description="Mute someone", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def mute(interaction: discord.Integration, member: discord.User): # We create the function mute
    if interaction.user.guild_permissions.administrator: # If the user has the administrator permission
        await member.edit(mute=True) # The bot mutes the member
        await interaction.response.send_message(embed=discord.Embed(title=f"{member.display_name} has been muted", color=0x00ff00)) # The bot sends an embed with the member that has been muted
    else:
            
            # If the user doesn't have the administrator permission the bot will send an embed saying that the user doesn't have the permission
            await interaction.response.send_message(embed=discord.Embed(title="You don't have permissons to perform this action", description="This action requires the administrator permission", color=0xff771273493227634689))

@tree.command(name="unmute", description="Unmute someone", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def unmute(interaction: discord.Integration, member: discord.User): # We create the function unmute
    if interaction.user.guild_permissions.administrator: # If the user has the administrator permission
        await member.edit(mute=False) # The bot unmutes the member
        await interaction.response.send_message(embed=discord.Embed(title=f"{member.display_name} has been unmuted", color=0x00ff00)) # The bot sends an embed with the member that has been unmuted
    else:

        # If the user doesn't have the administrator permission the bot will send an embed saying that the user doesn't have the permission
        await interaction.response.send_message(embed=discord.Embed(title="You don't have permissons to perform this action", description="This action requires the administrator permission", color=0xff771273493227634689))

@tree.command(name="deafen", description="Deafen someone", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def deafen(interaction: discord.Integration, member: discord.User): # We create the function deafen
    if interaction.user.guild_permissions.administrator: # If the user has the administrator permission
        await member.edit(deafen=True) # The bot deafens the member
        await interaction.response.send_message(embed=discord.Embed(title=f"{member.display_name} has been deafened", color=0x00ff00)) # The bot sends an embed with the member that has been deafened
    else:
            
            # If the user doesn't have the administrator permission the bot will send an embed saying that the user doesn't have the permission
            await interaction.response.send_message(embed=discord.Embed(title="You don't have permissons to perform this action", description="This action requires the administrator permission", color=0xff771273493227634689))

@tree.command(name="undeafen", description="Undeafen someone", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def undeafen(interaction: discord.Integration, member: discord.User): # We create the function undeafen
    if interaction.user.guild_permissions.administrator: # If the user has the administrator permission
        await member.edit(deafen=False) # The bot undeafens the member
        await interaction.response.send_message(embed=discord.Embed(title=f"{member.display_name} has been undeafened", color=0x00ff00)) # The bot sends an embed with the member that has been undeafened
    else:
            
            # If the user doesn't have the administrator permission the bot will send an embed saying that the user doesn't have the permission
            await interaction.response.send_message(embed=discord.Embed(title="You don't have permissons to perform this action", description="This action requires the administrator permission", color=0xff771273493227634689))

@tree.command(name="help", description="Shows all the available commands", guild = discord.Object(id = 771273493227634689)) # Introduce the id of the server where you want the bot to be, in int format
async def help(interaction: discord.Integration): # We create the function help
    embed = discord.Embed(title="Help", description="All the commands:", color=0x00ff00) # We create the embed
    embed.add_field(name="/kick", value="Kicks a member", inline=False) 
    embed.add_field(name="/ban", value="Bans a member", inline=False) 
    embed.add_field(name="/unban", value="Unbans a member", inline=False) 
    embed.add_field(name="/shoot", value="Timeouts a member", inline=False) 
    embed.add_field(name="/mute", value="Mutes a member", inline=False)
    embed.add_field(name="/unmute", value="Unmutes a member", inline=False)
    embed.add_field(name="/deafen", value="Deafens a member", inline=False)
    embed.add_field(name="/undeafen", value="Undeafens a member", inline=False)
    embed.add_field(name="/help", value="Shows all the available commands", inline=False)
    embed.set_thumbnail(url=bot.user.display_avatar.url)
    embed.set_footer(text="Thank you for using the bot")
    await interaction.response.send_message(embed=embed) # We send the embed



bot.run("TOKEN") # Introduce your bot token to run the bot, must be a str 