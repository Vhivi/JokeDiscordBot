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
with open('listeblague.txt', 'r') as f:
    jokelist = []
    current_block = ''
    for line in f:
        if line.strip() == '{':
            current_block = ''
        elif line.strip() == '}':
            jokelist.append(current_block.strip())
        else:
            current_block += line


def joke():
    # On renvoie une blague aléatoire
    return jokelist[random.randint(0, len(jokelist) - 1)]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Connecté en tant que')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # On vérifie que le bot ne se réponde pas à lui-même
        if message.author.id == self.user.id:
            return

        # Si un utilisateur tape !joke, on va afficher une blague
        if message.content.startswith('!joke'):
            await message.channel.send(joke())

intents = discord.Intents.default()
intents.messages = True

client = MyClient(intents=intents)
client.run(TOKEN)
