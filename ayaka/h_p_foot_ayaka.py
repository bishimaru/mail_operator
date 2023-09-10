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
from widget import pcmax, happymail, func
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback
from datetime import timedelta


def h_p_foot(cnt):
  name = "彩香"
  return_foot_message = """足跡からです！

初めまして、あやかです。
アプリ入れるのやめたつもりが、なぜか入っていたので、この際やってしまおうと始めました...笑

あ、自己紹介が遅れました。
普段は都内の幼稚園で保育士として働いています〜！

子供が大好きでもちもちしてます(ﾉ)`∨´(ヾ)

お仕事とかは充実しているんですが、仕事柄なんですが出会いとかは全然なくて...泣

同僚の子がここでせふれさんを作ったって言っていて、それなら私もって思ってせふれ探しを始めました！！
職業柄甘えられるのも好きだけど、甘えるのも大好きな寂しがり屋です(>_<)

私と友達以上、恋人未満の関係に興味あればお返事貰えたらとても嬉しいです( ´,,•ω•,,`)"""
  h_return_foot_img = ""
  p_return_foot_img = ""
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  p_w = func.get_windowhandle("pcmax", name)

  try:   
    func.h_p_return_footprint(name, h_w, p_w, driver, return_foot_message, cnt, h_return_foot_img, p_return_foot_img)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True
if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    cnt = int(sys.argv[1])
  h_p_foot(cnt)