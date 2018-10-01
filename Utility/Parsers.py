from argparse import ArgumentParser

def getArgs():
    parser = ArgumentParser("palamedes.py")
    parser.add_argument("scopeFiles", nargs='+', help='Set the scope files')
    parser.add_argument("-p", "--path", default='results', help='Set the path to save the results (Default= results)')
    parser.add_argument("-e", "--interface", help='Set the network interface')
    return parser.parse_args()


def txtfiletoName(fileName):
    if '.txt' in fileName:
        name = fileName.split('.txt')[0]
        return name
    else:
        return fileName
