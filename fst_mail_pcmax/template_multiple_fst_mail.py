import pcmax
import sys
import sqlite3
from concurrent.futures import ThreadPoolExecutor
# 〜〜〜〜〜〜キャラ情報〜〜〜〜〜〜
# name = "ゆりあ"
# login_id = "18983588"
# login_pass = "6667"
# fst_message = """初めまして！ゆりあって言います♪
# 都内で不動産関係のOLをしています！

# 仕事に少し慣れてきたこともあり、仕事終わりにお家に帰ると人肌恋しさを感じるようになってきました(>_<)
# いっぱいいちゃいちゃできるようなせふれさんとここで出会えたらいいなって思ってます( ´ ▽ ` )

# 同じように人肌恋しいって感じたことありませんか？？"""
# fst_message_img = ""

# 〜〜〜〜〜〜検索設定〜〜〜〜〜〜

# メール送信数（上限なしは0）
limit_send_cnt = 0
# 地域選択（3つまで選択可能）
select_areas = [
  "東京都",
  # "千葉県",
  "埼玉県",
  "神奈川県",
  # "静岡県",
  # "新潟県",
  # "山梨県",
  # "長野県",
  # "茨城県",
  # "栃木県",
  # "群馬県",
]
# 年齢選択（最小18歳、最高60以上）
youngest_age = "19"
oldest_age = "36"
# NGワード（複数、追加可能）
ng_words = [
  "通報",
  "業者",
  "食事",
  "お茶",
  "円",
  "パパ",
  "援",
  "援交",
  "お金のやり取り",
]

maji_soushin = False
if len(sys.argv) == 2:
  if sys.argv[1] == str(1):
    maji_soushin = True
  elif sys.argv[1] == str(0):
    maji_soushin = False
elif len(sys.argv) >= 3:
  print("引数を正しく入力してください")

# sqlite用コード〜〜〜〜〜〜〜〜〜〜〜〜〜〜
if len(sys.argv) == 3:
  name = sys.argv[2]
  if sys.argv[1] == str(1):
    maji_soushin = True
  elif sys.argv[1] == str(0):
    maji_soushin = False
elif len(sys.argv) > 3:
  print("引数を正しく入力してください")

chara_name_list = {
  "ももか":{}, "きりこ":{}, "りこ":{},
}

dbpath = 'firstdb.db'
conn = sqlite3.connect(dbpath)
# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()
# 順番
# データ検索
for chara_name in chara_name_list:
  cur.execute('SELECT * FROM pcmax WHERE name = ?', (chara_name,))
  for row in cur:
      # print("キャラ情報")
      # print(row)
      chara_name_list[chara_name]["login_id"] = row[2]
      chara_name_list[chara_name]["login_pass"] = row[3]
      chara_name_list[chara_name]["fst_message"] = row[5]
      chara_name_list[chara_name]["fst_message_img"] = row[6]
      chara_name_list[chara_name]["second_message"] = row[9]
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜sqlite用コード「
# print(chara_name_list)

def main():
  with ThreadPoolExecutor(max_workers=3) as executor:

    if 3 < len(select_areas):
      print("選択地域は3つまでです。")
      return
    
    names = list(chara_name_list.keys())
    if len(names) == 4:
      executor.submit(pcmax.send_fst_mail, names[0], chara_name_list[names[0]]["login_id"], chara_name_list[names[0]]["login_pass"], chara_name_list[names[0]]["fst_message"], chara_name_list[names[0]]["fst_message_img"], chara_name_list[names[0]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
      executor.submit(pcmax.send_fst_mail, names[1], chara_name_list[names[1]]["login_id"], chara_name_list[names[1]]["login_pass"], chara_name_list[names[1]]["fst_message"], chara_name_list[names[1]]["fst_message_img"], chara_name_list[names[1]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
      executor.submit(pcmax.send_fst_mail, names[2], chara_name_list[names[2]]["login_id"], chara_name_list[names[2]]["login_pass"], chara_name_list[names[2]]["fst_message"], chara_name_list[names[2]]["fst_message_img"], chara_name_list[names[2]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
      executor.submit(pcmax.send_fst_mail, names[3], chara_name_list[names[3]]["login_id"], chara_name_list[names[3]]["login_pass"], chara_name_list[names[3]]["fst_message"], chara_name_list[names[3]]["fst_message_img"], chara_name_list[names[3]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
    elif len(names) == 3:
      executor.submit(pcmax.send_fst_mail, names[0], chara_name_list[names[0]]["login_id"], chara_name_list[names[0]]["login_pass"], chara_name_list[names[0]]["fst_message"], chara_name_list[names[0]]["fst_message_img"], chara_name_list[names[0]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
      executor.submit(pcmax.send_fst_mail, names[1], chara_name_list[names[1]]["login_id"], chara_name_list[names[1]]["login_pass"], chara_name_list[names[1]]["fst_message"], chara_name_list[names[1]]["fst_message_img"], chara_name_list[names[1]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
      executor.submit(pcmax.send_fst_mail, names[2], chara_name_list[names[2]]["login_id"], chara_name_list[names[2]]["login_pass"], chara_name_list[names[2]]["fst_message"], chara_name_list[names[2]]["fst_message_img"], chara_name_list[names[2]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
    elif len(names) == 2:
      executor.submit(pcmax.send_fst_mail, names[0], chara_name_list[names[0]]["login_id"], chara_name_list[names[0]]["login_pass"], chara_name_list[names[0]]["fst_message"], chara_name_list[names[0]]["fst_message_img"], chara_name_list[names[0]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
      executor.submit(pcmax.send_fst_mail, names[1], chara_name_list[names[1]]["login_id"], chara_name_list[names[1]]["login_pass"], chara_name_list[names[1]]["fst_message"], chara_name_list[names[1]]["fst_message_img"], chara_name_list[names[1]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
    elif len(names) == 1:
      executor.submit(pcmax.send_fst_mail, names[0], chara_name_list[names[0]]["login_id"], chara_name_list[names[0]]["login_pass"], chara_name_list[names[0]]["fst_message"], chara_name_list[names[0]]["fst_message_img"], chara_name_list[names[0]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt)
    else:
      print("キャラ数を正しく取得できませんでした")
      
if __name__ == '__main__':
  main()