import discord
import os
from discord import message
import requests
import json
import random
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()

cussWords = ["lodu", "madarchod", "bhenchod", "gandu",
             "lavde", "chutiya", "chutiye", "bhosdike", "rendi", "randi", "baklund", "bsdk", "chu"]

starter_response_to_cussWords = ["Woahh, watch your language kid",
                                 "Bahoot jyada ni ho raha?", "Tameez se!!", "Chalo sorry bolo", "Aaj tu pitega", "Gaali not allowed, this is a family friendly server"]


def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q']
    return(quote)

def get_dadJoke():
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    json_data = json.loads(response.text)
    joke = json_data['joke']
    return joke

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
    if message.content.startswith('make me laugh daddy'):
        await message.channel.send(get_dadJoke())
    if any(word in msg for word in cussWords):
        await message.channel.send(random.choice(starter_response_to_cussWords))
client.run(os.getenv("TOKEN"))
