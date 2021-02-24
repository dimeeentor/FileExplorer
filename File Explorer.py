# File Explorer v.1.1
import os
from pathlib import Path
from sys import exit


# Variables
TEMP = os.environ.get('TEMP')
APP_DATA = os.environ.get('APPDATA')
SYSTEM_ROOT = os.environ.get('SYSTEMROOT')
USER_PROFILE = os.environ.get('USERPROFILE')
PUBLIC = os.environ.get('PUBLIC')
PROGRAM_FILES = os.environ.get('PROGRAMFILES')
PROGRAM_FILES_X86 = os.environ.get('PROGRAMFILES(X86)')
PROGRAM_DATA = os.environ.get('PROGRAMDATA')
COMMON_PROGRAM_FILES = os.environ.get('COMMONPROGRAMFILES')
COMMON_PROGRAM_FILES_X86 = os.environ.get('COMMONPROGRAMFILES(X86)')
ONE_DRIVE = os.environ.get('ONEDRIVE')
FILE_DIRECTORY = os.getcwd()

# Functions
def help(module):
	if module == 'cd':
		paths = ['Windows (W, w)', 'User Folder (UF, uf)', 'Public (PUBL, publ)','Program Files (PF, pf)', 'Program Files (x86) (PF86, pf86)', 'App Data (AD, ad)', 'Common Program Files (CPF, cpf)', 'Common Program Files (x86) (CPF86, cpf86)', 'Program Data (PD, pd)', 'One Drive (OD, od)', 'File Directory (FD, fd)']

		systemPaths = [SYSTEM_ROOT, USER_PROFILE, PUBLIC, PROGRAM_FILES, PROGRAM_FILES_X86, APP_DATA, COMMON_PROGRAM_FILES, COMMON_PROGRAM_FILES_X86, PROGRAM_DATA, ONE_DRIVE, FILE_DIRECTORY]

		for count, path in enumerate(paths):
			print(f'{count + 1}) {path} - \'{systemPaths[count]}\';')

	elif module == 'run':
		print('\nIf you want to execute a file, type the name of file with the extension.\nIf you want to exit this menu, type \'-\'.\nIf you you need to see files again type \'show\' or \'ls\'.')

	elif module == 'folder':
		print(f'\nType the name of folder.\nFolder will be created in this directory: \'{currentDir}\'.')

	else:
		shortcuts = ['Change directory (change, cd)', 'Show files in this directory (show, ls)', 'Execute a specific file (run)', 'Clean \'TEMP\' folder (clean, cltmp)', 'Make a folder (mkdir)', 'Exit (exit)']
		print('Help Shortcuts:')

		for count, shortcut in enumerate(shortcuts):
			print(f'{count + 1}) {shortcut};')

def checkExtension(file):
	if Path(file).suffix == '':
		return True
	else:
		return False

def tempCleaner(path):
	for file in os.listdir(path):
		try:
			os.remove(f'{path}\{file}')
			os.removedirs(f'{path}\{file}')
			print(f'Deleted: {path}\{file}')

		except PermissionError:
			print(f'[!] Cannot delete: {path}\{file}')
			continue
		except FileNotFoundError:
			print(f'[!] Cannot delete: {path}\{file}')
			continue

def showFiles(path, detailed = False):
	if detailed or detailed == 'T' or detailed == 't':
		for root, dirs, files in os.walk(path, topdown = True):
			print(f'Root: {root}\nDirectories: {dirs}\nFiles: {files}\n')
		
	else:
		for file in os.listdir(currentDir):
			if checkExtension(file):
				print(f'{file} - \'Folder\'')
			else:
				print(f'{file} - \'File\'')

