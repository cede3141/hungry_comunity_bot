from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()
import random
import socket
import time
import asyncio
import mcstatus
import pymysql
from discord.ext import tasks
import datetime

from datetime import datetime
from discord.ext import commands
from discord.ext import tasks
from mcstatus import JavaServer
from discord import app_commands


PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents= discord.Intents.default())
        self.synced  = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f'{self.user}으로 로그인 하였습니다.')
        game =  discord.Game('play.WaveMC.kr')
        
        await self.change_presence(status=discord.Status.online, activity=game)

client = aclient()
tree =  app_commands.CommandTree(client)

server = JavaServer.lookup("play.wavemc.kr")
serverstatus = "bad"


#===============응답 ===============
# @tasks.loop(seconds=1)
# async def serverstatus(self):
#     try:                
#         status = server.status()
#         if status.latency >= 150:
#             if serverstatus != "bad":
#                 embed=discord.Embed(title="서버 상태", color=0xff0000)
#                 embed.add_field(name="서버의 지연시간이 불안정합니다.", value="서버의 지연시간이 150ms를 초과하였습니다.\n서버 접속이 불안정 또는 불가할 수 있습니다.", inline=True)
#                 embed.set_footer(text="eunha.mcsv.kr")
#                 await client.get_guild(1100416773213388900).get_channel(1111337783647273071).send(embed=embed)

#                 serverstatus = "bad"
#         else:
#             if serverstatus != "good":
#                 embed=discord.Embed(title="서버 상태", color=0x66ff00)
#                 embed.add_field(name="서버에 정상적으로 접속이 가능합니다.", value="서버에 발견된 문제가 없습니다.", inline=True)
#                 embed.set_footer(text="eunha.mcsv.kr")
#                 await client.get_guild(1100416773213388900).get_channel(1111337783647273071).send(embed=embed)
#                 serverstatus = "good"

#             # 1초 sleep하여 중복 전송 방지
#                 time.sleep(1)
#     except:
#         if serverstatus != "bad":
#             embed=discord.Embed(title="서버 상태", color=0xff0000)
#             embed.add_field(name="서버에 접속이 불가능합니다.", value="서버가 응답하지 않습니다.\n서버가 종료되었거나 문제가 발생하였습니다.", inline=True)
#             embed.set_footer(text="eunha.mcsv.kr")
#             await client.get_guild(1100416773213388900).get_channel(1111337783647273071).send(embed=embed)
#             serverstatus = "bad"

        
@tree.command(name='안녕',description='웨이브 봇과 인사해보세요!')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message("안녕하세요!")
    

@tree.command(name='랜덤숫자',description='범위 내의 랜덤한 숫자를 출력합니다.')
async def slash2(interaction: discord.Interaction, 숫자: int, 숫자2: int):
    await interaction.response.send_message(random.randrange(숫자,숫자2+1))



@tree.command(name='애교',description='~')
async def 애교(interaction: discord.Interaction):
    await interaction.response.send_message("웨이브는 애교같은 거 부릴 줄 몰라요~")
    
@tree.command(name='바보',description='바보 아닙니다.')
async def 바보(interaction: discord.Interaction):
    await interaction.response.send_message("이이이잌...")

@tree.command(name='서버상태',description='WaveMC의 정보를 알려줍니다.') #서버 상태 확인
async def 서버상태(interaction: discord.Interaction):
    try:                
        status = server.status()
        await interaction.response.send_message(f"서버상태\n접속자: {status.players.online} player(s)\n핑: {round(status.latency)} ms")
        
    except:
        await interaction.response.send_message("서버에 접속할 수 없습니다.")

# @tree.command(name='낚시대회',description='낚시대회에 관한 정보를 알려줍니다.') #낚대 상황
# async def 낚시대회(interaction: discord.Interaction):
#    now = datetime.now()
#    if datetime.today().weekday() % 2 == 0:
#         if now.hour+9 < 16:
#            await interaction.response.send_message("아직 낚시대회가 시작하지 않았습니다.(시작시간: 4시)")
        
#         elif now.hour+9 == 16:
#            await interaction.response.send_message("현재 낚시대회가 진행중입니다!")

#         else:
#            await interaction.response.send_message("오늘의 낚시대회는 종료되었습니다.(시작시간: 4시)")
           

#    else:
#         if now.hour+9 < 20:
#            await interaction.response.send_message("아직 낚시대회가 시작하지 않았습니다.(시작시간: 8시)")
        
#         elif now.hour+9 == 20:
#            await interaction.response.send_message("현재 낚시대회가 진행중입니다!")

#         else:
#            await interaction.response.send_message("오늘의 낚시대회는 종료되었습니다.(시작시간: 8시)")





    
@tree.command(name='패치노트',description='업데이트 정보를 확인하세요!')
async def 패치노트(interaction: discord.Interaction):
    await interaction.response.send_message("""```#####################패치노트#####################
2023/08/25 - 12:37
- 임베드 명령어로 필드 여러개를 사용할 수 있도록 변경되었습니다.
- /임베드사용법 명령어가 추가되었습니다.
```""",ephemeral=True)
    
