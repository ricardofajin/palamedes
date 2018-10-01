import nmap
import threading
from colorama import Fore, Style
from Utility import Loading

def tcp(ip,interface,folder='results'):
    nm = nmap.PortScanner()
    print('[' + Fore.GREEN + 'TCP - SCANNING' + Style.RESET_ALL + '] - ' + ip)

    try:
        param = '-sV --open -sC -T3 -e ' + interface + ' -o ' + folder + '/' + ip.replace('/', '-') + '_TCP.txt'
        the_process = threading.Thread(name='Scan TCP - Palapica 8==D', target=nm.scan(ip, '1-65535', param))
        the_process.start()

        while the_process.isAlive():
            Loading.animated()
    except Exception as e:
        e = str(e)
        e = e.replace("'", "")
        e = e.replace("\\nQUITTING!\\n", "")
        print("[" + Fore.RED + "ERROR" + Style.RESET_ALL + "]" " - " + e)
        exit()

def udp(ip,interface,folder='results'):
    nm = nmap.PortScanner()
    print('[' + Fore.BLUE + 'UDP - SCANNING' + Style.RESET_ALL + '] - ' + ip)

    try:
        param = '-sV -sC -sU -T3 --open -e ' + interface + ' -oN ' + folder + '/' + ip.replace('/', '-') + '_UDP.txt'
        the_process = threading.Thread(name='Scan TCP - Palapica 8==D', target=nm.scan(ip, '1-65535', param))
        the_process.start()

        while the_process.isAlive():
            Loading.animated()
    except nmap.nmap.PortScannerError as e:
        e = str(e)
        e = e.replace("'", "")
        e = e.replace("\\nQUITTING!\\n", "")
        print("[" + Fore.RED + "ERROR" + Style.RESET_ALL + "]" " - " + e)
        exit()
