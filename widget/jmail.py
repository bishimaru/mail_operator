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
import traceback
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import func
from selenium.webdriver.support.select import Select
import sqlite3
import re
from datetime import datetime, timedelta
import difflib
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


def login_jmail(driver, wait, login_id, login_pass):
  driver.delete_all_cookies()
  # https://mintj.com/msm/login/?adv=___36h1tmot02r12l8kxdtxx0b3z
  driver.get("https://mintj.com/msm/login/")
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  wait_time = random.uniform(3, 6)
  time.sleep(2)
  id_form = driver.find_element(By.ID, value="loginid")
  id_form.send_keys(login_id)
  pass_form = driver.find_element(By.ID, value="pwd")
  pass_form.send_keys(login_pass)
  time.sleep(1)
  send_form = driver.find_element(By.ID, value="B1login")
  try:
    send_form.click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(1)
  except TimeoutException as e:
    print("TimeoutException")
    driver.refresh()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(2)
    id_form = driver.find_element(By.ID, value="loginid")
    id_form.send_keys(login_id)
    pass_form = driver.find_element(By.ID, value="pwd")
    pass_form.send_keys(login_pass)
    time.sleep(1)
    send_form = driver.find_element(By.ID, value="B1login")
    send_form.click()

def re_post(driver, name):
  try:
    wait = WebDriverWait(driver, 15)
    dbpath = 'firstdb.db'
    conn = sqlite3.connect(dbpath)
    # SQLiteを操作するためのカーソルを作成
    cur = conn.cursor()
    # 順番
    # データ検索  
    cur.execute('SELECT * FROM jmail WHERE name = ?', (name,))
    for row in cur:
        # print(6666)
        # print(row)
        login_id = row[2]
        login_pass = row[3]
        post_title = row[4]
        post_content = row[5]
    login_jmail(driver, wait, login_id, login_pass)
    # メニューをクリック
    menu_icon = driver.find_elements(By.CLASS_NAME, value="menu-off")
    menu_icon[0].click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(2)
    #  アダルト掲示板をクリック
    menu = driver.find_elements(By.CLASS_NAME, value="iconMenu")
    adult_post_menus = menu[0].find_elements(By.TAG_NAME, value="p")
    adult_post_menu = adult_post_menus[0].find_elements(By.XPATH, "//*[contains(text(), 'アダルト掲示板')]")
    adult_post_menu_link = adult_post_menu[0].find_element(By.XPATH, "./.")
    #  adult_post_menu_link.click()
    driver.get(adult_post_menu_link.get_attribute("href"))
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(2)
    #  投稿をクリック　color_variations_03
    post_icon = driver.find_elements(By.CLASS_NAME, value="color_variations_03")
    post_icon[0].click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(2)
    #  コーナーを選択
    corner_select = driver.find_elements(By.NAME, value="CornerId")
    select = Select(corner_select[0])
    select.select_by_visible_text("今すぐあそぼっ")
    time.sleep(1)
    #  件名を入力
    post_title_input = driver.find_elements(By.NAME, value="Subj")
    post_title_input[0].clear()
    post_title_input[0].send_keys(post_title)
    time.sleep(1)
    #  メッセージを入力
    post_content_input = driver.find_elements(By.NAME, value="Comment")
    post_content_input[0].clear()
    post_content_input[0].send_keys(post_content)
    time.sleep(1)
    #  メール受信数を選択　Number of emails received
    select_recieve_number = driver.find_elements(By.NAME, value="ResMaxCount")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", select_recieve_number[0])
    time.sleep(1)
    select = Select(select_recieve_number[0])
    select.select_by_visible_text("5件")
    time.sleep(1)
    #  書き込む
    write_button = driver.find_elements(By.NAME, value="Bw")
    write_button[0].click()
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    time.sleep(1)

    return True
  except Exception as e:
    print(f"掲示板再投稿エラー{name}")    
    return False


