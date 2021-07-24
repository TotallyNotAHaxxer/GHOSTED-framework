import os 
import sys  
import time
import webbrowser
import json # to store tracing and recived data  
import requests # for IP trcae r
import urllib # urllib to parse url 
import twint # twint for twitter scraping 
import tabulate # tabulate for format 
import colorama  # color 
import phonenumbers # phone num tracing outside us
import webbrowser # to open google maps link for Ip tracer 4
import pyfiglet # for design 
from phonenumbers import timezone #timezone 
from phonenumbers import carrier # carrier 
from phonenumbers import geocoder, carrier # carrier and location 
from colorama import Fore  #color
from colorama import Back  #color
from colorama import Style #color
from geopy.geocoders import Nominatim ### snap 
from urllib.request import urlopen as open


time.sleep(1)
os.system(' clear ')

#animation for label  
def load_animation(): 
  
    load_str = "Loading GH0ST3D."
    ls_len = len(load_str) 
  
    animation = "|/-|/-\|/-/"
    anicount = 0
      
    counttime = 0        
       
    i = 0                     
  
    while (counttime != 30): 
          

        time.sleep(0.075)  
                              
        load_str_list = list(load_str)  
 
        x = ord(load_str_list[i]) 
          
        y = 0                             

        if x != 32 and x != 46:              
            if x>90: 
                y = x-32
            else: 
                y = x + 32
            load_str_list[i]= chr(y) 
          
        res =''              
        for j in range(ls_len): 
            res = res + load_str_list[j] 
              
        sys.stdout.write("\r"+res + animation[anicount]) 
        sys.stdout.flush() 
  
        load_str = res 
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len 
        counttime = counttime + 1
      
          
    # for linux / Mac OS 
    else: 
        os.system("clear") 
#driver 
if __name__ == '__main__':  
    load_animation() 

print(Fore.LIGHTBLACK_EX+" XD ")
os.system(' clear ')
print(Fore.RED+"      ___           ___           ___           ___           ___ ")     
print(Fore.LIGHTBLACK_EX+"     /\  \         /\__\         /\  \         /\  \         /\  \     ")
print(Fore.RED+"    /::\  \       /:/  /        /::\  \       /::\  \        \:\  \    ")
print(Fore.LIGHTBLACK_EX+"   /:/\:\  \     /:/__/        /:/\:\  \     /:/\ \  \        \:\  \   ")
print(Fore.RED+"  /:/  \:\  \   /::\  \ ___   /:/  \:\  \   _\:\~\ \  \       /::\  \  ")
print(Fore.LIGHTBLACK_EX+" /:/__/_\:\__\ /:/\:\  /\__\ /:/__/ \:\__\ /\ \:\ \ \__\     /:/\:\__\ ")
print(Fore.RED+" \:\  /\ \/__/ \/__\:\/:/  / \:\  \ /:/  / \:\ \:\ \/__/    /:/  \/__/ ") #banner 
print(Fore.LIGHTBLACK_EX+"  \:\ \:\__\        \::/  /   \:\  /:/  /   \:\ \:\__\     /:/  /   ")  
print(Fore.RED+"   \:\/:/  /        /:/  /     \:\/:/  /     \:\/:/  /     \/__/  ")    
print(Fore.LIGHTBLACK_EX+"    \::/  /        /:/  /       \::/  /       \::/  /           ")      
print(Fore.RED+"     \/__/         \/__/         \/__/         \/__/          ")        
time.sleep(1)
time.sleep(0.1)
print("___________________________________________________________________________________________")
print("|[1] Trace a IPV4         | [2] Trace a Phone number              | [3] Gather User info  | ")
time.sleep(0.1)
print("|[4] Trace a username     | [5] Gather and Mine tweets from a acc | [6] Download snap IF  |")
time.sleep(0.1)
print("|[7] Trace a US phone num | [8] Scan a IP for Ports               | [9] Run Brute forceFW |")
time.sleep(0.1)
print("|_________________________________________________________________________________________|")
options = input(" Options@> ") #input for user 

