from os import system
from time import sleep
import aab, V1, V2



Yes = ['Yes', 'yes', 'Ya', 'ya', 'Y', 'y']
No = ['No', 'no', 'N', 'n']
		

			
def kirim ():
	system ("mv -f mentah.bashrc ../../usr/etc")
	system ("cat ../../usr/etc/mentah.bashrc >> ../../usr/etc/bash.bashrc")
	system ("rm -f ../../usr/etc/mentah.bashrc")

def play():
	aab.pembatas()
	aab.profil()
	aab.pembatas()
	print ("1. Lihat Contoh")
	print ("2. Buat dan Pasang")
	print ("99. Exit")
	pilih = int(input("Masukan Angka Yang Kamu Pilih : "))
	aab.pembatas()
	if pilih == (1):
		print ("1. Figlet")
		print ("2. Cowsay")
		print ("99. Exit")
		pilih1 = int(input("Masukan Angka : "))
		aab.pembatas()
		
		if pilih1 == (1):
			V1.pilihan.figlet()
			sleep (5)
			play()
		elif pilih1 == (2):
			V2.cowsay.pilihan()
			V2.cowsay.contoh()
			sleep (5)
			play()
		else:
			abb.berakhir()
			system ("exit")

	elif pilih == (2):
		print ("1. Pasang Figlet")
		print ("2. Pasang Cowsay")
		print ("99. Exit")
		pilih2 = int(input("Mau Pasang Yang Mana ? : "))
		if pilih2 == (1):
			V1.buat_file.buat()
			sleep (2)
		elif pilih2 == (2):
			V2.cowsay.pilihan()
			V2.cowsay.buat()
			sleep (2)
			
		send = str(input("Apakah Anda Mau Memasang File [Y/n] : "))
		if send in Yes:
			aab.berjalan()
			sleep (1)
			kirim()
		else:
			play()
	else:
		system ("exit")
			
			
				
	
	
	
	
	
	
	
	
play()