@tree.command(name='changelog',description='개발자 전용 명령어입니다.')
async def changelog(interaction: discord.Interaction):
    if interaction.user.id == 766875066490683392:
        await interaction.response.send_message("""```#####################패치노트#####################
2023/08/25 - 12:37
- 임베드 명령어로 필드 여러개를 사용할 수 있도록 변경되었습니다.
- /임베드사용법 명령어가 추가되었습니다.
```""")
    else:
        await interaction.response.send_message("권한이 없거나 알 수 없는 오류가 발생하였습니다.",ephemeral=True)

@tree.command(name='버그제보', description= '디스코드 봇과 관련된 버그만 제보해 주세요.')
async def 문의(interaction: discord.Interaction, 내용 : str):
    embed=discord.Embed(title="버그 제보", description="", color=0x14ffd8)
    embed.add_field(name="버그 제보가 접수되었습니다.", value="", inline=False)
    embed.add_field(name="장난성, 부적적한 제보는 제재 사유가 될 수 있습니다.", value="", inline=False)
    embed.add_field(name="해당 제보 내용은 관리자에게 전달됩니다.", value="", inline=False)
    await interaction.response.send_message(embed=embed,ephemeral=True)

    users = await client.fetch_user("766875066490683392")
    await users.send("질문자 아이디: {} / 문의 내용: {}".format(interaction.user.id, 내용))


@tree.command(name='제보답변', description= '개발자 전용 명령어입니다.')
async def 문의답변(interaction: discord.Interaction, 아이디:str, 내용 : str):
    if interaction.user.id == 766875066490683392:
        user = await client.fetch_user("{}".format(아이디))
        await user.send("**제보 답변**\n{}".format(내용))
        await interaction.response.send_message(f"**답변완료**\n내용:{내용}")
        
    else:
        await interaction.response.send_message("권한이 없거나 알 수 없는 오류가 발생하였습니다.",ephemeral=True)

        
@tree.command(name='말하기', description= '관리자 전용 명령어 입니다.')
async def 문의답변(interaction: discord.Interaction ,내용 : str , 채널: discord.TextChannel):
    if interaction.user.guild_permissions.administrator:
        channel = await client.fetch_channel("{}".format(채널.id))
        await channel.send(내용.replace("$","\n"))
        await interaction.response.send_message("전송 완료",ephemeral=True)
    else:
        await interaction.response.send_message("권한이 없거나 알 수 없는 오류가 발생하였습니다.",ephemeral=True)

@tree.command(name='임베드', description= '관리자 전용 명령어 입니다.(/임베드사용법 명령어를 사용하여 자세한 사용법을 확인하세요.)')
async def 임베드(interaction: discord.Interaction ,채널: discord.TextChannel, 타이틀: str ,설명: str = "",필드: str = "None;None",바닥글: str = ""):
    if interaction.user.guild_permissions.administrator:
        embed=discord.Embed(title=타이틀.replace("$","\n"), description=설명.replace("$","\n"), color=0x14ffd8)

        fields=필드.split(';')

        for i in range(0,len(fields)-1,2):
            embed.add_field(name=fields[i].replace("$","\n"), value=fields[i+1].replace("$","\n"), inline=False)
        
        embed.set_footer(text=바닥글)


        channel = await client.fetch_channel("{}".format(채널.id))
        await channel.send(embed=embed)
        await interaction.response.send_message("전송 완료",ephemeral=True)
    else:
        await interaction.response.send_message("권한이 없거나 알 수 없는 오류가 발생하였습니다.",ephemeral=True)

@tree.command(name='임베드사용법', description= '관리자 전용 명령어 입니다.')
async def 임베드사용법(interaction: discord.Interaction):
    if interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("$: 줄 바꾸기\n필드1 제목;필드1 내용;필드2 제목;필드2 내용...",ephemeral=True)
    else:
        await interaction.response.send_message("권한이 없거나 알 수 없는 오류가 발생하였습니다.",ephemeral=True)
        
@tree.command(name='이미지', description= '관리자 전용 명령어 입니다.')
async def 이미지(interaction: discord.Interaction ,채널: discord.TextChannel, 주소: str):
    if interaction.user.guild_permissions.administrator:
        embed = discord.Embed(color=0x14ffd8)
        embed.set_image(url=주소)
        channel = await client.fetch_channel("{}".format(채널.id))
        await channel.send(embed=embed)
        await interaction.response.send_message("완료",ephemeral=True)
    else:
        await interaction.response.send_message("권한이 없거나 알 수 없는 오류가 발생하였습니다.",ephemeral=True)

@tree.command(name='가위바위보',description='웨이브 봇과 가위바위보를 해보세요.') #가위바위보
async def 가위바위보(interaction: discord.Interaction, 선택: str): 
    user_id = interaction.user.id
    rps_table = ['가위', '바위', '보']
    bot = random.choice(rps_table)
    result = rps_table.index(선택) - rps_table.index(bot) 
    if result == 0:
        await interaction.response.send_message(f'<@{user_id}>: {선택} , 봇: {bot}  비겼습니다.')
    elif result == 1 or result == -2:
        await interaction.response.send_message(f'<@{user_id}>: {선택} , 봇: {bot}  유저승')
    else:
        await interaction.response.send_message(f'<@{user_id}>: {선택} , 봇: {bot}  봇승')

        
try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