if '7' in options: # if to conduct else if statement 
       os.system(' clear ')
       num = str(input(" US Num ==> "))
       time.sleep(1)
       os.system(' chmod +x ./ph33rNoNum.sh ')
       os.system(f' sudo ./ph33rNoNum.sh --num {num} --csv ')
       time.sleep(15)
       os.system(' clear ')
       print(" [=] data saved to a CSV file [=] ")

elif '9' == options:
    os.system(' clear ')
    time.sleep(1)
    print(" running framework [=] ")
    time.sleep(1)
    os.system(' sudo python3 BRUTY.py ')

elif '8' == options:
    time.sleep(1)
    os.system(' clear ')
    V = str(input(" IPV4 @>>>> "))
    os.system(f' python3 Scan.py {V} ')


elif '6' == options: 
    os.system(' clear ')
    print(" [=] why hello there :D [=] ")
    time.sleep(1)
    os.system(' clear ')
    address = str(input(" Address @>> "))
    radius = str(input(" radius DEF 5000 @>> "))
    time.sleep(1)
    os.system(f' python3 snap.py --address {address} --radius {radius} ')
    os.system(' clear ')
    print(" [+] data has been saved to file [+] ")

elif '5' == options:
    os.system(' clear ')
    os.system(' clear ')
    time.sleep(1)
    print(" [+] Loading script [+] ")
    time.sleep(1)
    os.system(' clear ')
    time.sleep(0.1)
    print(Fore.MAGENTA+"             ___________       .__.__  __ ")                                                             
    time.sleep(0.1)
    print(Fore.MAGENTA+"             \__    ___/_  _  _|__|__|/  |_  ___________        ")                   
    time.sleep(0.1)
    print(Fore.RED+"               |    |  \ \/ \/ /  |  \   __\/ __ \_  __ \ ")                         
    time.sleep(0.1)
    print(Fore.MAGENTA+"               |    |   \     /|  |  ||  | \  ___/|  | \/   ")                       
    time.sleep(0.1)
    print(Fore.RED+"               |____|    \/\_/ |__|__||__|  \___  >__|        ")                     
    time.sleep(0.1)
    print(Fore.MAGENTA+"            .___        __         .__  .__  .__\/              ")                   
    time.sleep(0.1)
    print(Fore.RED+"            |   | _____/  |_  ____ |  | |  | |__| ____   ____   ____   ____  ____  ")
    time.sleep(0.1)
    print(Fore.MAGENTA+"            |   |/    \   __\/ __ \|  | |  | |  |/ ___\_/ __ \ /    \_/ ___\/ __ \ ")
    time.sleep(0.1)
    print(Fore.RED+"            |   |   |  \  | \  ___/|  |_|  |_|  / /_/  >  ___/|   |  \  \__\  ___/ ")
    time.sleep(0.1)
    print(Fore.MAGENTA+"            |___|___|  /__|  \___  >____/____/__\___  / \___  >___|  /\___  >___  > ")
    time.sleep(0.1)
    print(Fore.RED+"                     \/          \/            /_____/      \/     \/     \/    \/ ")
    time.sleep(0.1)
    print(Fore.MAGENTA+"       /.\                          ")
    time.sleep(0.1)
    print(Fore.RED+"          \                  ")
    time.sleep(0.1)
    print(Fore.MAGENTA+"      /                    ")
    time.sleep(0.1)
    print(Fore.RED+"     //  /                  ")
    time.sleep(0.1)
    print(Fore.MAGENTA+"     |/ /\_==================")
    time.sleep(0.1)
    print(Fore.RED+"     / /            ")
    time.sleep(0.1)
    print(Fore.MAGENTA+"    / /     ")
    time.sleep(0.1)
    print(Fore.RED+"    \/ ")
    time.sleep(1)
    print(" Usage: input a username and scrape tweets                  | EX: JoeBiden ")

    A = str(input(" @> "))
    time.sleep(1)
    os.system(' clear ')
    print("______________________________")
    print("|Would you like the user ID's|")
    print("|To be saved to a output file|")
    print("|____________________________|")
    print(" True or False? ")
    B = str(input(" @> "))
    os.system(' clear ')
    print("|-----------------------|")
    print("|name of file for output|")
    print("|-----------------------|")
    time.sleep(1)
    file = str(input(" @> "))
    os.system(' clear ')
    time.sleep(1)
    print(Fore.CYAN+" XD ")
    os.system(' clear ')
    print(" ______________________________________________")
    print(" | How much tweets would you like to limit to | ")
    print(" | limit = 1-3200 Tweets Per Search           | ")
    print(" |--------------------------------------------|")
    num = str(input(" @> "))
    time.sleep(1)
    os.system(' clear ')
    print(" [=] Scraping tweets [=] ")
    os.system(' clear ')
    time.sleep(0.1)
    print(Fore.MAGENTA+"             ___________       .__.__  __ ")                                                             
    time.sleep(0.1)
    print(Fore.MAGENTA+"             \__    ___/_  _  _|__|__|/  |_  ___________        ")                   
    time.sleep(0.1)
    print(Fore.RED+"               |    |  \ \/ \/ /  |  \   __\/ __ \_  __ \ ")                         
    time.sleep(0.1)
    print(Fore.MAGENTA+"               |    |   \     /|  |  ||  | \  ___/|  | \/   ")                       
    time.sleep(0.1)
    print(Fore.RED+"               |____|    \/\_/ |__|__||__|  \___  >__|        ")                     
    time.sleep(0.1)
    print(Fore.MAGENTA+"            .___        __         .__  .__  .__\/              ")                   
    time.sleep(0.1)
    print(Fore.RED+"            |   | _____/  |_  ____ |  | |  | |__| ____   ____   ____   ____  ____  ")
    time.sleep(0.1)
    print(Fore.MAGENTA+"            |   |/    \   __\/ __ \|  | |  | |  |/ ___\_/ __ \ /    \_/ ___\/ __ \ ")
    time.sleep(0.1)
    print(Fore.RED+"            |   |   |  \  | \  ___/|  |_|  |_|  / /_/  >  ___/|   |  \  \__\  ___/ ")
    time.sleep(0.1)
    print(Fore.MAGENTA+"            |___|___|  /__|  \___  >____/____/__\___  / \___  >___|  /\___  >___  > ")
    time.sleep(0.1)
    print(Fore.RED+"                     \/          \/            /_____/      \/     \/     \/    \/ ")
    time.sleep(0.1)
    print(" [=] data has been saved to a file [=] ")

    c = twint.Config()

    c.Username = f"{A}" #formating for string 
    c.Custom["tweet"] = ["id"]
    c.Custom["user"] = ["bio"] 
    c.Limit = f"{num}"
    c.Store_csv = f"{B}" 
    c.Output = f"{file}"

    twint.run.Search(c)

