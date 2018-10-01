import sys, time
from colorama import Fore, Style

def animated():
    chars = "/—\|"
    loading = '[' + Fore.YELLOW + 'LOADING...' + Style.RESET_ALL
    for char in chars:
        sys.stdout.write('\r'+ loading +char+' ]')
        time.sleep(.1)
        sys.stdout.flush()