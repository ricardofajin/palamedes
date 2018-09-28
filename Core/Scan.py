import nmap
from colorama import Fore, Style
from Utility import Check, Make

def tcp(IP,Folder,Interface):
    nm = nmap.PortScanner()
    print(Fore.GREEN + 'Scaning ' + IP + Style.RESET_ALL)

    try:
        Check.dir(Folder)
    except:
        Make.dir('results')
        Folder = 'results'

    nm.scan(IP, '1-65535', '-sV --open -sC -T3 -e ' + Interface + ' -oN ' + Folder + '/' + IP.replace('/', '-') + 'TCP_.txt')


def udp(IP,Folder,Interface):
    nm = nmap.PortScanner()
    print(Fore.GREEN + 'Scaning ' + IP + Style.RESET_ALL)

    try:
        Check.dir(Folder)
    except:
        Make.dir('results')
        Folder = 'results'

    try:
        nm.scan(IP, '1-65535', '-sV -sC -sU -T3 --open -e ' + Interface + ' -oN ' + Folder + '/' + IP.replace('/', '-') + 'UDP_.txt')
    except nmap.nmap.PortScannerError as e:
        e = str(e)
        e = e.replace("'", "")
        e = e.replace("\\nQUITTING!\\n", "")
        print("[" + Fore.RED + "ERROR" + Style.RESET_ALL + "]" " - " + e)
        exit()
