import os
from colorama import Fore, Style

def dir(dir):
    try:
        os.mkdir(dir)
    except Exception as e:
        print('[' + Fore.RED + 'ERRO' + Style.RESET_ALL + '] - ' + str(e))

# TODO: Problema em criar arquivos com espaço ex: "folder\ espace" ele n�o entende :( #TemQueVerIssoAe ...