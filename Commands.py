class Commands:
	def help():
		method_list = [func for func in dir(Commands) if callable(getattr(Commands, func)) and not func.startswith("__")]
		string = str()
		for each in method_list:
			string+= '/'+each+'\n'
		string+='/exit'
		return string
