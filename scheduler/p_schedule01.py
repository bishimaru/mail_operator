from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, time, timedelta
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail, func
import h_footprint1
import sb_h_day_shift
import s_check_mail_hpj
from fst_mail_pcmax import template_multiple_fst_mail, chara_order_fstmail
from datetime import datetime, timedelta



def tick():
    print("Tick! The time is : %s'" % datetime.now())

if __name__ == '__main__':
    scheduler = BlockingScheduler()  # スケジューラを作る

    # fst_mail
    chara_name_list = {
     "アスカ":{},"あやか":{},"いおり":{},
    "えりか":{}, "きりこ":{},"すい":{}, 
    "さな":{},  "つむぎ":{},"なお":{}, 
    }
    
    # 朝のジョブ
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=8, minute=50, args=[1, chara_name_list, 10, 0],  misfire_grace_time=60*60)
    # 昼のジョブ
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=13, minute=15, args=[1, chara_name_list, 14, 15],  misfire_grace_time=60*60)
    # 夜のジョブ
    scheduler.add_job(chara_order_fstmail.main, 'cron', hour=17, minute=0, args=[1, chara_name_list, 21, 30], misfire_grace_time=60*60)
    print("Press Ctrl+{0} to exit.".format('Break' if os.name == 'nt' else 'C'))
    
    try:
        scheduler.start()  # スタート
    except (KeyboardInterrupt, SystemExit):
        pass