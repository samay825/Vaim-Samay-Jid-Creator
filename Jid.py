#-----------------------------------------
# scripted by samay 
# design credits : Vaimpier ritik 
# Python3 database expert 
# Vaim - Samay Projects 
# Copy This script doesn't  makes you coder 
# idea-maker :- virusman ,acezinmaker ! 
#------------------------------------------

#-----------------------------Imports

import os
import random
import sys
from os import system
from time import sleep

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

#-----------------------Banner and  functions 

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
os.system('python3 pass_s.conf.py')

def banner():
    print(logo)

def deprint():
    print("\n")




def bye():
	os.system("clear")
	banner()
	string = """ 
	\033[1;37mDeveloper  \033[1;34m: \033[1;31mVAIM-SAMAY

	\033[1;37mGithub     \033[1;34m: \033[1;31msamay825

	\033[1;37mInstagram  \033[1;34m: \033[1;31mvaimpier_ritik

	\033[1;37mE-mail     \033[1;34m: \033[1;31mcybokhackers@gmail.com
	"""
	for letter in string:
	  sleep(0.01) 
	  sys.stdout.write(letter)
	  sys.stdout.flush()
	print("\n")


def Main_function_1_options():
    system('clear')
    banner()
    deprint()
    super_ask = input(r+"└─"+w+"\033[1;37mEnter Name to Create File: "+r)
    deprint()
    super_Ask_2 = int(input(r+"└─"+w+"\033[1;37mHow many Jids You want : "+r))
    deprint()
    super_Ask_3 = int(input(r+"└─"+w+"\033[1;37mRange : "+r))
    deprint()
    for i in range(1,super_Ask_2+1):
        with open(f'Samay_Random/{super_ask}_{i}','w') as f:
            f.write('')
            with open(f'Samay_Random/{super_ask}_{i}','a') as f:
                for i in range(1,super_Ask_3+1):
                    data_Send = '@s.whatsapp.net,'
                    data_1_Set = [1,2,3,4,5,6,7,8,9,10,11]
                    data_1_ = str(random.choice(data_1_Set))
                    data_2_ = str(random.choice(data_1_Set))
                    data_3_ = str(random.choice(data_1_Set))
                    data_4_ = str(random.choice(data_1_Set))
                    data_5_ = str(random.choice(data_1_Set))
                    data_6_ = str(random.choice(data_1_Set))
                    data_7_ = str(random.choice(data_1_Set))
                    data_8_ = str(random.choice(data_1_Set))
                    data_9_ = str(random.choice(data_1_Set))
                    data_10_ = str(random.choice(data_1_Set))
                    data_11_ = str(random.choice(data_1_Set))
                    random_num_Set_join = (data_1_+data_2_+data_3_+data_4_+data_5_+data_6_+data_7_+data_8_+data_9_+data_10_+data_11_+data_Send)
                    f.write(random_num_Set_join)
                    print(r+"└─"+w+"\033[1;37mGenerating ---> "+g+str(i)+r)
            deprint()
            print(r+" ..└─"+w+f"\033[1;37mJid Generated Successfully and Saved in "+r+"Samay_Random/"+g)
            #system('cd Samay_Random/ ')
            #system(f"ls Samay_Random | grep {super_ask}")
            
                
            
            deprint()
    for x in range(1, super_Ask_2+1):
                print(r+"└─"+w+"Your File as saved in"+r+" /Samay_Random/"+g+super_ask+str(x))
	    deprint()
            



def Main_function_2_options():
    system('clear')
    banner()
    deprint()
    super_ask = input(r+"└─"+w+"\033[1;37mEnter Name to Create File: "+r)
    deprint()
    super_Ask_2 = int(input(r+"└─"+w+"\033[1;37mHow many Jids You want : "+r))
    deprint()
    super_Ask_3 = int(input(r+"└─"+w+"\033[1;37mRange : "+r))
    deprint()
    for i in range(1,super_Ask_2+1):
        with open(f'Vaim_Sequence/{super_ask}_{i}.txt','w') as f:
            data_send_Write_file = '@s.whatsapp.net,'
            f.write('')
            with open(f'Vaim_Sequence/{super_ask}_{i}.txt','a') as g:
                for i in range(1,super_Ask_3+1):
                    g.write(f'0000'+str(i)+str(data_send_Write_file))
                    print(r+"└─"+w+f"\033[1;37mGenerating ---> {i} \n"+r)
            deprint()
            print(r+" ..└─"+w+f"\033[1;37mGenerated ---> {i} in Onefile stored in Folder Vaim_Sequence ----> {super_Ask_2} Successfully !"+g)
            system(f"ls Vaim_Sequence | grep {super_ask}")
            deprint()





#-----------------------------Main Object Oriented Programming --!


class Banner_Main:
    __main__ = '__front_client_input'
    def __init__(self):
        system('clear')
        banner()
class Main_interface_frame(Banner_Main):
    __main__ = '__second_client_input'
    def __init__(self):
        super().__init__()
    def __Main_Interface_Options_Frame__(self):
        super().__init__()
        print(r+"└─"+w+"\033[1;37m[ 1 ] Random Digits Jid : ")
        print(r+"└─"+w+"\033[1;37m[ 2 ] Sequence Digits Jid : ")
        print(r+"└─"+w+"\033[1;37m[ 3 ] About me : ")
        print(r+"└─"+w+"\033[1;37m[ 4 ] Update : ")
        print(r+"└─"+w+"\033[1;37m[ 5 ] Exit : ")
class Options_Interact_Function:
    deprint()
    def options_choose_func(self):
        deprint()
        self.user_program_input = int(input(r+"└─"+w+"\033[1;37mEnter Desire Option: "+r))
        if self.user_program_input==1:
            Main_function_1_options()
        elif self.user_program_input==2:
            Main_function_2_options()
        elif self.user_program_input==3:
            bye()
            deprint()
            samay_main_return = input(r+"..└─"+w+"\033[1;37mReturn or exit [ y / n ]: "+r)
            if samay_main_return=="y" or samay_main_return=="Y":
                os.system('python3 Jid.py')
            else:
                sys.exit()
        elif self.user_program_input==4:
            system('bash update.sh')
            
        elif self.user_program_input==5:
            sys.exit()
        





samay1 = Banner_Main()
samay2 = Main_interface_frame()
samay2.__Main_Interface_Options_Frame__()
samay3 = Options_Interact_Function()
samay3.options_choose_func()




  
