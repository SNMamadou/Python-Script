devices=[]

file=open("devices.txt","a")
print("Il faut écrire 'ex' pour quitter \n")

while True:

	NewiTem=input("ajoutez un nouveau périphérique" + "  ")
	if NewiTem == "ex":
		print("Parfait c'est bon!")
		break
	file.write(NewiTem + "\n")


file.close()

