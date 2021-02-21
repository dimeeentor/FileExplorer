# File Explorer v.1
import os

# Variables
TEMP = os.environ.get('TEMP')
SYSTEM_ROOT = os.environ.get('SYSTEMROOT')
USER_PROFILE = os.environ.get('USERPROFILE')
PROGRAM_FILES = os.environ.get('PROGRAMFILES')
PROGRAM_FILES_X86 = os.environ.get('PROGRAMFILES(X86)')

# Function
def tempCleaner(path):
	for file in os.listdir(path):
		try:
			os.remove(f'{path}\{file}')
			os.rmdir(f'{path}\{file}')
			print(f'Deleted: {path}\{file}')
		except PermissionError:
			print(f'[!] Cannot delete: {path}\{file}')
			continue

def showFiles(path, detailed = False):
	if detailed or detailed == 'T' or detailed == 't':
		for root, dirs, files in os.walk(path, topdown = True):
			print(f'[+] Root: {root}\nDirectories: {dirs}\nFiles: {files}\n\n')
			
	else:
		for file in os.listdir(currentDir):
			print(f'[+] {file}')

while True:
	currentDir = os.getcwd()
	action = input(f'\nYou are in this directory: \'{currentDir}\'\n[!] Choose an action:\n[+] 1) Change directory.\n[+] 2) Show files in this directory.\n: ')

	if action == '1' or action == 'change':
		print(f'\n[!] Some shortcuts:\n1) Windows (W, w) - \'{SYSTEM_ROOT}\'\n2) User Folder (UF, uf) - \'{USER_PROFILE}\'\n3) Program Files (PF, pf) - {PROGRAM_FILES}\n4) Program Files (x86) (PF86, pf86) - {PROGRAM_FILES_X86}\n')

		changeDirectory = input('[?] Enter the new directory: ')
		if changeDirectory == 'Windows' or changeDirectory == 'W' or changeDirectory == 'w':
			currentDir = os.chdir(SYSTEM_ROOT)
		elif changeDirectory == 'User Folder' or changeDirectory == 'UF' or changeDirectory == 'uf':
			currentDir = os.chdir(USER_PROFILE)
		elif changeDirectory == 'Program Files' or changeDirectory == 'PF' or 'pf':
			currentDir = os.chdir(PROGRAM_FILES)
		elif changeDirectory == 'Program Files (x86)' or changeDirectory == 'PF86' or changeDirectory == 'pf86':
			currentDir = os.chdir(PROGRAM_FILES_X86)
		else:
			currentDir = os.chdir(changeDirectory)
			
		print('\n[!] Directory has changed successfully...')

	elif action == '2' or action == 'show':
		detailed = input('\n[!] Show details?\nTrue or False.\nDefault is \'FALSE\'.\n: ')

		showFiles(currentDir, detailed)