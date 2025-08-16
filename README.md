Note: All tokens in commit history are now expired

# Remote-Control
## This project will almost certainly no longer be updated. No idea if it still works. I'll likely remake it in C, or something similar.

type shi

### This was fully created as practice with Python, and is inefficient and slow, with few practical capabilities.
Libraries are a little wonky, you might need to find some of them yourself.

**TO DO (in no particular order)**
1. Keylogger? Eventually?
2. Reverse shell shortcut (done, hopefully?)
3. More detailed details command (idk what else to add)
4. Figure out how to make a bunch of params that the user can ignore if they want (look into parsing lib)
5. Make it a telegram bot? :O
6. Integrate MQTT protocol to send some data


**COMMANDS**
1. Details 
  Usage: !details
  Does: Prints  of the client computer (hostname, public/private IPv4, MAC address, User, OS info, cwd)
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
  Does: Overwrites everything with your own content. Keep in mind you can use this to create a new file too
12. WiFi
  Usage: !wifi
  Does: Sends all stored WiFi passwords
13. Steal
   Usage: !steal fileName
   Does: Uploads the file to discord for you to download
14. Inject
   Usage: !inject downloadLink
   Does: Downloads a file to the client computer, in the cwd
15. Passwords
   Usage: !passwords
   Does: Steals all **CHROME** passwords
16. Screenshot
   Usage: !screenshot
   Does: Screenshots client screen
17. Reverse shell
   Usage: !revshell IP PORT
   Does: Initiates a reverse shell on a given ip and port
18. Move
  Usage: !move fileName destination
  Does: Moves a file
