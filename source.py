# This code is made by viben#0076, edit this code only if you know what your doing.

import random, string
import os
from termcolor import colored
from colorama import Fore

os.system('cls')

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

os.system("title Nitro Gen v1 ~ Made by viben#0076")

amount = int(input('Amount > '))
value = 1
while value <= amount:
	code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=15))
	f = open('codes.txt', "a+")
	f.write(f'{code}\n')
	print(colored(f'{code}', 'yellow'))
	value += 1
print('')
input(Fore.GREEN + 'Saved in codes.txt, press enter to exit the program. ')
