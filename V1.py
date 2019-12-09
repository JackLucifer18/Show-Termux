import aab
from time import sleep
from os import system 

class pilihan(): 
	def figlet():
		aab.pembatas()
		print ("")
		print ("1. Banner			10. Slant")
		print ("2. Block			11. Shadow")
		print ("3. Bubble			12. Small")
		print ("4. Digital			13. Smscript")
		print ("5. Ivrit			14. Smshadow")
		print ("6. lean				15. Smslant")
		print ("7. mini				16. Standard")
		print ("8. Mnemonic			17. Term")
		print ("9. Script			99. Exit / Kembali")
		print ("")
		pilih1 = int(input("Pilih Gaya Font : "))
		aab.pembatas ()
		if pilih1 == (1):
			system("figlet -f banner.flf 'Hello Jack' | lolcat")
		elif pilih1 == (2):
			system ("figlet -f block.flf 'Hello Jack' | lolcat")
		elif pilih1 == (3):
			system("figlet -f bubble.flf 'Hello Jack' | lolcat")
		elif pilih1 == (4):
			system("figlet -f digital.flf 'Hello Jack' | lolcat")
		elif pilih1 == (5):
			system("figlet -f ivrit.flf 'Hello Jack' | lolcat")
		elif pilih1 == (6):
			system("figlet -f lean.flf 'Hello Jack' | lolcat")
		elif pilih1 == (7):
			system("figlet -f mini.flf 'Hello Jack' | lolcat")
		elif pilih1 == (8):
			system("figlet -f mnemonic.flf 'Hello Jack' | lolcat")
		elif pilih1 == (9):
			system("figlet -f script.flf 'Hello Jack' | lolcat")
		elif pilih1 == (10):
			system("figlet -f slant.flf 'Hello Jack' | lolcat")
		elif pilih1 == (11):
			system("figlet -f shadow.flf 'Hello Jack' | lolcat ")
		elif pilih1 == (12):
			system("figlet -f small.flf 'Hello Jack' | lolcat")
		elif pilih1 == (13):
			system("figlet -f smscript.flf 'Hello  jack' | lolcat")
		elif pilih1 == (14):
			system("figlet -f smshadow.flf 'Hello Jack' | lolcat")
		elif pilih1 == (15):
			system("figlet -f smslant.flf 'Hello Jack' | lolcat")
		elif pilih1 == (16):
			system("figlet -f standard.flf 'Hello Jack' | lolcat")
		elif pilih1 == (17):
			system ("figlet -f term.flf 'Hello Jack' | lolcat")
		else :
			print ("PROSES TERHENTI")
			sleep (2)
			system ("exit")


class buat_file():
	def buat():
		with open("mentah.bashrc", 'a') as f:
			aab.pembatas()
			print ("")
			print ("1. Banner			10. Slant")
			print ("2. Block			11. Shadow")
			print ("3. Bubble			12. Small")
			print ("4. Digital			13. Smscript")
			print ("5. Ivrit			14. Smshadow")
			print ("6. lean				15. Smslant")
			print ("7. mini				16. Standard")
			print ("8. Mnemonic			17. Term")
			print ("9. Script			99. Exit / Kembali")
			print ("")
			pilih1 = int(input("Pilih Gaya Font : "))
			aab.pembatas ()
			if pilih1 == (1):
				f.write("\nfiglet -f banner.flf 'Aldi Fortuna 18'  | lolcat")
			elif pilih1 == (2):
				f.write ("\nfiglet -f block.flf 'Aldi Fortuna 18' | lolcat")
			elif pilih1 == (3):
				f.write("\nfiglet -f bubble.flf 'Aldi Fortuna 18' | lolcat")
			elif pilih1 == (4):
				f.write("\nfiglet -f digital.flf 'Aldi Fortuna 18' | lolcat")
			elif pilih1 == (5):
				f.write("\nfiglet -f ivrit.flf 'Aldi Fortuna 18' | lolcat")
			elif pilih1 == (6):
				f.write("\nfiglet -f lean.flf 'Aldi Fortuna 18' | lolcat")
			elif pilih1 == (7):
				f.write("\nfiglet -f mini.flf 'Aldi Fortuna 18'  | lolcat")
			elif pilih1 == (8):
				f.write("\nfiglet -f mnemonic.flf 'Hello Jack' | lolcat")
			elif pilih1 == (9):
				f.write("\nfiglet -f script.flf 'Hello Jack' | lolcat")
			elif pilih1 == (10):
				f.write("\nfiglet -f slant.flf 'Hello Jack' | lolcat ")
			elif pilih1 == (11):
				f.write("\nfiglet -f shadow.flf 'Hello Jack' | lolcat")
			elif pilih1 == (12):
				f.write("\nfiglet -f small.flf 'Hello Jack' | lolcat")
			elif pilih1 == (13):
				f.write("\nfiglet -f smscript.flf 'Hello  jack' | lolcat")
			elif pilih1 == (14):
				f.write("\nfiglet -f smshadow.flf 'Hello Jack' | lolcat")
			elif pilih1 == (15):
				f.write("\nfiglet -f smslant.flf 'Hello Jack' | lolcat")
			elif pilih1 == (16):
				f.write("\nfiglet -f standard.flf 'Hello Jack' | lolcat")
			elif pilih1 == (17):
				f.write("\nfiglet -f term.flf 'Hello Jack' | lolcat")
			else :
				print ("PROSES TERHENTI")
				sleep (2)
				system ("exit")
			f.close()	