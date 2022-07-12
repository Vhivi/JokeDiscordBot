#!/usr/bin/python
# -*- coding: utf-8 -*-

# Projet de bot Discord

# Pour apprendre python en réalisant des projets simple, vous pouvez aussi
# vous intéresser au scripting et à l’automatisation avec des bots. Vous
# pouvez facilement faire un bot qui execute des tâches très simples en
# quelques dizaines de lignes de code.

import os

import random
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Liste des blagues
jokelist = ['''Pourquoi Napoléon n'a-t-il jamais déménager ?
Parce qu'il avait un Bon appart' !''',
'''Un jour un serveur de restaurant dit au chef cuisinier : "je pense qu'on serait de bons joueurs de tennis
Le chef demande : Pourquoi tu dis ça ? et le serveur répond : Parce qu'on fait déjà trois services par jour"''',
'''Pourquoi les marins ne peuvent-ils pas écrire ?
Parce qu'ils ont jeté l'ancre !''',
'''Quelle est la monnaie de la mer ?
Le sou marin.''',
'''Un électricien et un plombier font un match de judo. A votre avis, qui est le plus fort ?
L'électricien bien sûr, car il connait toutes les prises.''',
'''Quel est le comble pour un joueur de pétanque ?
C'est de perdre la boule.''',
'''Qu'est ce qu'une maman dinosaure raconte à son enfant avant qu'il aille se coucher ?
Une préhistoire.''',
'''Un client entre dans une librairie et dit au libraire :
- je voudrais un livre
- de quel auteur ?
- 20 cm, je crois...
- Vincent qui ?''']

def joke():
    # On renvoie une blague aléatoire
    return jokelist[random.randint(0, len(jokelist))]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Connecté en tant que')
        print(self.user.name)
        print(self.user.id)
        print('------')
        
    async def on_message(self, message):
        # On vérifie que le bot ne se répobnde à lui-même
        if message.author.id == self.user.id:
            return
        
        # Si un utilisateur tape !joke, on va afficher une blague
        if message.content.startswith('!joke'):
            await message.channel.send(joke())

intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(TOKEN)
