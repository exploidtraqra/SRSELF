import os
import profil
import main
f = open("pesan.txt",'w')
send = input(' message: ')
f.write(profil.name)
f.write(send)
f.close()
Wokez="curl -T pesan.txt http://"+server+".co.za") 
os.system(Wokez)
os.system('python2 send.py')