def check_new_mail(driver, wait, name):
  return_list = []
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  cur = conn.cursor()
  cur.execute('SELECT login_id, login_passward, fst_message, return_foot_message, second_message FROM jmail WHERE name = ?', (name,))
  login_id = None
  for row in cur:
    login_id = row[0]
    login_pass = row[1]
    fst_message = row[2]
    return_foot_message = row[3]
    second_message = row[4]
  if login_id == None or login_id == "":
    print(f"{name}のjmailキャラ情報を取得できませんでした")
    return 1, 0
  login_jmail(driver, wait, login_id, login_pass)
  # メールアイコンをクリック
  mail_icon = driver.find_elements(By.CLASS_NAME, value="mail-off")
  link = mail_icon[0].find_element(By.XPATH, "./..")
  driver.get(link.get_attribute("href"))
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(2)
  interacting_user_list = []
  interacting_users = driver.find_elements(By.CLASS_NAME, value="icon_sex_m")
  # 未読メールをチェック
  send_count = 0
  for interacting_user_cnt in range(len(interacting_users)):
    # interacting_userリストを取得
    interacting_user_name = interacting_users[interacting_user_cnt].text
    if "未読" in interacting_user_name:
      interacting_user_name = interacting_user_name.replace("未読", "")
    if "退会" in interacting_user_name:
      interacting_user_name = interacting_user_name.replace("退会", "")
    if " " in interacting_user_name:
      interacting_user_name = interacting_user_name.replace(" ", "")
    if "　" in interacting_user_name:
      interacting_user_name = interacting_user_name.replace("　", "")
    # 未読、退会以外でNEWのアイコンも存在してそう
    interacting_user_list.append(interacting_user_name)
    # NEWアイコンがあるかチェック
    new_icon = interacting_users[interacting_user_cnt].find_elements(By.TAG_NAME, value="img")
    if "未読" in interacting_users[interacting_user_cnt].text or len(new_icon):
    # deug
    # if "masa" in interacting_users[interacting_user_cnt].text:
      # 時間を取得　align_right
      parent_usr_info = interacting_users[interacting_user_cnt].find_element(By.XPATH, "./..")
      parent_usr_info = parent_usr_info.find_element(By.XPATH, "./..")
      next_element = parent_usr_info.find_element(By.XPATH, value="following-sibling::*[1]")
      current_year = datetime.now().year
      date_string = f"{current_year} {next_element.text}"
      date_format = "%Y %m/%d %H:%M" 
      date_object = datetime.strptime(date_string, date_format)
      now = datetime.today()
      
      elapsed_time = now - date_object
      print(interacting_users[interacting_user_cnt].text)
      print(f"メール到着からの経過時間{elapsed_time}")
      if elapsed_time >= timedelta(minutes=4):
        print("4分以上経過しています。")
        send_message = ""
        # リンクを取得
        link_element = interacting_users[interacting_user_cnt].find_element(By.XPATH, "./..")
        driver.get(link_element.get_attribute("href"))
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(2)

        # 受信メッセージにメールアドレスが含まれていれば条件文を送信
        send_by_user = driver.find_elements(By.CLASS_NAME, value="balloon_left")
        send_by_user_message = send_by_user[0].find_elements(By.CLASS_NAME, value="balloon")[0].text
        # メールアドレスを抽出する正規表現
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        email_list = re.findall(email_pattern, send_by_user_message)
        if email_list:
          print("メールアドレスが含まれています")
          print(email_list)
          # icloudの場合
          if "icloud.com" in send_by_user_message:
            print("icloud.comが含まれています")
            icloud_text = "メール送ったんですけど、ブロックされちゃって届かないのでこちらのアドレスにお名前添えて送ってもらえますか？"
            dbpath = 'firstdb.db'
            conn = sqlite3.connect(dbpath)
            # # SQLiteを操作するためのカーソルを作成
            cur = conn.cursor()
            # # 順番
            # # データ検索
            cur.execute('SELECT mail_address FROM jmail WHERE name = ?', (name,))
            for row in cur:
                mail_address = row[0]
            send_message = icloud_text + "\n" + mail_address
          # gmailで条件文を送信
          else:
            for user_address in email_list:
              dbpath = 'firstdb.db'
              conn = sqlite3.connect(dbpath)
              # # SQLiteを操作するためのカーソルを作成
              cur = conn.cursor()
              # # 順番
              # # データ検索
              cur.execute('SELECT condition_message, gmail_password, mail_address FROM jmail WHERE name = ?', (name,))
              for row in cur:
                  text = row[0]
                  password = row[1]
                  mailaddress = row[2]
              
              func.send_conditional(interacting_user_name, user_address, mailaddress, password, text)
            interacting_users = driver.find_elements(By.CLASS_NAME, value="icon_sex_m")
            continue
          
        # 相手からのメッセージが何通目か確認する
        send_by_me = driver.find_elements(By.CLASS_NAME, value="balloon_right")
        if len(send_by_me) == 0:
          send_message = fst_message
        elif len(send_by_me) == 1:
          send_message = second_message
        elif second_message in send_by_me[0].text:
          print("捨てメアドに通知")
          print(f"{name}   {login_id}  {login_pass} : {interacting_user_name}  ;;;;{send_by_user_message}")
          return_message = f"{name}jmail,{login_id}:{login_pass}\n{interacting_user_name}「{send_by_user_message}」"
          return_list.append(return_message)
          print("捨てメアドに、送信しました")

        if send_message:
          # 返信するをクリック
          res_do = driver.find_elements(By.CLASS_NAME, value="color_variations_05")
          res_do[1].click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(2)
          # メッセージを入力　name=comment
          text_area = driver.find_elements(By.NAME, value="comment")
          text_area[0].send_keys(send_message)
          time.sleep(4)
          # 画像があれば送信
          send_button = driver.find_elements(By.NAME, value="sendbutton")
          send_button[0].click()
          wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
          time.sleep(2)
        # メール一覧に戻る　message_back
        back_parent = driver.find_elements(By.CLASS_NAME, value="message_back")
        back = back_parent[0].find_elements(By.TAG_NAME, value="a")
        back[0].click()
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(2)
        interacting_users = driver.find_elements(By.CLASS_NAME, value="icon_sex_m")

  # # あしあと返し
  #メニューをクリック
  menu_icon = driver.find_elements(By.CLASS_NAME, value="menu-off")
  menu_icon[0].click()
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(2)
  menu = driver.find_elements(By.CLASS_NAME, value="iconMenu")
  #足跡をクリック
  foot_menus = menu[0].find_elements(By.TAG_NAME, value="p")
  foot_menu = foot_menus[0].find_elements(By.XPATH, "//*[contains(text(), 'あしあと')]")
  foot_menu_link = foot_menu[0].find_element(By.XPATH, "./..")
  driver.get(foot_menu_link.get_attribute("href"))
  wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
  time.sleep(2)
  # interacting_user_listになければ足跡返す
  name_element = driver.find_elements(By.CLASS_NAME, value="icon_sex_m")
  for foot_return_cnt in range(len(name_element)):
    print("足跡リストのユーザーがメールリストになければ足跡を返す")
    print(name_element[foot_return_cnt].text)
    print("メールリストのユーザーリスト")
    print(interacting_user_list)
    foot_user_name = name_element[foot_return_cnt].text
    if foot_user_name not in interacting_user_list:
      print(f"{foot_user_name}はメールリストになかった")
      foot_user_link = name_element[foot_return_cnt].find_element(By.XPATH, "./..")
      driver.get(foot_user_link.get_attribute("href"))
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(2)
      text_area = driver.find_elements(By.ID, value="textarea")
      driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", text_area[0])
      time.sleep(1)
      text_area[0].send_keys(return_foot_message)
      time.sleep(4)
      send_btn = driver.find_elements(By.CLASS_NAME, value="send_btn")
      send_btn[0].click()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(2)
      interacting_user_list.append(foot_user_name)

      # あしあとリストに戻る
      driver.back()
      wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
      time.sleep(2)
      name_element = driver.find_elements(By.CLASS_NAME, value="icon_sex_m")





  if len(return_list):
    return return_list, send_count
  else:
    return 1, send_count

   

   
   