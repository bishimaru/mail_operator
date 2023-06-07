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

def h_foot(cnt):
  name = "くみ"
  return_foot_message = """こんにちは！くみです♪
このサイトで今だけせふれさん探してます！

先日、とっても可愛い水着を購入しました！その水着を見てもらいたくて、足跡をつけてくれた方に声をかけさせていただきました。

思わず「これを着て海やプールに行きたいな」という気分になるような水着なんです。デザインは大胆で、シンプルな柄がとても鮮やかで気に入っています♪

私自身、せふれさんを探してて、楽しく会える人がいいです！せっかくなので、気に入った水着を見てもらえたら嬉しいなと思い、こちらに投稿しました。

もし興味があって、私とメッセージ交換してもいいよと思ってくださったら、お返事をいただけるとうれしいです。写真を添付して送らせていただきます。

それでは、返信を待ってますね。よろしくお願いします♪"""
  return_foot_img = "/Users/yamamotokenta/Documents/Pictures/キャラ画像/kumi_mizugi.jpeg"
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)

  try:   
    happymail.return_footpoint(name, setting.kumi_happy_windowhandle, driver, return_foot_message, cnt, return_foot_img)
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
  h_foot(cnt)