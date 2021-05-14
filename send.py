import os
import profil
f = open("pesan.txt",'w')
send = raw_input('isi pesan: ')
f.write(profil.name)
f.write(send)
f.close()
os.system('curl -T pesan.txt http://ratia.co.za')
os.system('python2 send.py')
