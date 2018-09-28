import nmap
import threading
from colorama import Fore, Style
from Utility import Check, Make, Loading

def tcp(ip,folder,interface):
    nm = nmap.PortScanner()
    print('[' + Fore.GREEN + 'TCP - SCANNING' + Style.RESET_ALL + '] - ' + ip)

    try:
        Check.dir(folder)
    except:
        Make.dir('results')

    the_process = threading.Thread(name='Scan TCP - Palapica 8==D', target=nm.scan(ip, '1-65535', '-sV --open -sC -T3 -e ' + interface + ' -oN ' + folder + '/' + ip.replace('/', '-') + 'TCP_.txt'))
    the_process.start()

    while the_process.isAlive():
        Loading.animated()

def udp(ip,interface,folder='results'):
    nm = nmap.PortScanner()
    print('[' + Fore.BLUE + 'UDP - SCANNING' + Style.RESET_ALL + '] - ' + IP)

    try:
        Check.dir(folder)
    except:
        Make.dir('results')

    try:

        the_process = threading.Thread(name='Scan TCP - Palapica 8==D', target=nm.scan(ip, '1-65535', '-sV -sC -sU -T3 --open -e ' + interface + ' -oN ' + folder + '/' + ip.replace('/', '-') + 'UDP_.txt'))
        the_process.start()

        while the_process.isAlive():
            Loading.animated()
    except nmap.nmap.PortScannerError as e:
        e = str(e)
        e = e.replace("'", "")
        e = e.replace("\\nQUITTING!\\n", "")
        print("[" + Fore.RED + "ERROR" + Style.RESET_ALL + "]" " - " + e)
        exit()
