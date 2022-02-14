#-----------------------------------------
# scripted by samay 
# design credits : Vaimpier ritik 
# Python3 database expert 
# Vaim - Samay Projects 
# Copy This script doesn't  makes you coder 
# idea-maker :- virusman ,acezinmaker ! 
#------------------------------------------




#----------------------imports
from os import system
from time import sleep 
import os
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
#-----------------------logo and space func



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

#--------------------Main object Oriented Programming ! 
banner()

class Main:
    def __init__(self,user_input):
        system('clear')
        banner()
        self.user_input = user_input
    def samay_confirm(self):
        if self.user_input==self.confirm_password:
            print(r+"└─"+w+"\033[1;37mPassword Correct !  "+r)
            sleep(3.0)
            pass
        else:
            print(r+"└─"+w+"\033[1;37mPassword Incorrect !  "+r)
            sleep(3.9)
            sys.exit()
print("\n")
user_input = input(r+"└─"+w+"\033[1;37mEnter The Password : "+r)
print("\n")
samay = Main(user_input)
list_pass = [
    'virus_Vaim',
    'virus_Ace'
]
samay.confirm_password = random.choice(list_pass)
samay.samay_confirm()




        





    

        


