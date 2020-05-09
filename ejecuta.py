import subprocess
u="gerardo"
p="12345"
username = input("Enter username:")
if u == username:
	password= input("Enter password:")
	if p == password:
		subprocess.Popen('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
	else: print("eliminado")
else: print("eliminado")