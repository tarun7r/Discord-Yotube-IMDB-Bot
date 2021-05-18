from bs4 import BeautifulSoup
import requests
import discord
import json
import os
import csv
import random
from discord.ext import commands
client = discord.Client()
bot = commands.Bot(command_prefix='=', help_command=None)  #Bot command


@bot.event
async def on_ready():
    print('We have logged')

@bot.command()
async def imdb(ctx, arg):
                    """IMDB API - Its a free api you can register for it in the rapidapi website"""
                    url = "https://imdb8.p.rapidapi.com/auto-complete"
                    querystring = {"q": arg}

                    headers = {
                                'x-rapidapi-key': "", #you rapid api key
                                'x-rapidapi-host': "imdb8.p.rapidapi.com"
                                    }

                    response = requests.request("GET", url, headers=headers, params=querystring)
                    data = json.loads(response.text)
                    for out in data['d']:
                        imd = out['id']
                        break
                    source = requests.get('https://www.imdb.com/title/'+imd).text
                    soup = BeautifulSoup(source,'lxml') 
                    name = soup.find('h1').text
                    imdbrating = soup.find('div',{'class':'ratingValue'}).text
                    imdbrating = " ".join(imdbrating.split())
                    imdbvotes = soup.find('span',{'class':'small'}).text
                    details = soup.find('div',{'class':'subtext'}).text
                    details = " ".join(details.split())
                    summary = soup.find('div',{'class':'summary_text'}).text
                    summary = summary.strip()
                    directors = soup.find('div',{'class':'credit_summary_item'}).text
                    directors = " ".join(directors.split())
                    url = soup.find('img')
                    image = url['src']
                    embed=discord.Embed(title=name, url='https://www.imdb.com/title/'+imd, description="Movie/Series Information", color=0xffae00)
                    embed.set_thumbnail(url=image)
                    embed.add_field(name="IMDB Rating", value= imdbrating, inline=True)
                    embed.add_field(name="IMDB VOTES", value= imdbvotes, inline=True)
                    embed.add_field(name="DETAILS", value= details, inline=True)
                    embed.add_field(name="DIRECTORS", value=directors, inline=True)
                    embed.add_field(name="SUMMARY", value= summary, inline=False)
                    await ctx.send(embed=embed)
@bot.command()
async def mood(ctx, arg):
                    url = "https://imdb8.p.rapidapi.com/auto-complete"
                    if arg == "action":
                        lines = open(r'action.txt',encoding='utf-8').read().splitlines()
                    elif arg == "anime" :
                        lines = open(r'anime.txt',encoding='utf-8').read().splitlines()
                    elif arg == "adventure" :
                        lines = open(r'adventure.txt',encoding='utf-8').read().splitlines()
                    elif arg == "comedy" :
                        lines = open(r'comedy.txt',encoding='utf-8').read().splitlines()
                    elif arg == "crime" :
                        lines = open(r'crime.txt',encoding='utf-8').read().splitlines()
                    elif arg == "horror" :
                        lines = open(r'horror.txt',encoding='utf-8').read().splitlines()
                    elif arg == "mystery" :
                        lines = open(r'mystery.txt',encoding='utf-8').read().splitlines()
                    elif arg == "scifi" :
                        lines = open(r'scifi.txt',encoding='utf-8').read().splitlines()
                    elif arg == "thriller" :
                        lines = open(r'thriller.txt',encoding='utf-8').read().splitlines()

                    data = random.choice(lines)
                    querystring = {"q": data}
                    headers = {
                                'x-rapidapi-key': "01e73b1ea8msh18f89608d977e12p1fda1bjsn74e2d0cda8a0",
                                'x-rapidapi-host': "imdb8.p.rapidapi.com"
                                    }

                    response = requests.request("GET", url, headers=headers, params=querystring)
                    data = json.loads(response.text)
                    for out in data['d']:
                        imd = out['id']
                        break
                    source = requests.get('https://www.imdb.com/title/'+imd).text
                    soup = BeautifulSoup(source,'lxml') 
                    name = soup.find('h1').text
                    imdbrating = soup.find('div',{'class':'ratingValue'}).text
                    imdbrating = " ".join(imdbrating.split())
                    imdbvotes = soup.find('span',{'class':'small'}).text
                    details = soup.find('div',{'class':'subtext'}).text
                    details = " ".join(details.split())
                    summary = soup.find('div',{'class':'summary_text'}).text
                    summary = summary.strip()
                    directors = soup.find('div',{'class':'credit_summary_item'}).text
                    directors = " ".join(directors.split())
                    url = soup.find('img')
                    image = url['src']
                    embed=discord.Embed(title=name, url='https://www.imdb.com/title/'+imd, description="Movie/Series Information", color=0xffae00)
                    embed.set_thumbnail(url=image)
                    embed.add_field(name="IMDB Rating", value= imdbrating, inline=True)
                    embed.add_field(name="IMDB VOTES", value= imdbvotes, inline=True)
                    embed.add_field(name="DETAILS", value= details, inline=True)
                    embed.add_field(name="DIRECTORS", value=directors, inline=True)
                    embed.add_field(name="SUMMARY", value= summary, inline=False)
                    await ctx.send(embed=embed)
@bot.command()
async def help(ctx):
        embed=discord.Embed(title="IMDb Bot Commands", url="https://discord.com/api/oauth2/authorize?client_id=826940767712444476&permissions=2148006976&scope=bot", description="**Show IMDb Information and Generate Random Movie**", color=0xffae00)
        embed.add_field(name="!imdb [ Movie / Series Name]", value="example:  **!imdb Avengers**", inline=True)
        embed.add_field(name="!mood [ action,adventure,anime,comedy,crime,horror,mystery,scifi]", value="example:  **!mood action**", inline=False)
        embed.add_field(name="!commands", value="List all of all IMDb bot commands", inline=True)
        embed.add_field(name="!invite", value="Invite Link will be sent", inline=True)
        await ctx.send(embed=embed)



bot.run('') #your bot token


