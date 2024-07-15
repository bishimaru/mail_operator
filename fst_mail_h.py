from widget import happymail
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from selenium.webdriver.support.ui import WebDriverWait
import traceback
from widget import pcmax, happymail, func
import sqlite3
from selenium.webdriver.chrome.service import Service
from datetime import timedelta
from datetime import datetime


def fst_mail_hm(end_hour, end_minute):
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--incognito")
  options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
  options.add_argument("--no-sandbox")
  options.add_argument("--window-size=456,912")
  # options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  options.add_argument("--disable-cache")
  service = Service(executable_path=ChromeDriverManager().install())
  driver = webdriver.Chrome(options=options, service=service)
  wait = WebDriverWait(driver, 15)
  name_list = [
    # "アスカ", 
    "いおり",
    "えりか", "くみ",
    "さな", "すい", "つむぎ", 
    "はづき", "ハル", 
    "りな", "めあり",
    "りこ", "ゆうな","ゆっこ",
    "わかな",
    
  ]
  happy_user_list = []
  wait_time = random.uniform(2, 5)
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  # # SQLiteを操作するためのカーソルを作成
  cur = conn.cursor()
  # # 順番
  # # データ検索
  cur.execute('SELECT name, login_id, passward, fst_message, mail_img FROM happymail')
  for row in cur:
      if row[0] in name_list:
      
        happy_user_list.append(row)
  while True:
    # 現在時刻を取得
    current_time = datetime.now()
    if current_time.hour > int(end_hour) or (current_time.hour == int(end_hour) and current_time.minute >= int(end_minute)):
        print("終了時刻を過ぎました。")
        driver.quit()  
        return
    else:
        print("現在時刻:", current_time)
    try:
      happymail.send_fst_message(happy_user_list, driver, wait)
    except Exception as e:
      print(traceback.format_exc())

    


if __name__ == '__main__':
  
  end_hour = sys.argv[1]
  end_minute = sys.argv[2]
  fst_mail_hm(end_hour, end_minute)
    