from dotenv import load_dotenv
import discord
import os
from src.OPENAI_CHATGPT.chatGPT import gpthelp
import datetime

load_dotenv()

dctk = os.getenv('DCBOT_TOKEN')

class ActivateThePigBrain(discord.Client):
    async def on_ready(self):
        await self.change_presence(status=discord.Status.idle , activity=discord.Activity(type=discord.ActivityType.listening , name="水星記"))
        print("HoSing's PigBrain is online right now!")

    async def on_message(self , xx):
        if xx.author == self.user:
            return
        cm,um=None,None

        for ms in ["/ask","/help"]:
            if xx.content.startswith(ms):
                cm=xx.content.split(' ')[0]
                um=xx.content.replace(ms, '')

        if cm == '/help':
                embed=discord.Embed(title="HoSingLi的使用方式", description="本次回答使用了0.0000001%的豬腦和99.9999999%的ChatGPT", color=0xe100ff)
                embed.set_author(name="智多星-HOSING")
                embed.set_thumbnail(url="https://raw.githubusercontent.com/020darling/CDN/main/img/IMG_3339.PNG")
                embed.add_field(name="使用方法:", value="1.輸入/ask <問題>即可", inline=False)
                embed.set_footer(text="本答案由樹熊手寫，我李浩星對樹熊的任何錯誤言論進行負責！")
                await xx.channel.send(embed=embed)
            

        if cm == '/ask':
            DogShout = gpthelp(dp=um)
            embed=discord.Embed(title="拷問⭐⭐", description="本次回答使用了0.0000001%的頭腦和99.9999999%的ChatGPT", color=0xe100ff, timestamp=datetime.datetime.now())
            embed.add_field(name=" ", value=" ", inline=True)
            embed.set_author(name="智多星-HOSING")
            embed.set_thumbnail(url="https://raw.githubusercontent.com/020darling/CDN/main/img/IMG_3339.PNG")
            embed.add_field(name="QUESTION問題:", value=um, inline=False)
            embed.add_field(name="Answer回答:", value=DogShout, inline=True)
            embed.add_field(name=" ", value=" ", inline=True)
            embed.set_footer(text="⚠本答案由AI自動生成，我李浩星不對AI的任何錯誤言論進行負責！")
            await xx.channel.send(embed=embed)


intents = discord.Intents.default()
intents.message_content = True

hosing = ActivateThePigBrain(intents=intents)
