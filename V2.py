from os  import system
import aab


class cowsay ():
	def  pilihan():
		aab.pembatas()
		print ("1. Beavis.zen			16. Head-in		31. Skeleton")
		print ("2. Bong				17. HelloKitty		32. Stegosaurus")
		print ("3. Bud-frogs			18. Kiss		33. Stimpy")
		print ("4. Bunny			19. Kitty		34. Three-Eyes")
		print ("5. Cheese			20. Koala		35. Turkey")
		print ("6. Cower			21. Kosh		36. Turtle")
		print ("7. Daemon			22. Luke-Koala		37. Tux")
		print ("8. Default			23. Mech-and-Cow	38. Vader-Koala")
		print ("9. Dragon-and-Cow		24. Meow		39. Vader")
		print ("10. Dragon			25. Milk		40. WWW")
		print ("11. Elephant-in-Snake		26. Moofasa")
		print ("12. Elephant			27. Moose")
		print ("13. Eyes			28. Multilated")
		print ("14. Flaming-Sheep		29. Ren")
		print ("15. Ghost-Busters		30. Sheep")
		
	def contoh ():
		aab.pembatas()
		pilih = int (input("Contoh Cowsay Yang Akan Anda Pilih : "))
		if pilih == (1):
			system ("cowsay -f beavis.zen.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (2):
			system ("cowsay -f bong.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (3):
			system ("cowsay -f bud-frogs.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (4):
			system ("cowsay -f bunny.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (5):
			system ("cowsay -f cheese.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (6):
			system ("cowsay -f cower.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (7):
			system ("cowsay -f daemon.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (8):
			system ("cowsay -f default.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (9):
			system ("cowsay -f dragon-and-cow.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (10):
			system ("cowsay -f dragon.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (11):
			system ("cowsay -f elephant-in-snike.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (12):
			system ("cowsay -f elephant.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (13):
			system ("cowsay -f eyes.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (14):
			system ("cowsay -f flaming-sheep.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (15):
			system ("cowsay -f ghostbusters.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (16):
			system ("cowsay -f head-in.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (17):
			system ("cowsay -f hellokitty.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (18):
			system ("cowsay -f kiss.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (19):
			system ("cowsay -f kitty.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (20):
			system ("cowsay -f koala.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (21):
			system ("cowsay -f kosh.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (22):
			system ("cowsay -f luke-koala.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (23):
			system ("cowsay -f mech-and-cow 'Jack Lucifer18' | lolcat")
		elif pilih == (24):
			system ("cowsay -f meow.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (25):
			system ("cowsay -f milk.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (26):
			system ("cowsay -f moofasa.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (27):
			system ("cowsay -f moose.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (28):
			system ("cowsay -f mutilated.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (29):
			system ("cowsay -f ren.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (30):
			system ("cowsay -f sheep.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (31):
			system ("cowsay -f skeleton.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (32):
			system ("cowsay -f stegosaurus.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (33):
			system ("cowsay -f stimpy.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (34):
			system ("cowsay -f three-eyes.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (35):
			system ("cowsay -f turkey.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (36):
			system ("cowsay -f turtle.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (37):
			system ("cowsay -f tux.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (38):
			system ("cowsay -f vader-koala.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (39):
			system ("cowsay -f vader.cow 'Jack Lucifer18' | lolcat")
		elif pilih == (40):
			system ("cowsay -f www.cow 'Jack Lucifer18' | lolcat")
		else :
			system ("exit")
		
		
	def buat():
		aab.pembatas()
		pilih = int (input("Cowsay Yang Akan Anda Pilih : "))
		with open("mentah.bashrc", 'a') as f:
			if pilih == (1):
				f.write ("\ncowsay -f beavis.zen.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (2):
				f.write ("\ncowsay -f bong.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (3):
				f.write ("\ncowsay -f bud-frogs.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (4):
				f.write ("\ncowsay -f bunny.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (5):
				f.write ("\ncowsay -f cheese.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (6):
				f.write ("\ncowsay -f cower.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (7):
				f.write ("\ncowsay -f daemon.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (8):
				f.write ("\ncowsay -f default.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (9):
				f.write ("\ncowsay -f dragon-and-cow.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (10):
				f.write ("\ncowsay -f dragon.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (11):
				f.write ("\ncowsay -f elephant-in-snike.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (12):
				f.write ("\ncowsay -f elephant.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (13):
				f.write ("\ncowsay -f eyes.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (14):
				f.write ("\ncowsay -f flaming-sheep.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (15):
				f.write ("\ncowsay -f ghostbusters.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (16):
				f.write ("\ncowsay -f head-in.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (17):
				f.write ("\ncowsay -f hellokitty.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (18):
				f.write ("\ncowsay -f kiss.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (19):
				f.write ("\ncowsay -f kitty.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (20):
				f.write ("\ncowsay -f koala.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (21):
				f.write ("\ncowsay -f kosh.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (22):
				f.write ("\ncowsay -f luke-koala.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (23):
				f.write ("\ncowsay -f mech-and-cow 'Jack Lucifer18' | lolcat")
			elif pilih == (24):
				f.write ("\ncowsay -f meow.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (25):
				f.write ("\ncowsay -f milk.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (26):
				f.write ("\ncowsay -f moofasa.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (27):
				f.write ("\ncowsay -f moose.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (28):
				f.write ("\ncowsay -f mutilated.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (29):
				f.write ("\ncowsay -f ren.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (30):
				f.write ("\ncowsay -f sheep.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (31):
				f.write ("\ncowsay -f skeleton.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (32):
				f.write ("\ncowsay -f stegosaurus.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (33):
				f.write ("\ncowsay -f stimpy.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (34):
				f.write ("\ncowsay -f three-eyes.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (35):
				f.write ("\ncowsay -f turkey.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (36):
				f.write ("\ncowsay -f turtle.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (37):
				f.write ("\ncowsay -f tux.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (38):
				f.write ("\ncowsay -f vader-koala.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (39):
				f.write ("\ncowsay -f vader.cow 'Jack Lucifer18' | lolcat")
			elif pilih == (40):
				f.write ("\ncowsay -f www.cow 'Jack Lucifer18' | lolcat")
			else :
				system ("exit")