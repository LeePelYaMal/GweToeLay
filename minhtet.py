import os,time,platform
os.system('clear')
print('[•] Checking Updates...')
os.system('git pull')
green = ('\033[1;32m')
white = ('\033[1;37m')
red = ('\033[1;31m')

print('<------------------------------------>')
bit = platform.architecture()[0]
if bit=='32bit':
    print(f'{red}[•] Join Over Facebook Group {white}')
    os.system('xdg-open https://www.facebook.com/groups/1422983921406005/?ref=share//')
    time.sleep(0.05)
    import trt1
elif bit=='64bit':
    import trt64
else:
    print(f'{green}[×] Sorry System Not Support{white}')
