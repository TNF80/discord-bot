#https://discord.com/oauth2/authorize?client_id=1562510129251881100&permissions=67584&integration_type=0&scope=b
import discord
import random

dice = random.randint(1,6)
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
async def on_ready():
    print(f'Logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == '!hello':
        await message.channel.send('HI I AM A BOT')
    if message.content.lower() == '!bye':
        await message.channel.send('byeeeeeeeeeeeeee') 
    if message.content.lower() == '!roll':
            await message.channel.send(dice)


    if message.content.lower() == '!ideas':
            idea = ideas()
            await message.channel.send(idea)

def ideas():
    idea_list = ['Follow the 5 Rs: Refuse single-use plastics, Reduce overall consumption, Reuse items, Recycle properly, and Rot (compost) organic waste.',
        'Switch to Reusables: Use stainless steel bottles, cloth shopping bags, and reusable food containers.',
        'Dispose of Hazardous Materials Safely: Never pour chemicals, paints, electronic waste, or batteries into standard household trash or down drains. Take them to designated local recycling sites.',
        'Choose Cleaner Transportation: Walk, cycle, use public transit, or carpool to reduce vehicle exhaust emissions.',
        'Save Energy at Home: Switch to LED bulbs, unplug unused electronics, and lower heating or cooling usage to reduce fossil fuel consumption from power plants.',
        'Avoid Burning Household Waste: Burning trash releases toxic dioxins and fine particulate matter into the air.']
    
    return random.choice(idea_list)
        













