from colorama import Fore 
import time 
import sys 
color_font_red=Fore.RED 
color_font_green=Fore.GREEN 
def error_msg(txt):
    for ch in txt:
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write(f'{color_font_red}{ch}')
    else:
        print(f'{color_font_green}')
        
while True:
    try:
        print(color_font_green)
        timer=int(input('Enter the number of seconds you want to count:'))
        if timer>60 or timer<0:
            error_msg('Error,we could not process your request, pls try again\n')
        else:
            if timer<10 and timer>1:
                print(f'00:0{timer}')
                time.sleep(1)
            elif timer>10 and timer<60:
                print(f'00:{timer}')
                time.sleep(1)
            while timer>0:
                timer-=1 
                if timer>=1 and timer<=9 or timer==0:
                    print(f'00:0{timer}')
                    time.sleep(1)
                elif timer>=10:
                    print(f'00:{timer}')
                    time.sleep(1)
    except ValueError:
        error_msg('Error,not a  numerical value pls try again\n')
