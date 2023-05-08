from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback


name = "ゆあ&すみれ"
happy_windowhandle = "B6A833C61FC9E66870AD876B6221DD30"
pcmax_windowhandle = "236654B90E86E9FEC6C48964CD1D1FAB"
title = "六本木の高級デリ嬢2人組の専属セフレ募集"
text = """掲示板見てくれてありがとうございます♫、
六本木の高級デリヘルで現役キャストしてます『ゆあ』と『すみれ』です！

お店の特別コースで私とすみれの3Pコースがあるんですけど、
１回やってみたら二人ともそれにハマっちゃって笑

私がSですみれがMなのでかなり楽しめると思うんですけど高級店の3Pだからか中々このコース選んでくれる人がいなくて（ ; ; ）

私たち的にはもっと3Pを楽しみたいけど、相手がいないので
じゃあ、このサイトでプライベートで長く関係を続けられる人を見つけよってなって、今お相手を探してるところです( ^ω^ )

一応、高級店に在籍してるので二人とも夜の営みには自信ありです笑

こんな私たちの専属のセフレになってくれる方で純粋にエッチを楽しみたい方ならどんな人でも大歓迎です！

ご連絡お待ちしてます♡"""


options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

# try:   
#   happymail.re_post(name, setting.yua_happy_windowhandle, driver, title, text)
# except Exception as e:
#   print('=== エラー内容 ===')
#   print(traceback.format_exc())
#   print('type:' + str(type(e)))
#   print('args:' + str(e.args))
#   print('message:' + e.message)
#   print('e自身:' + str(e))
try:
  pcmax.re_post(name, setting.yua_pcmax_windowhandle, driver)
except Exception as e:
  print('=== エラー内容 ===')
  print(traceback.format_exc())
  print('type:' + str(type(e)))
  print('args:' + str(e.args))
  print('message:' + e.message)
  print('e自身:' + str(e))
driver.quit()