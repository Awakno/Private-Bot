import os

try:
    print("L'installation est en cours")
    os.system("pip install -r requirements.txt")
    try:
        import discord
        print("Succes !")
    except:
        print("Une erreur a eu lieux durant l'importation !")
except Exception as e:
    print("Une erreur a eu lieux durant l'installation !")
    print(e)

print("Voulez vous lancer le bot ? [o/n]")
reponse = input('>>> ')
rep = reponse.lower()

if rep == "o":
    os.system("python main.py")
else:
    print("bye")