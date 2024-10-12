import os,sys,platform
def clearscr():
    if platform.system() == "Windows":
        os.system('cls')  # Clear screen for Windows
    else:
        os.system('clear')
RESET = "\033[0m"
Blod = "\033[1m"
RED = "\033[31m"

def MenuDelete():
    try:
        textMD="""
######################################################
#   Delete "PowerShell" to context Menus       --(1) #
#   Delete "Command Prompt" to context Menus   --(2) #
#   Delete "Firewall" to context Menus         --(3) #
#   Delete "Network" to context Menus          --(4) #
#   Delete "registryFile" to context Menus     --(5) #
#   Delete "registryFile" to context Menus     --(5) #
#   Delete "ShellFile" to context Menus        --(6) #
#   Delete "SystemProperties" to context Menus --(7) #
#   To exit Enter                              --(0) #
######################################################   
    """
        checkDE = int(input(textMD+"\n"+"Enter Number Between 0-->7 :  "))   
        if checkDE ==1:
            #Delete Powershell To Context Cenu
            os.system(r'outils\PowerShellDELETE.bat')
            clearscr()
        elif checkDE==2:
            #Delete CommandPrompt To Context Menu
            os.system(r'outils\CommandPromptDELETE.bat')
            clearscr()
        elif checkDE==3:
            #Delete Firewall To Context Menu
            os.system(r'outils\FirewallDELETE.bat')
            clearscr()
        elif checkDE==4:
            #Delete Network To Context Menu
            os.system(r'outils\NetworkDELETE.bat')
            clearscr()
        elif checkDE==5:
            #Delete RegistryFile To Context Menu in New
            os.system(r'outils\RegistryFileDELETE.bat')
            clearscr()
        elif checkDE==6:
            #Delete ShellFile To Context Menu in New
            os.system(r'outils\ShellFileDELETE.bat')
            clearscr()
        elif checkDE==7:
            #Delete SystemProperties To Context Menu in New
            os.system(r'outils\SystemPropertiesDELETE.bat')
            clearscr()
        elif checkDE==0:
            clearscr()
            Menu()
        else:
            clearscr()
            print(f"{Blod}{RED}Please Enter Number Between 0 ------------> 7{RESET}")
        MenuDelete() 
    except ValueError as e:
        clearscr()
        print(f"{Blod}{RED}Invalid input. Please enter a valid integer between 0 and 7.\n{RESET}")
        MenuDelete()

        
def MenuAdd():
    try:
        textMADD="""
######################################################
#   Add "PowerShell" to context Menus       --(1)    #
#   Add "Command Prompt" to context Menus   --(2)    #
#   Add "Firewall" to context Menus         --(3)    #
#   Add "Network" to context Menus          --(4)    #
#   Add "registryFile" to context Menus     --(5)    #
#   Add "ShellFile" to context Menus        --(6)    #
#   Add "SystemProperties" to context Menus --(7)    #
#   To exit In The Menu Enter               --(0)    #
######################################################   
"""
        checkADD = int(input(textMADD+"\n"+"Enter Number Between 0-->7 :  "))
        if checkADD ==1:
            #Add Powershell To Context Cenu
            os.system(r'outils\PowerShell.bat')
            clearscr()
        elif checkADD==2:
            #Add CommandPrompt To Context Menu
            os.system(r'outils\CommandPrompt.bat')
            clearscr()
        elif checkADD==3:
            #Add Firewall To Context Menu
            os.system(r'outils\Firewall.bat')
            clearscr()
        elif checkADD==4:
            #Add Network To Context Menu
            os.system(r'outils\Network.bat')
            clearscr()
        elif checkADD==5:
            #Add RegistryFile To Context Menu in New
            os.system(r'outils\RegistryFile.bat')
            clearscr()
        elif checkADD==6:
            #Add ShellFile To Context Menu in New
            os.system(r'outils\ShellFile.bat')
            clearscr()
        elif checkADD==7:
            #Add SystemProperties To Context Menu in New
            os.system(r'outils\SystemProperties.bat')
            clearscr()
        elif checkADD==0:
            clearscr()
            Menu()
        else:
            clearscr()
            print(f"{Blod}{RED}Please Enter Number Between 0 ------------> 7{RESET}")
        MenuAdd() 
    except ValueError as e:
        clearscr()
        print(f"{Blod}{RED}Invalid input. Please enter a valid integer between 0 and 7.\n{RESET}")
        MenuAdd()
def Menu():
    try:
        textM="""
######################################################
#   To Add Context Menus                --(add)      #
#   To Delete Context Menus             --(delete)   #
#   To exit Enter                       --(exit)     #
###################################################### 
"""
        input_TextM = input(textM+"     :   ").lower()
        if input_TextM == "exit":
            clearscr()
            sys.exit(0)
        elif input_TextM == "add":
            clearscr()
            MenuAdd()
        elif input_TextM == "delete" :
            clearscr()
            MenuDelete()
    except ValueError :
                print(f"{Blod}{RED}Invalid input. Please enter a valid integer between 0 and 2.\n{RESET}")
                Menu()

while True :
    clearscr()
    Menu()
