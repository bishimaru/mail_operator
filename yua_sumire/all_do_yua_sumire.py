import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import setting
sys.path.append(setting.yua_sumire_path)
import h_foot
import p_foot
import post
import time


def do_post_foot(h_cnt, p_cnt):
    start_time = time.time() 
    post.repost_happymail_pcmax()
    while True:
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      if elapsed_time >= 420:
        start_time = time.time() 
        h_foot.h_foot(h_cnt)
        p_foot.p_foot(p_cnt)
        break
      else:
        time.sleep(10)
    return True

if __name__ == '__main__':
  if len(sys.argv) < 2:
    h_cnt = 20
    p_cnt = 10
  elif len(sys.argv) == 2:
    h_cnt = int(sys.argv[1])
    p_cnt = 10
  else:
    h_cnt = int(sys.argv[1])
    p_cnt = int(sys.argv[2])
  do_post_foot(h_cnt, p_cnt)