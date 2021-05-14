import os

time= int(input('enter time : '))
for i in range(time):
        print '\033[31m'
        os.system('curl http://ratia.co.za/pesan.txt')
