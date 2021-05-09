import os, datetime, sys, math, requests, re

from bs4 import BeautifulSoup

# 봇 재시작
def restart_bot():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def mid_exam_strong():
    message_time = datetime.datetime.now()
    mid_exam_1 = datetime.datetime(2021, 4, 19, 9)
    mid_exam_2 = mid_exam_1 - message_time
    mid_exam_3 = math.trunc(mid_exam_2.seconds/3600)
    mid_exam_4 = math.trunc((mid_exam_2.seconds - mid_exam_3*3600)/60)
    mid_exam_5 = (mid_exam_2.seconds - mid_exam_3*3600) - mid_exam_4 *60
    return mid_exam_2.days, mid_exam_3, mid_exam_4, mid_exam_5

def fin_exam_strong():
    message_time = datetime.datetime.now()
    fin_exam_1 = datetime.datetime(2021, 6, 10, 9)
    fin_exam_2 = fin_exam_1 - message_time
    fin_exam_3 = math.trunc(fin_exam_2.seconds/3600)
    fin_exam_4 = math.trunc((fin_exam_2.seconds - fin_exam_3*3600)/60)
    fin_exam_5 = (fin_exam_2.seconds - fin_exam_3*3600) - fin_exam_4 *60
    return fin_exam_2.days, fin_exam_3, fin_exam_4, fin_exam_5

# 코로나 확진자 수 크롤링
def corona_message():
    url = "http://ncov.mohw.go.kr/"
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, "html.parser")
    title1 = soup.select_one('body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum_today_new > div > ul > li:nth-child(1) > span.data')
    title2 = soup.select_one('body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum_today_new > div > ul > li:nth-child(2) > span.data')
    title3 = soup.select_one('body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > h2 > a > span.livedate')
    regex = re.compile('{}(.*){}'.format(re.escape('>'), re.escape('<')))
    regex1 = re.compile('{}(.*){}'.format(re.escape('('), re.escape(')')))
    text1 = regex.findall(str(title1))
    text2 = regex.findall(str(title2))
    text3 = regex1.findall(str(title3))
    stringA = text3[0]
    text4 = int(text1[0]) + int(text2[0])
    return text1[0], text2[0], text4, text3[0]

def lan_check(tar):
    if tar == '한':
        target_lan = 'ko'
    elif tar == '영':
        target_lan = 'en'
    elif tar == '일':
        target_lan = 'ja'
    return target_lan

def time_division(time):
    td_days = time.days
    td_hours = math.trunc(time.seconds/3600)
    td_minutes = math.trunc((time.seconds - td_hours*3600)/60)
    td_seconds = (time.seconds - td_hours*3600) - td_minutes *60
    return td_days, td_hours, td_minutes, td_seconds

# 남은 시간 출력
def remaining_time(target_time, current_time):
    r_time = target_time - current_time
    r_years = math.trunc(r_time.days/365)
    r_days = r_time.days - (r_years*365)
    r_hours = math.trunc(r_time.seconds/3600)
    r_minutes = math.trunc((r_time.seconds - r_hours*3600)/60)
    r_seconds = (r_time.seconds - r_hours*3600) - r_minutes *60
    return r_years, r_days, r_hours, r_minutes, r_seconds

# 예외 메시지 출력
def get_full_class_name(obj):
    module = obj.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return obj.__class__.__name__
    return module + '.' + obj.__class__.__name__ + '\n'

# 문자열 공백 등 제거
def no_space(text):
    text1 = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', text)
    text2 = re.sub('\n\n', '', text1)
    return text2


## 학식 관련 함수

# 예산캠퍼스(공주대 홈페이지)
def get_yesan_meal_text(ysmeal):
    ysmeal = ysmeal.get_text()
    ysmeal = ysmeal.replace("<td>", "")
    ysmeal = ysmeal.replace(" ", "")
    ysmeal = ysmeal.replace("<br/>", "")
    ysmeal = ysmeal.replace("</td>", "")
    ysmeal = ysmeal.replace("\r", "\n")
    return ysmeal

def get_yesan_meal_date_text(ysdate):
    ysdate = ysdate.get_text()
    ysdate = no_space(ysdate)
    ysdate = ysdate.replace("<th scope=\"col\">", "")
    ysdate = ysdate.replace("</th>", "")
    ysdate = ysdate.replace("<th class=\"on\" scope=\"col\">", "")
    return ysdate

# 요일 영한변환
def dow_eng2kor(dow):
    if dow == "Mon":
        return "월"
    elif dow == "Tue":
        return "화"
    elif dow == "Wed":
        return "수"
    elif dow == "Thu":
        return "목"
    elif dow == "Fri":
        return "금"
    elif dow == "Sat":
        return "토"
    elif dow == "Sun":
        return "일"

# 학생생활관 홈페이지
def get_dream_domi_meal_text(dmmeal):
    dmmeal = dmmeal.get_text()
    dmmeal = dmmeal.replace("<td data-mqtitle=\"breakfast\">", "")
    dmmeal = dmmeal.replace("<td data-mqtitle=\"lunch\">", "")
    dmmeal = dmmeal.replace("<td class=\"noedge-r last\" data-mqtitle=\"dinner\">", "")
    dmmeal = dmmeal.replace("</td>", "")
    dmmeal = dmmeal.replace("amp;", "")
    dmmeal = dmmeal.replace(",", "\n")
    if dmmeal != "":
        return dmmeal
    else:
        return "- 항목 없음 -"
        
def get_cheonan_domi_meal_text(dmmeal):
    dmmeal = dmmeal.get_text()
    dmmeal = dmmeal.replace("<td data-mqtitle=\"breakfast\">", "")
    dmmeal = dmmeal.replace("<td data-mqtitle=\"lunch\">", "")
    dmmeal = dmmeal.replace("<td class=\"noedge-r last\" data-mqtitle=\"dinner\">", "")
    dmmeal = dmmeal.replace("</td>", "")
    dmmeal = dmmeal.replace("amp;", "")
    dmmeal = dmmeal.replace(" ", "\n")
    if dmmeal != "":
        return dmmeal
    else:
        return "- 항목 없음 -"

def get_domi_meal_date_text(dmdate):
    dmdate = dmdate.get_text()
    dmdate = dmdate.replace("<td data-mqtitle=\"date\">", "")
    dmdate = dmdate.replace("</td>", "")
    dmdate = dmdate.replace("<font class=\"day\">", "")
    dmdate = dmdate.replace("</font>", "")
    return dmdate