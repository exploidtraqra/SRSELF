import os
server =
time = int(input('enter time : '))
for i in range(time):
        print '\033[31m'
        XD ="curl http://"+server+".co.za/pesan.text"
        os.system(XD)
