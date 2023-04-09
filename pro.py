import os, sys, platform,time
try:
    import requests
except:
    os.system('pip install requests')

bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('git pull')
    import pro64
elif bit == '32bit':
    os.system('clear')
    os.system('git pull')
    import pro32
