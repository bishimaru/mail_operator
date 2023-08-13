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
  name = "あすか"
  return_foot_message = """足跡が付いてたので気になってご連絡しちゃいました♪
あすかです٩( 'ω’ )و
友達のゆかと3人でエッチを楽しめるセフレさんを見つけたくてサイトに登録しました！

2人ともメンズ専門の脱毛サロンで働いてるんですけど、毎回VIOの施術中にエッチな気分になっちゃって(//ω照♥

私もゆかも今は特定の相手もいないし、折角なら3人でエッチを楽しめるセフレさんが出来たらなって思ってるんですけど今ってそういうお相手探してたりしませんか？？"""
  relative_path = os.path.join(setting.BASE_DIR, setting.asuka_yuka_picture_path)
  h_return_foot_img = relative_path
  p_return_foot_img = "230813"
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