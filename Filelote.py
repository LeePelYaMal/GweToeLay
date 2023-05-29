import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('clear')

bit = platform.architecture()[0]
if bit == '64bit':
    import file64
elif bit == '32bit': 
    import Main