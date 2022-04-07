choice = True

import random, string
import os
from termcolor import colored
from colorama import Fore
import requests

os.system("cls")

os.system("title NitroGen v1.3 ~ Made by viben#6633 [Menu]")

print('')
print('')
print(colored('███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗', 'magenta'))
print(colored('████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║', 'magenta'))
print(colored('██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║', 'magenta'))
print(colored('██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║', 'magenta'))
print(colored('██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║', 'magenta'))
print(colored('╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝', 'magenta'))
print('')
print(colored('this is a tool made by viben#6633, if you edit it please give me credit!', 'blue'))
print('')
print('[1] Generator')
print('[2] Generator + Checker')
print("[3] Exit")
print("")
print("")

choice = input("Choice > ")

if choice == '1':
 os.system('cls')

 print('')
 print('')
 print(colored('███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗', 'magenta'))
 print(colored('████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║', 'magenta'))
 print(colored('██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║', 'magenta'))
 print(colored('██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║', 'magenta'))
 print(colored('██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║', 'magenta'))
 print(colored('╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝', 'magenta'))
 print("")
 print(colored('this is a tool made by viben#6633, if you edit it please give me credit!', 'blue'))
 print('')
 print('')

 os.system("title Nitro Gen v1.3 ~ Made by viben#6633 [Generator]")

 amount = int(input('Amount > '))
 value = 1
 while value <= amount:
  code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=15))
  f = open('unchecked.txt', "a+")
  f.write(f'{code}\n')
  print(colored(f'{code}', 'yellow'))
  value += 1
 print("")
 print("")
 input(colored("Saved in unchecked.txt, press enter to exit the program. ", 'green'))

elif choice == '2':
 os.system('cls')

 os.system("title Nitro Gen v1.3 ~ Made by viben#6633 [Generator + Checker]")

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
 print(colored('this is a tool made by viben#6633, if you edit it please give me credit!', 'blue'))
 print('')
 print('')
 num = int(input('Amount > '))


 with open("checked.txt", "w", encoding='utf-8') as file:

    print('')
    
    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 15
        ))

        file.write(f"https://discord.gift/{code}\n")


 with open("checked.txt") as file:
    for line in file.readlines():
        code = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(Fore.GREEN + f"\n\nValid | {code}\n")
        else:
            print(Fore.RED + f"Invalid | {code}")

 print('')
 input(Fore.GREEN + 'Saved in checked.txt, press enter to exit the program. ')

elif choice == '3':
 quit()

else:
 os.system("cls")
 os.system("title Nitro Gen v1.3 ~ Made by viben#6633 [Error]")
 print('')
 print('')
 print(colored('███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗', 'magenta'))
 print(colored('████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║', 'magenta'))
 print(colored('██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║', 'magenta'))
 print(colored('██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║', 'magenta'))
 print(colored('██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║', 'magenta'))
 print(colored('╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝', 'magenta'))
 print('')
 print(colored('this is a tool made by viben#6633, if you edit it please give me credit!', 'blue'))
 print("")
 print("")
 print(colored("Oops! Looks like this isn't a correct choice!", 'red'))
 print("")
 print("")
 input(colored("Press enter to exit the program... ", 'yellow'))
