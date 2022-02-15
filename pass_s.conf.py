#-----------------------------------------
# scripted by samay 
# design credits : Vaimpier ritik 
# Python3 database expert 
# Vaim - Samay Projects 
# Copy This script doesn't  makes you coder 
# idea-maker :- virusman ,acezinmaker ! 
#------------------------------------------

#------------------------imports 

from os import system
from time import sleep
import sys
import random
#-----------------------------Colors

r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"


#---------------------------------------------------


logo = """\033[1;37m

\033[1;37m[!] \033[1;31mThis is use for JIDs generator, You can Unlimitedly Edit !!! BYE :_)
\033[1;37m
┌-=============================   -   
=      \033[1;31m . ┌──────── \033[1;37mVaim-Samay    -   
=  \033[1;31m .┌───  \033[1;37mB-Hat Samay            -   \033[34m[✔]     https://github.com/samay825        [✔]
\033[1;37m=    JID Generator - Pro          -   \033[34m[✔]            Version 2.0                 [✔]
\033[1;37m= \033[1;31m . └──── \033[1;37mBY Samay               -   \033[91m[X] Please Don't Use For illegal Activity  [X]
\033[1;37m= \033[1;31m .     └─── \033[1;37mVERSION 2.0         -
\033[1;37m└-=============================   -

\033[1;31m    
Disclaimer: \033[1;32mthis tool is designed for Prank
	    testing in an authorized simulated cyberattack
	    Attacking targets without prior mutual consent
            is illegal!                                                               
\033[1;37m                                    
\033[97m """

def banner():
    print(logo)

class Vrushabh:
    def __init__(self,user):
        system('clear')
        banner()
        self.user = user
class Samay(Vrushabh):
    def __init__(self, user,samay):
        super().__init__(user)
        system('clear')
        print('\n')
        self.samay = samay
    def samay_encryption(self):
        while True:
            if self.user==self.samay:
                print("\n")
                print(r+"└─"+w+"\033[1;37mPassword Correct !"+r)
		sleep(2.9)
                print("\n")
                system('clear')
                break
            elif self.samay not in self.user:
                print("\n")
                print(r+"└─"+w+"\033[1;37mPassword Incorrect ! "+r)
                print("\n")
                sleep(3.0)
                system('clear')
                system('python3 pass_s.conf.py')
                break
        
            
banner()

_user = input(r+"└─"+w+"\033[1;37mPress Enter >>>>>>  "+r)
print('\n')
samay1 = Vrushabh(_user)
_user_ = input(r+"└─"+w+"\033[1;37mEnter The Password : "+r)
print('\n')
list_pass = [
    'virus-vaim',
    'virus-ace'
]
samay_user = random.choice(list_pass)
samay2 = Samay(_user_, samay_user)
samay2.samay_encryption()

