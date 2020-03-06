
def picklanguage():
	language = int(input("What language do you speak? 1 for English, 2 for Spanish, 3 for French:  "))
	return language	 


def name_input(language):
	"""
	This is a function that asks your name
	"""
	if language == 1:
		name  = input("What is your name?  ")
		print("Hello " + name) 	 
	elif language == 2:
		name = input("Como se llama?  ")
		print("Hola " + name)
	elif language == 3:
		name = input("Comment vous appelez-vous?  ")
		print ("Bonjour " + name)
	else:
		print("Didn't select an option!")
		
	

name_input(picklanguage())

