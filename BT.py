import requests
import discord
import unicodedata
from discord.ext import commands
import time
from bs4 import BeautifulSoup

TOKEN = ''
client = commands.Bot(command_prefix =  '!')
n = 0

@client.event
async def on_ready():
    print("Bot Ready")

@client.command(pass_context=True)
async def lookup(ctx, query):
    url = 'https://www.brownthomas.com/men/'
    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    embed = discord.Embed(color=0x00ff00)
    embed.title = "test"
    total_items = soup.find('div', class_='pagination')
    total_items2 = total_items.find('span', attrs={'class':'pag-total-items-show'})
    total_items2 = total_items2.text[:-9]
    s = total_items2
    s = s.replace(',','')
    print(s)
    print(url+'?&sz='+s)
    result = requests.get(url+"?&sz="+s)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    for image in soup.find_all('li', class_='grid-tile js-product-grid-tile'):
            product_image = image.div.div.a.picture.source.get("data-srcset")
            item_price = image.find('span', attrs={'class':'product-sales-price'}).text
            item_brand = image.find('span', attrs={'class':'product-brand'}).text
            item_name = image.find('span', attrs={'class':'product-name name-link'}).text
            n = 0
            n + 1
            embed = discord.Embed(
                    title = 'Brand',
                    description = item_brand,
                    colour = discord.Colour.blurple()
                )
            embed.set_author(name='Brown Thomas Scraper')
            embed.add_field(name='Product Name', value=item_name, inline=False)
            embed.add_field(name='Price', value=item_price, inline=False)
            embed.set_footer(text='Watson',icon_url='https://cdn.discordapp.com/app-icons/711256658592137237/74a1779046799c1665d03cda5bb9694f.png'
    ),
            embed.set_thumbnail(url=product_image)
            if(query.lower() in item_brand.lower()):
                await ctx.send(embed=embed)
                print('Item Found')

client.run(TOKEN)
