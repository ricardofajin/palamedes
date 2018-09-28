import os
from colorama import Fore, Style

def mkdir(dir):
    try:
        os.mkdir(dir)
    except Exception as e:
        print('[' + Fore.RED + 'ERRO' + Style.RESET_ALL + '] - ' + str(e))
