import os
import shutil
import random
import inquirer
import textwrap
from colorama import Fore, Style

from Dialogs import *
from Commands import *
from Locations import*

cls = lambda: os.system('cls')

def get_terminal_width():
    columns, _ = shutil.get_terminal_size()
    return columns

def word_wrap(sentence):
    wrapped_text = textwrap.fill(sentence, width=get_terminal_width()-4)
    return wrapped_text

def ask_questions(question:str,choices:list,var = 'temp'):
	question = [inquirer.List(var,message=question,choices=choices)]
	answer = inquirer.prompt(question)
	return answer[var]

def take_commands():
	History = []
	cls()

	#tieing commands to coresponding functions prob has a easier way to do this
	cmds = {"/help":Commands.help,
			"/h":Commands.help,}

	command = None
	while command != "/exit":
		command = input(">>>")
		result = None	
		if command!=None and command in cmds.keys():
			result = cmds[command]()
			print(result)
	cls()

def tell(script:list,color:int):
	color_mapping = {
	    0: Fore.RED,
	    1: Fore.GREEN,
	    2: Fore.BLUE,
		3: Fore.WHITE
	}

	c = color_mapping.get(color, Fore.WHITE)

	History = []
	for dialog in script:
		History.append(f"{c}{Style.BRIGHT}>{dialog}{Style.RESET_ALL}")
		cls()
		for each in History:
			each = word_wrap(each)
			print(each+'\n')

		inp = input(f"{Style.RESET_ALL}Press Enter to continue...")
		if inp == "/cmd":
			take_commands()

		History.pop()
		History.append(f"{c}{dialog}{Style.RESET_ALL}")


# here in order 0,1,2 define color put 3 for white

order = [
(dev_note,0),
(story,1)]

for each in order:
	if callable(each):
		player = each()
		print(player)
	else:
		tell(each[0],each[1])
	
