import os
import colorama
from colorama import Fore
print(Fore.BLUE + "          ____                                                                     ")
print(Fore.BLUE + "        /\  _`\                                                                   ")
print(Fore.BLUE + "         \ \,\L\_\    __  __  __     __      __        " + Fore.RED + "_____    __  __             ")
print(Fore.WHITE + " _______ " + Fore.BLUE + " \/_\__ \   /\ \/\ \/\ \  /'__`\  /'__`\     " + Fore.RED + "/\ '__`\ /\ \/\ \   " + Fore.WHITE + " _______ ")
print("/\______\   " + Fore.BLUE + "/\ \L\ \ \ \ \_/ \_/ \/\  __/ /\  __/  __ " + Fore.RED + "\ \ \L\ \\ \ \_\ \ " +  Fore.WHITE + " /\______|")
print("\/______/   " + Fore.BLUE + "\ `\____\ \ \___x___/'\ \____\\ \____\/\_\ " + Fore.RED + "\ \ ,__/ \/`____ \ " + Fore.WHITE + "\/______/")
print("             " + Fore.BLUE + "\/_____/  \/__//__/   \/____/ \/____/\/_/  " + Fore.RED + "\ \ \/   `/___/> \         ")
print("                                                         " + Fore.RED + "\ \_\      /\___/         ")
print("                                                          " + Fore.RED + "\/_/      \/__/          ")
print(Fore.YELLOW + "By Mohamad Hani Janaty")
print(Fore.GREEN + "instagram : mohamadhanijanaty85")
print("aparat : aparat.com/hanicraft2")
print("telegram : @hani_j85")
print("reddit : u/mhjhacker1")
print(Fore.CYAN + "select tool you wanna use")
print("[1] API Brute")
print("[2] FireFox History Tracer")
print("[3] Phishing Mailer")
print("[4] Port Scanner (Simple Mode)")
print("[5] SSL Issuer (Requires nmapscan.xml To Be In Folder)")
print("more tools will be added in next updates")
a = input("Enter Tool Number (Ex 1,2,3) : ")
if a=='1':
    os.system("python ./Data/APIBrute.py")
elif a=='2':
    os.system("python ./Data/FirefoxHistory.py")
elif a=='3':
    os.system("python ./Data/PhishingMailer.py")
elif a=='4':
    os.system("python ./Data/PortScanner.py")
elif a=='5':
    os.system("python ./Data/SSLissuer.py nmapscan.xml")
else:
    print("Please Enter A Valid Tool Number")