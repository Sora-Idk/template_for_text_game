import os
import shutil
import random
import inquirer
import textwrap
from dialogs import *
from colorama import Fore, Style

cls = lambda: os.system('cls')

class Commands:
	def help():
		method_list = [func for func in dir(Commands) if callable(getattr(Commands, func)) and not func.startswith("__")]
		string = str()
		for each in method_list:
			string+= '/'+each+'\n'
		return string
	def set_user_height(): # example command
		return ask_questions("how tall are you?",['short','avg','tall'])


class Player: # working on adding easier ways of making characters this is just a test or rather an example
    def __init__(self):
        is_char_custom = ask_questions("Select A Char:", ['random','custom'])

        if is_char_custom == 'random':
            self.gender = random.choice(['Male','Female'])
            self.height = random.choice(['short','avg','tall'])

        if is_char_custom == 'custom':
            self.gender = ask_questions("what is your gender",['a','b'])
            self.height = ask_questions("How tall are you?",['short','avg','tall'])


def get_terminal_width(): #only used to wrap text in word_wrap() might delete later
    columns, _ = shutil.get_terminal_size()
    return columns

def word_wrap(sentence):
    wrapped_text = textwrap.fill(sentence, width=get_terminal_width()-4)
    return wrapped_text

def ask_questions(question:str,choices:list): 
	question = [inquirer.List('temp',message=question,choices=choices)] #can ask multiple questions but to make it easier to read i just make it ask one at a time (increases lines but makes it easier to understand)
	answer = inquirer.prompt(question)
	return answer['temp']

def take_commands():
	History = []
	cls()

	cmds = {"/help":Commands.help,
			"/h":Commands.help,
			"/set_user_height":Commands.set_user_height}

	command = None
	while command != "/exit":
		command = input(">>>")
		result = None	
		if command!=None:
			if command in cmds.keys():
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
		History.append(f"{c}{Style.BRIGHT}{dialog}{Style.RESET_ALL}")
		#cls()
		for each in History:
			each = word_wrap(each)
			print(each+'\n')

		inp = input(f"{Style.RESET_ALL}Press Enter to continue>>>")
		if inp == "/cmd":
			take_commands()

		History.pop()
		History.append(f"{c}{dialog}{Style.RESET_ALL}")


player= None

# here order is the order of  your story
order = [
(dev_note,3),#devnote is just a list in the file dialogues, 3 is the color white(look at tell())
lambda: Player(), #dont know of other ways to call function so using this 
(opening_scene,1)]#list in dialogues


for each in order:
	if callable(each):
		player = each()# this is still wip wont be like this later
		print(player)
	else:
		tell(each[0],each[1])
	
