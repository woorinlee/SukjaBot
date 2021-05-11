import sukjabot2_setting, sukjabot2_define
import discord, datetime, pytz
from discord.ext import tasks


## 설정
bot = sukjabot2_setting.bot
sjb_avatar_url = sukjabot2_setting.sjb_avatar_url


## 매크로

# 중간고사
@tasks.loop(seconds=2.5)
async def mid_exam_status():
    me_day, me_hour, me_min, me_sec = sukjabot2_define.mid_exam_strong()
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('중간고사까지 {}일 {}시간 {}분 {}초 남았습니다.'.format(me_day, me_hour, me_min, me_sec)))

@tasks.loop(seconds=3600)
async def mid_exam_output():
    me_day, me_hour, me_min, me_sec = sukjabot2_define.mid_exam_strong()
    embed=discord.Embed(title="", description=f"",timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0xF14952)
    embed.add_field(name="조졌어요!",value='중간고사까지 {}일 {}시간 {}분 {}초 남았습니다.'.format(me_day, me_hour, me_min, me_sec),inline=False)
    embed.set_author(name="모두를 위한 타이머",icon_url=sjb_avatar_url)
    await bot.get_channel(int(sukjabot2_setting.mainch)).send(embed=embed)

# 기말고사
@tasks.loop(seconds=2.5)
async def fin_exam_status():
    fe_day, fe_hour, fe_min, fe_sec = sukjabot2_define.fin_exam_strong()
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('중간고사까지 {}일 {}시간 {}분 {}초 남았습니다.'.format(fe_day, fe_hour, fe_min, fe_sec)))

@tasks.loop(seconds=3600)
async def fin_exam_output():
    fe_day, fe_hour, fe_min, fe_sec = sukjabot2_define.fin_exam_strong()
    embed=discord.Embed(title="", description=f"",timestamp=datetime.datetime.now(pytz.timezone('UTC')),color=0xF14952)
    embed.add_field(name="조졌어요!",value='기말고사까지 {}일 {}시간 {}분 {}초 남았습니다.'.format(fe_day, fe_hour, fe_min, fe_sec),inline=False)
    embed.set_author(name="모두를 위한 타이머",icon_url=sjb_avatar_url)
    await bot.get_channel(int(sukjabot2_setting.mainch)).send(embed=embed)


# 컴공 공지 출력 (테스트중)
@tasks.loop(seconds=5)
async def testmacro():
    await bot.get_channel(int(sukjabot2_setting.mainch)).send()