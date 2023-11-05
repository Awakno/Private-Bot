# Mon Bot Discord Personnalisé

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![discord.py Version](https://img.shields.io/badge/discord.py-1.7%2B-blue)

## Présentation
Ce bot Discord personnalisé est un projet open-source conçu pour vous aider à démarrer avec votre propre bot Discord. Il est basé sur la bibliothèque discord.py (rewrite version) en Python. Vous pouvez l'utiliser comme base pour développer des fonctionnalités supplémentaires ou le personnaliser selon vos besoins.

## Fonctionnalités
- Modération
- Logs
- commande utilitaire

## Installation
1. Assurez-vous d'avoir Python 3.8 ou une version ultérieure installée.
2. Clonez ce référentiel sur votre ordinateur.
3. Installez les dépendances en utilisant `pip install -r requirements.txt`.
4. Créez un fichier `config.json` et ajoutez-y vos clés API et d'autres configurations (voir ci-dessous).
5. Exécutez le bot en utilisant `python main.py`.

## Configuration
- Si vous voulez désactiver des commandes / fonctionnalité, renommez le nom du fichier avec un "-" devant celui ci
- Créez un fichier `config.json` dans le répertoire du bot avec les détails de configuration suivants :

```json
{
    "token": "TOKEN",
    "prefix": "$",
    "lang": "fr",
    "statut": {
        "playing": "n",
        "watching": "y",
        "listening": "n",
        "streaming": "n",
        "text": "Powered by Private-Bot",
        "url": "https://twitch.tv/x"
    },

    "owner": [
        
    ],
    
    "logs": {
        "activate": "n",
        "channel": "channel ID"
    },
    "tempo-vocal":{
        "activate": "y",
        "hub": "channel ID",
        "categories": "channel id",
        "names": "salon de {user.name}"
    },
     
    "welcome": {
        "activate": "n",
        "embeds": "n",
        "channel": "channel ID",
        "message": "Bienvenue {user.mention} ! comment tu vas ?",
        "embed": {
            "title": "Bienvenue {user.name}",
            "description": "Bienvenue sur le serveur {guild.name}",
            "author": "Private-Bot",
            "author_avatar": "",
            "image" : "",
            "thumbnail": "{user.avatar}",
                "fields": [
                    {"name": "Example", "value": "Example", "inline": true}
                    

            ],
            "footer": "Tu es notre {guild.membercount} membres",
            "color": "#FF0000",
            "footer-url": "{guild.icon}" 

        }

    },
    "leave": {
        "activate": "y",
        "embeds": "n",
        "channel": 1163191742435168438,
        "message": "Au revoir {user.name} :cry:",
        "embed": { // Configuration du embed
            "title": "Au revoir {user.name}",
            "description": "Bienvenue sur le serveur {guild.name}",
            "author": "Private-Bot",
            "author_avatar": "",
            "image" : "",
            "thumbnail": "{user.avatar}",
                "fields": [
                    {"name": "Example", "value": "Example", "inline": true}
                    

            ],
            "footer": "Tu es notre {guild.membercount} membres",
            "color": "#FF0000",
            "footer-url": "{guild.icon}" 

        }

    }
}
```

# Variable
Private-Bot possède un système de variable permettant d'avoir des données non constante
exemple: "Bienvenue {user}"
BOT: "Bienvenue utilisateur#0000"
__Si vous voulez en savoir plus regarder le fichier variable.py !__



## Besoin d'aide ?
Rejoins le support 
"https://discord.gg/ZUFb892bdZ"

