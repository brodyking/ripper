from colorama import Fore, Back, Style
import os

def initPrompt():
    initInput = input("Ripper> ")
    if (initInput == ''):
        initPrompt()
    else:
        run(initInput)

def run(givenInput):
    # List of all commands
    commands = ['help','h','download','d','stream','s','quit','q','about','a']
    # Checks to see if the command given is a valid command
    if (any(givenInput in x for x in commands)):
        # Help
        if (givenInput == "help" or givenInput == 'h'):
            print("")
            print("    Available Commands:")
            print(Fore.RED +"    [help/h]"+Fore.WHITE+"     Displays help screen")
            print("")
            print(Fore.RED +"    [about/a]"+Fore.WHITE+"    About information")
            print("")
            print(Fore.RED +"    [quit/q]"+Fore.WHITE+"     Quit the Application")
            print("")
            print(Fore.RED +"    [download/d]"+Fore.WHITE+" Open the download application.")
            print("                 You can put Spotify or Youtube")
            print("                 links as inputs or type song  ")
            print("                 names for a faster search.")
            print("")
            print(Fore.RED +"    [stream/s]"+Fore.WHITE+"   Stream youtube videos with URL. ")
            print("                 Note: this requires MPV.")
            print(Style.RESET_ALL + "")
            initPrompt()
        if (givenInput == "download" or givenInput == 'd'):
            givenInput = input("Ripper / Downloader> ")
            if (givenInput[0:24] == "https://open.spotify.com"):
                os.system('spotdl ' + givenInput)
                initPrompt()
            elif (givenInput[0:24] == "https://www.youtube.com/"):
                os.system('yt-dlp ' + givenInput)     
                initPrompt()
            else:
                os.system('spotdl "' + givenInput + '"')
                initPrompt()   
        if (givenInput == "stream" or givenInput == 's'):
                    givenInput = input("Ripper / Streamer> ")
                    if (givenInput[0:24] == "https://www.youtube.com/"):
                        os.system('mpv ' + givenInput)
                        initPrompt()
                    else:
                        print(Fore.RED + "[!] Not a valid YouTube URL." + Style.RESET_ALL)
        if (givenInput == 'q' or givenInput == 'quit'):
            exit()
        if (givenInput == 'a' or givenInput == 'about'):
            print("")
            print("         Ripper")
            print(Fore.RED +"       version: " + Style.RESET_ALL + "1.0")
            print(Fore.RED +"          date: " + Style.RESET_ALL + "Jun 14 2024")
            print(Fore.RED +"       credits: " + Style.RESET_ALL + "spotdl, yt-dlp, mpv, colorama")
            print("")
            initPrompt()
    else:
        print(Fore.RED + "[!] Command not Found." + Style.RESET_ALL)
        initPrompt()

initPrompt()
