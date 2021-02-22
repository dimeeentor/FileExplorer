# File Explorer v.1.1
import os

# Variables
TEMP 		  = os.environ.get('TEMP')
SYSTEM_ROOT 	  = os.environ.get('SYSTEMROOT')
USER_PROFILE 	  = os.environ.get('USERPROFILE')
PROGRAM_FILES 	  = os.environ.get('PROGRAMFILES')
PROGRAM_FILES_X86 = os.environ.get('PROGRAMFILES(X86)')

# Function
def help():
	print('\nHelp Shortcuts:\n1) Change directory (change, cd).\n2) Show files in this directory (show, ls).\n3) Execute a specific file (run).\n4) Clean \'TEMP\' folder (clean, cltmp).\n\nIf you are in menu \'File To Open (run)\' enter \'none\' to exit this menu.')

def tempCleaner(path):
	for file in os.listdir(path):
		try:
			os.remove(f'{path}\{file}')
			print(f'Deleted: {path}\{file}')
		except PermissionError or FileNotFoundError:
			print(f'[!] Cannot delete: {path}\{file}')
			continue

def showFiles(path, detailed = False):
	if detailed or detailed == 'T' or detailed == 't':
		for root, dirs, files in os.walk(path, topdown = True):
			print(f'Root: {root}\nDirectories: {dirs}\nFiles: {files}\n')
		
	else:
		for file in os.listdir(currentDir):
			print(f'{file}')
		
def changeDirectory():
	while True:
		try:
			changeDirectory = input('Enter the new directory: ').strip()
			if changeDirectory == 'help' or changeDirectory == '-h':
				print(f'\n[!] Some shortcuts:\n1) Windows (W, w) - \'{SYSTEM_ROOT}\'\n2) User Folder (UF, uf) - \'{USER_PROFILE}\'\n3) Program Files (PF, pf) - \'{PROGRAM_FILES}\'\n4) Program Files (x86) (PF86, pf86) - \'{PROGRAM_FILES_X86}\'\n')
				continue
			elif changeDirectory == 'Windows' or changeDirectory == 'W' or changeDirectory == 'w':
				os.chdir(SYSTEM_ROOT)
			elif changeDirectory == 'User Folder' or changeDirectory == 'UF' or changeDirectory == 'uf':
				os.chdir(USER_PROFILE)
			elif changeDirectory == 'Program Files' or changeDirectory == 'PF' or changeDirectory == 'pf':
				os.chdir(PROGRAM_FILES)
			elif changeDirectory == 'Program Files (x86)' or changeDirectory == 'PF86' or changeDirectory == 'pf86':
				os.chdir(PROGRAM_FILES_X86)
			else:
				os.chdir(changeDirectory)

			print('Directory has changed successfully...')	
			break

		except FileNotFoundError:
			print('\nSpecified directory does not exist.\nCheck if the directory is correct.\n')
			continue
		except PermissionError:
			print('\n[You do not have any permission to get into this directory.\n')
			continue
		except NotADirectoryError:
			print('\n[Must be a directory.\n')
			continue
		except OSError:
			print('\nSpecified directory does not exist.\nCheck if the directory is correct.\n')
			continue

# Main Logic
while True:
	currentDir = os.getcwd()

	action = input(f'\n{currentDir}>').strip()
	if action == 'change' or action == 'cd':
		print()
		changeDirectory()

	elif action == 'show' or action == 'ls':
		detailed = input('\nShow details?: ')
		showFiles(currentDir, detailed)
	
	elif action == 'clean' or action == 'cltmp':
		tempCleaner(TEMP)
	
	elif action == 'run':
		showFiles(currentDir)
		fileToOpen = input('\nWhich file you want to open: ')

		if fileToOpen == 'help' or fileToOpen == '-h':
			help()
		elif fileToOpen == 'none':
			continue
		else:
			try:
				os.startfile(f'{currentDir}\{fileToOpen}')
			except PermissionError:
				print('\n[You do not have any permission to get into this directory.\n')

	elif action == 'help' or action == '-h':
		help()
