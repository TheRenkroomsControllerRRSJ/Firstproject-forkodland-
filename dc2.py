import requests #bu komuda erişebilmek için: pip install requests demen lazım
import discord #bu komuda erişebilmek için: pip install discord demen lazım
import random
import os
from discord.ext import commands
from bot_mantik import emoji_olusturucu, yazi_tura, sifre_olusturucu

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık!')

@bot.command()
async def hello(ctx):
    await ctx.send('Selam! Ben bir botum!')

@bot.command()
async def smile(ctx):
    await ctx.send(emoji_olusturucu())

@bot.command()
async def coin(ctx):
    await ctx.send(yazi_tura())

@bot.command(name='pass')
async def generate_pass(ctx):
    await ctx.send(sifre_olusturucu(10))

@bot.command()
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    dosyalar = os.listdir('images')
    mem_dosyasi = random.choice(dosyalar)
    dosya_yolu = os.path.join('images', mem_dosyasi)
    with open(dosya_yolu, 'rb') as f:
        resim = discord.File(f)
    await ctx.send(file=resim)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("TOKEN BURAYA YAZILCAK")
