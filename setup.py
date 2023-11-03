import os

try:
    try:
        import discord
    except:
        os.system("pip install -r requirements.txt")
except Exception as e:
    print(f"Une erreur est survenue: {e}")

print("Voulez vous lancer le bot ? [o/n]")
reponse = input('>>> ')
rep = reponse.lower()

if rep == "o":
    os.system("python main.py")
else:
    print("bye")
