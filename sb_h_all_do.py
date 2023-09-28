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
from widget import pcmax, happymail, func
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback
from datetime import timedelta
from sb_h_repost_return_foot import sb_h_repost_returnfoot

def sb_h_all_do(cnt, return_foot_cnt):
  chara_order = [
    "あすか", "彩香", "えりか", "きりこ", "波留（はる）", "めあり", "ももか", "りこ", "りな", "ゆうこ", "ハル",
  ]
  chara_order = [
    "きりこ", 
  ]
  def timer(sec, functions):
    start_time = time.time() 
    for func in functions:
      func()
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    while elapsed_time < sec:
      time.sleep(5)
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      # print(elapsed_time)
  wait_cnt = 7200 / len(chara_order)

  while cnt:

    start_one_rap_time = time.time() 
    for chara in chara_order:
      try:
        timer(wait_cnt, [lambda: sb_h_repost_returnfoot(chara, return_foot_cnt)])
      except Exception as e:
        print(f"エラー{chara}")
        print(traceback.format_exc())
    elapsed_time = time.time() - start_one_rap_time  
    while elapsed_time < 7200:
      time.sleep(300)
      elapsed_timedelta = timedelta(seconds=elapsed_time)
      elapsed_time_formatted = str(elapsed_timedelta)
      print(f"<<<<<<<<<<<<<サイト回し一周タイム： {elapsed_time_formatted}>>>>>>>>>>>>>>>>>>")
    cnt -= 1

if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 1
    return_foot_cnt = 22
  elif len(sys.argv) >= 2:
    cnt = int(sys.argv[1])
    return_foot_cnt = int(sys.argv[2])

  sb_h_all_do(cnt, return_foot_cnt)