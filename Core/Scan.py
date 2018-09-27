import nmap
from colorama import Fore, Style

def tcp(IP):
    nm = nmap.PortScanner()
    print(Fore.GREEN + 'Scaning ' + IP + Style.RESET_ALL)
    # Tenho fe que a pasta estara la :D
    #aguardando checkDir() - Utility
    nm.scan(IP, '1-65535', '-sV -sC -T3 -o /results/' + IP.replace('/','-') + '.txt')

    print(nm.scaninfo())
    print(nm.csv())
    return

def udp(IP):
    print('nmap UDP!')
    print('IP: ' + IP)
    # TODO deixa pra dps u.u
    return