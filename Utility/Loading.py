import sys, time

def animated():
    chars = "/—\|"
    for char in chars:
        sys.stdout.write('\r'+'loading...'+char)
        time.sleep(.1)
        sys.stdout.flush()