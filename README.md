# Palamedes
- *A preguiça, o ócio e a recreação revigoravam as energias para a batalha.*

Script em python para agilizar testes de segmentação. Para execução do Script, será necessário informar os escopos de testes(em formato de VLAN ex: 192.168.0.0/24, 10.0.0.0/23, 172.16.0.0/16, ...) e a interface de rede. 

Ex:

- palamedes.py -e eth0 /tmp/scope1.txt /tmp/scope2.txt
- palamedes.py -p /tmp/folder_results -e eth0 /tmp/scope1.txt /tmp/scope2.txt

### Usage 
```
        ____        __                         __         
       / __ \____ _/ /___ _____ ___  ___  ____/ /__  _____
      / /_/ / __ `/ / __ `/ __ `__ \/ _ \/ __  / _ \/ ___/
     / ____/ /_/ / / /_/ / / / / / /  __/ /_/ /  __(__  ) 
    /_/    \__,_/_/\__,_/_/ /_/ /_/\___/\__,_/\___/____/  

    "- A preguiça, o ócio e a recreação revigoravam as energias para a batalha."
                                                      
Palamedes v0.3 - Teste segmentacao
usage: palamedes.py [-h] [-p PATH] [-e INTERFACE] scopeFiles [scopeFiles ...]

positional arguments:
  scopeFiles            Set the scope files

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Set the path to save the results (Default= results)
  -e INTERFACE, --interface INTERFACE
                        Set the network interface
```

## Dependencias
- python-nmap

```
pip install python-nmap
```

Download - [python-nmap-0.6.1.tar.gz](https://xael.org/pages/python-nmap-0.6.1.tar.gz)


```
tar xvzf python-nmap-0.6.1.tar.gz
cd python-nmap-0.6.1
python setup.py install
```

* Referência -  https://xael.org/pages/python-nmap-en.html
