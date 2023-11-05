from itertools import permutations 
import time 
import sys 
from colorama import Fore 
digit_length=1
def error_msg(txt):
    for n in txt:
        sys.stderr.flush()
        time.sleep(0.1)
        sys.stderr.write(f'{Fore.RED}{n}')
    else:
        reset_to_default_color=Fore.RESET 
        print(f'{reset_to_default_color}')
while True:
 try:
  repeat=int(input('how many digits do you want?:'))
  digits=[]
  if repeat==1:
      pass 
  else:
   for n in range(repeat):
      digit=int(input('digit:'))
      time.sleep(0.2)
      strdigit=str(digit)
      if len(strdigit)>1:
          error_msg(txt='Error,digit should"nt be more than 1 character long\n')
      else:
          digits.append(strdigit)
   else:
      print('\n all orderings of your given digits:\n')
      combinations=permutations(digits)
      for num in combinations:
          sys.stderr.flush()
          time.sleep(0.5)
          print(f'{"".join(num)}\n')
 except ValueError:
     error_msg(txt='Error not a numeric value')