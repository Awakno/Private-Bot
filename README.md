# Mon Bot Discord Personnalisé

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![discord.py Version](https://img.shields.io/badge/discord.py-1.7%2B-blue)

## Présentation
Ce bot Discord personnalisé est un projet open-source conçu pour vous aider à démarrer avec votre propre bot Discord. Il est basé sur la bibliothèque discord.py (rewrite version) en Python. Vous pouvez l'utiliser comme base pour développer des fonctionnalités supplémentaires ou le personnaliser selon vos besoins.

## Fonctionnalités
- Commandes personnalisées
- Gestion de la présence du bot
- Événements de base (messages, membres, rôles)
- Structure modulaire

## Installation
1. Assurez-vous d'avoir Python 3.8 ou une version ultérieure installée.
2. Clonez ce référentiel sur votre ordinateur.
3. Installez les dépendances en utilisant `pip install -r requirements.txt`.
4. Créez un fichier `config.json` et ajoutez-y vos clés API et d'autres configurations (voir ci-dessous).
5. Exécutez le bot en utilisant `python main.py`.

## Configuration
Créez un fichier `config.json` dans le répertoire du bot avec les détails de configuration suivants :

```json
{
    "token": "Your token",
    "prefix": "$",
    "lang": "en",
    
    "owner": [
        "Owner bot"
    ],
    "logs_channel": "Channel logs"
}

