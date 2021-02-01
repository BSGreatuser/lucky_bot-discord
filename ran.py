import discord
import urllib
from urllib.parse import quote_plus
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

client = discord.Client()

token = '★봇토큰★'

@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    game = discord.Game('★~하는중에 표시될 네임 작성★')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!운세'):
        w = message.content.split(" ")
        try:
            contentt = w[2]
        except IndexError:
            await message.channel.send('별자리가 입력되지 않았습니다')
            return

        if contentt == '전갈자리' or contentt == '물병자리' or contentt =='물고기자리' \
                or contentt =='양자리' or contentt =='황소자리' or contentt =='쌍둥이자리' \
                or contentt =='게자리' or contentt =='사자자리' or contentt =='처녀자리' \
                or contentt =='천칭자리' or contentt =='사수자리' or contentt =='염소자리':
            ww = message.content.split(" ")
            content = ww[1]
            star = urllib.parse.quote(content + '운세')
            hdr = {'User-Agent': 'Mozilla/5.0'}
            url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + star
            req = Request(url, headers=hdr)
            html = urllib.request.urlopen(req)
            soup = BeautifulSoup(html, "html.parser")

            today = soup.select('#yearFortune > div > div.detail.detail2 > p:nth-child(3)')[0].text
            tomorrow = soup.select('#yearFortune > div > div.detail.detail2 > p:nth-child(4)')[0].text
            realstar = soup.select('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a')[0].text

            thumbloc = soup.find('div', {'class': 'thumb'})
            thumbfind = thumbloc.find('img')
            thumb = thumbfind.get('src')

            embed = discord.Embed(colour=discord.Colour.gold())
            embed.add_field(name=f'{realstar} 오늘의 운세', value=today, inline=False)
            embed.add_field(name=f'{realstar} 내일의 운세', value=tomorrow, inline=False)
            embed.set_thumbnail(url=thumb)
            embed.set_footer(text='포춘82에서 제공한 정보입니다')
            await message.channel.send(embed=embed)
        else:
            errembed = discord.Embed(color=0xff0000)
            errembed.add_field(name='올바르지 않은 별자리입니다', value='``전갈자리`` ``물병자리`` ``물고기자리`` ``양자리`` ``황소자리`` ``쌍둥이자리`` ``게자리`` ``사자자리`` ``처녀자리`` ``천칭자리`` ``사수자리`` ``염소자리``')
            await message.channel.send(embed=errembed)
        
client.run(token)