def changeDirectory():
	while True:
		try:
			changeDirectory = input('\nEnter the new directory: ').strip()

			if changeDirectory == 'help' or changeDirectory == '-h':
				help('cd')
				continue

			elif changeDirectory == 'Windows' or changeDirectory == 'W' or changeDirectory == 'w':
				os.chdir(SYSTEM_ROOT)

			elif changeDirectory == 'User Folder' or changeDirectory == 'UF' or changeDirectory == 'uf':
				os.chdir(USER_PROFILE)

			elif changeDirectory == 'Program Files' or changeDirectory == 'PF' or changeDirectory == 'pf':
				os.chdir(PROGRAM_FILES)

			elif changeDirectory == 'Program Files (x86)' or changeDirectory == 'PF86' or changeDirectory == 'pf86':
				os.chdir(PROGRAM_FILES_X86)

			elif changeDirectory == 'App Data' or changeDirectory == 'AD' or changeDirectory == 'ad':
				os.chdir(APP_DATA)

			elif changeDirectory == 'Program Data' or changeDirectory == 'PD' or changeDirectory == 'pd':
				os.chdir(PROGRAM_DATA)

			elif changeDirectory == 'Common Program Files' or changeDirectory == 'CPF' or changeDirectory == 'cpf':
				os.chdir(COMMON_PROGRAM_FILES)

			elif changeDirectory == 'Common Program Files (x86)' or changeDirectory == 'CPF86' or changeDirectory == 'cpf86':
				os.chdir(COMMON_PROGRAM_FILES_X86)

			elif changeDirectory == 'File Directory' or changeDirectory == 'FD' or changeDirectory == 'fd':
				os.chdir(CURRENT_DIRECTORY)

			elif changeDirectory == '-':
				break

			else:
				os.chdir(changeDirectory)

			print('Directory has changed successfully...')	
			break

		except FileNotFoundError:
			print('\nSpecified directory does not exist.\nCheck if the directory is correct.\n')
			continue
		except PermissionError:
			print('\nYou do not have any permission to get into this directory.\n')
			continue
		except NotADirectoryError:
			print('\nMust be a directory.\n')
			continue
		except OSError:
			print('\nSpecified directory does not exist.\nCheck if the directory is correct.\n')
			continue

def runFile():
	showFiles(currentDir)

	while True:
		fileToOpen = input('\nWhich file you want to open?: ')

		if fileToOpen == 'help' or fileToOpen == '-h':
			help('run')

		elif fileToOpen == 'show' or fileToOpen == 'ls':
			showFiles(currentDir)
			continue

		elif fileToOpen == '-':
			break

		else:
			if checkExtension(fileToOpen):
				try:
					os.startfile(f'{currentDir}\{fileToOpen}')
					break

				except PermissionError:
					print('\nYou do not have any permission to get into this directory.\n')
					continue

				except FileNotFoundError:
					print('\nThis file does not exist.\n')
					continue

			else:
				print('You can \'EXECUTE\' only \'FILES\'.')

def makeDirectory(folder, path):
	os.mkdir(folder)
	print(f'Folder: {folder} was successfully created.\nIn this directory: \'{path}\'.')

while True:
	currentDir = os.getcwd()
	action = input(f'\n{currentDir}>').strip()

	if action == 'change' or action == 'cd':
		changeDirectory()

	elif action == 'show' or action == 'ls':
		detailed = input('\nShow details?: ')
		showFiles(currentDir, detailed)

	elif action == 'clean' or action == 'cltmp':
		while True:
			agree = input('Are you sure to continue? (Yes, No): ')

			if agree == 'Yes' or agree == 'yes' or agree == 'Y' or agree == 'y':
				tempCleaner(TEMP)
				break

			elif agree == 'No' or agree == 'no' or agree == 'N' or agree == 'n':
				break

			else:
				continue

	elif action == 'run':
		runFile()

	elif action == 'help' or action == '-h':
		help(None)

	elif action == 'mkdir':
		folder = input('Enter the name of folder: ')

		if folder == 'help' or folder == '-h':
			help('folder')
			
		else:
			makeDirectory(folder, currentDir)

	elif action == 'exit':
		exit()

	else:
		print(f'\nUnknown command: \'{action}\'')