elif '4' == options:
    os.system(' clear ')
    time.sleep(0.5)
    #print(" ==Username== ")
    #user = str(input(" @>>> "))#
    #git clone https://github.com/wishihab/userrecon.git
    #cd userrecon 
    # chmod +x ./userrecon.sh 
    os.system(' clear ')
    os.system(' ./userrecon.sh ')

elif '3' == options:
    os.system(' clear ') # clear termina; 
    print(" [=] Finally you use me :< ") # why not 
    time.sleep(1)
    os.system(' pip install profil3r ') # extra install why not  # might add req.txt 
    os.system(' clear ')
    user = str(input(" Username @>>>  ")) # string for automation 
    os.system(' clear ')
    time.sleep(1)
    print(" happy tracking [!] ")
    os.system(f' profil3r -p {user} ') # f for formating with tools 

elif '2' == options: 
    os.system(' clear ')
    print(" YESSSS!! ")
    time.sleep(1)
    os.system(' clear ')
    banner = pyfiglet.figlet_format("GHOST", font = "isometric1")
    print(banner)
    time.sleep(1)
    print(Fore.LIGHTBLACK_EX+" usage EX| +1 000-000-000")
    ph = str(input(" @> "))
    # parsing to input 
    phoneNumber = phonenumbers.parse(f"{ph}")
    #timezone 
    timeZone = timezone.time_zones_for_number(phoneNumber)
    # carrier 
    Carrier = carrier.name_for_number(phoneNumber, 'en')
    Region = geocoder.description_for_number(phoneNumber, 'en')
    #valid or not 
    valid = phonenumbers.is_valid_number(phoneNumber)
    possible = phonenumbers.is_possible_number(phoneNumber)
    print("=======NUMBER======")
    time.sleep(0.1)
    print(phoneNumber)
    time.sleep(0.1)
    print("========TIMEZ=======")
    time.sleep(0.1)
    print(timeZone)
    time.sleep(0.1)
    print("========ISP=========")
    time.sleep(0.1)
    print(Carrier)
    time.sleep(0.1)
    print("=======REGION=======")
    time.sleep(0.1)
    print(Region)
    time.sleep(0.1)
    print("======VALID=========")
    time.sleep(0.1)
    print(valid)
    time.sleep(0.1)
    print("======Possible======")
    time.sleep(0.1)
    print(possible)
    time.sleep(0.1)
    print("=================")
    time.sleep(3)

