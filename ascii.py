from rich.console import Console
from rich.theme import Theme
import time 
import os
custom_theme=Theme({"error":"bold red"})
console=Console(theme=custom_theme)
def error_msg(txt):
   for ch in txt:
        console.print(ch,style="error",end='')
        time.sleep(0.1)
try:
     with console.screen():
        timer=int(console.input("[green] [i]enter the number of seconds you would like to count:"))
        if timer>60 or timer<0:
            error_msg('Error,we could not process your request, pls try again\n')
        else:
            if timer<10 and timer>1:
                console.print(f'00:0{timer}',justify="center")
                time.sleep(1)
                os.system("cls")
            elif timer>10 and timer<60:
                console.print(f'00:{timer}',justify="center")
                time.sleep(1)
                os.system("cls")
            while timer>0:
                timer-=1 
                if timer>=1 and timer<=9 or timer==0:
                    console.print(f'00:0{timer}',justify="center")
                    time.sleep(1)
                    os.system("cls")
                elif timer>=10:
                   console.print(f'00:{timer}',justify="center")
                   time.sleep(1)
                   os.system("cls")
except ValueError:
        error_msg('Error,not a  numerical value pls try again\n')
