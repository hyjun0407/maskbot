from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os
import time
import telegram
import lxml
# 토큰을 지정해서 bot을 선언해 줍시다! (물론 이 토큰은 dummy!)
bot = telegram.Bot('1135279699:AAHMNoTLwbHc1ytS7sNTIS0KKgyhbaD-k5I')
# 우선 테스트 봇이니까 가장 마지막으로 bot에게 말을 건 사람의 id를 지정해줄게요.
# 만약 IndexError 에러가 난다면 봇에게 메시지를 아무거나 보내고 다시 테스트해보세요.
chat_id = bot.getUpdates()[-1].message.chat.id
bot.sendMessage(chat_id=chat_id, text='로딩성고오오오옹')

while True:
    url = "https://smartstore.naver.com/kumaelectron/products/4754238400"
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, "lxml")
    search = "not_goods"
    if search in html:
         a = 0
    else:
        bot.sendMessage(chat_id=chat_id, text='마스크가 이써요 빨리 접속 ㄱㄱ')

