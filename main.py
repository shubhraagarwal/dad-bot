import discord
import os
from discord import message
import requests
import json
import random

client = discord.Client()
TOKEN = "ODQxMDk3NjQ0Mjg1NjI0Mzcy.YJhzOQ.ENCQ9E4YDQSOY5ZYZ-0HEoGQbFY"
cussWords = ["lodu", "madarchod", "bhenchod", "gandu",
             "lavde", "chutiya", "chutiye", "bhosdike"]

starter_response_to_cussWords = ["Woahh, watch your language kid",
                                 "Bahoot jyada ni ho raha?", "Tameez se!!", "Chalo sorry bolo", "Aaj tu pitega"]


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    return(quote)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if message.content.startswith('bsdk'):
        await message.channel.send("Jubaan sambhaal ke, varna iss server ki membership se bedahkal karr diye jaoge")
    if message.content.startswith('motivate me daddy'):
        await message.channel.send(get_quote())
    if any(word in msg for word in cussWords):
        await message.channel.send(random.choice(starter_response_to_cussWords))
client.run(TOKEN)
