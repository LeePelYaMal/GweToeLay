import os,platform
os.system('xdg-open https://www.facebook.com/groups/1422983921406005/?ref=share')
os.system('pip uninstall requests')
os.system('pip install requests')
BXI=platform.architecture()[0]
if BXI=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif BXI=="64bit":
    __import__("Proof")
