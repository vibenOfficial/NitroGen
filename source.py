import requests
import random
import string
from termcolor import colored
import os
from colorama import Fore

os.system('cls')

os.system("title Nitro Gen v1.1 ~ Made by viben#0076")

print('')
print('')
print(colored('███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗', 'magenta'))
print(colored('████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║', 'magenta'))
print(colored('██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║', 'magenta'))
print(colored('██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║', 'magenta'))
print(colored('██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║', 'magenta'))
print(colored('╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝', 'magenta'))
print('')
print('')
print(colored('this tool is made by viben#0076, if u edit it pls give me credit!', 'blue'))
print('')
print('')
num = int(input('Amount > '))


with open("codes.txt", "w", encoding='utf-8') as file:

    print('')
    
    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 15
        ))

        file.write(f"https://discord.gift/{code}\n")


with open("codes.txt") as file:
    for line in file.readlines():
        code = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(Fore.GREEN + f"\n\nValid | {code}\n")
        else:
            print(Fore.RED + f"Invalid | {code}")

print('')
input(Fore.GREEN + 'Saved in codes.txt, press enter to exit the program. ')