elif '1' == options: #elif for == statements in option input 
    print(" hello senpai :> ")
    time.sleep(1)
    import pyfiglet
    import sys
    import socket
    from datetime import datetime
    os.system('clear')

    #colors 
    # RED ++++ print(\033[31m)


    print(Fore.RED+"                $$$$$$\ $$$$$$$\        $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  ")
    print(Fore.MAGENTA+"		\_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\  ")
    print(Fore.RED+"  		  $$ |  $$ |  $$ |         $$ |   $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ | ")
    print(Fore.MAGENTA+"  		  $$ |  $$$$$$$  |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  | ")
    print(Fore.RED+"  		  $$ |  $$  ____/          $$ |   $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$<  ")
    print(Fore.MAGENTA+" 		  $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ | ") 
    print(Fore.RED+"		$$$$$$\ $$ |               $$ |   $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ | ")
    print(Fore.MAGENTA+"		\______|\__|               \__|   \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__| ")

    #\033[1;32m = cyan 
    print(Fore.CYAN+"|======================================================================================================|")
    print(Fore.BLUE+"|Github: ArkAngeL43 | https://github.com/ArkAngeL43                                                    |")
    print(Fore.MAGENTA+"|instagram ark_angel6                                                                                  |")
    print(Fore.BLUE+"|NOTES:::::: if you want to exit the script just type exit, its easier than ctrl+c+d                   |")
    print(Fore.CYAN+"|======================================================================================================|")

    #LOOP WITHOUT ELSE +++ while True:
    global ip
    ip = input("\033[1;36mEnter Your Target IP: \033[1;36m")

    if 'Exit' in ip:
            os.system(' clear ')
            time.sleep(1)
            print(" [+] Thanks for stopping by [+] ")
            print(" [=] Have a good one :D     [=]")
            time.sleep(2)
            sys.exit()

    elif 'exit' in ip:
                os.system(' clear ')
                time.sleep(1)
                print(" [+] Thanks for stopping by [+] ")
                print(" [=] Have a good one :D     [=]")
                time.sleep(2)
                sys.exit()

    url = "http://ip-api.com/json/"
    response = open(url + ip)
    data = response.read()
    values = json.loads(data)
    status = values['status']
    success = "success"
    lat = str(values['lat'])
    lon = str(values['lon'])
    a = lat + ","
    b = lon + "/"
    c = b + "data=!3m1!1e3?hl=en"
    location = a + c

    time.sleep(1)
    os.system(' clear ')
    os.system(' mpg123 loc.mp3 ')
    os.system(' clear ')
    time.sleep(1)
    print(Fore.RED+"                $$$$$$\ $$$$$$$\        $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  ")
    time.sleep(0.1)
    print(Fore.RED+"		\_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\  ")
    time.sleep(0.1)
    print(Fore.RED+"  		  $$ |  $$ |  $$ |         $$ |   $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ | ")
    time.sleep(0.1)
    print(Fore.RED+"  		  $$ |  $$$$$$$  |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  | ")
    time.sleep(0.1)
    print(Fore.RED+"  		  $$ |  $$  ____/          $$ |   $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$<  ")
    time.sleep(0.1)
    print(Fore.RED+" 		  $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ | ") 
    time.sleep(0.1)
    print(Fore.RED+"		$$$$$$\ $$ |               $$ |   $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ | ")
    time.sleep(0.1)
    print(Fore.RED+"		\______|\__|               \__|   \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__| ")
    time.sleep(0.1)
    print("---------------------------------")
    time.sleep(0.1)
    print(" [=] IP: " + values['query']        )
    time.sleep(0.1)
    print(" [=] Status: " + values['status']   )
    time.sleep(0.1)
    print(" [=] city: " + values['city']       )
    time.sleep(0.1)
    print(" [=] ISP: " + values['isp']         )
    time.sleep(0.1)
    print(" [=] latitude: " + lat              )
    time.sleep(0.1)
    print(" [=] longitude: " + lon             )
    time.sleep(0.1)
    print(" [=] country: " + values['country'] )
    time.sleep(0.1)
    print(" [=] region: " + values['regionName'])
    time.sleep(0.1)
    print(" [=] city: " + values['city']       )
    time.sleep(0.1)
    print(" [=] zip: " + values['zip']         )
    time.sleep(0.1)
    print(" [=] AS: " + values['as']           )
    time.sleep(0.1)
    print("---------------------------------")
    time.sleep(1)
    print(" [+] opening location LINK [+] ")
    maps = "https://www.google.com/maps/search/"
    webbrowser.open(maps + location)
    print(" [-] would you like to scan the ports of this IP? ")
    time.sleep(2)
    B = str(input(" ┌─[User7]-[~/main/IPTracer]──╼"))
    time.sleep(1)

    if 'yes' in B:
            time.sleep(1)
            print(" [+] cleaning up [+] ")
            time.sleep(1)
            os.system(' clear ')
            os.system(f' python3 Scan.py {ip} ')

    elif 'no' in B:
            os.system(' clear ')
            print(" [-] cleaning up [-] ")
            time.sleep(1)
            sys.exit()

    elif 'No' in B:
            os.system(' clear ')
            pritn(" [-] cleaning up [-] ")
            time.sleep(1)
            sys.exit()

    elif 'Yes' in B:
            time.sleep(1)
            print(" [+] cleaning up [+] ")
            time.sleep(1)
            os.system(' clear ')
            os.system(f' python3 Scan.py {ip} ')            


    elif 'sure' in B:
                time.sleep(1)
                print(" [+] cleaning up [+] ")
                time.sleep(1)
                os.system(' clear ')
                os.system(f' python3 Scan.py {ip} ')      

    elif 'YE' in B:
            time.sleep(1)
            print(" [+] cleaning up [+] ")
            time.sleep(1)
            os.system(' clear ')
            os.system(f' python3 Scan.py {ip} ')      

    elif 'YEE' in B:
            time.sleep(1)
            print(" [+] cleaning up [+] ")
            time.sleep(1)
            os.system(' clear ')
            os.system(f' python3 Scan.py {ip} ')      
       

#print("="* 60)
#banner = pyfiglet.figlet_format("GHOST", font = "isometric1")
#print(banner)
#print("="* 60)