from __future__ import print_function
from __future__ import division

import pymysql
import pandas as pd
import logging
import sys
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

pd.options.mode.chained_assignment = None

sql = """
      SELECT pday, clazz, tag, expo_rate, rate, duration_avg, v_duration_avg, ev_avg, pv_avg, vv_avg,
      article_cnt, ev, euv, pv, uv, vv, vuv, share, share_rate, store, store_rate, comment, comment_rate
      FROM datarubik.global_classified_category
      where pday = '{0}' and tag_clazz = '{1}' 
      and stat_source = {2} and data_type = 'newsapp' and rec_channel = 'headline' and requester = 'ifengnews'
      and clazz_type = 'item_type' 
      order by case clazz when 'docpic' then 0 when 'video' then 1 when 'slide' then 2 else 3 end asc, clazz, rate desc;
      """


def download(pday, base_path):
    db = pymysql.connect("10.90.3.183", "mysql", "ifeng1001", "datarubik", charset="utf8")
    try:
        for s in ['0', '1', '-1314']:
            for c in ['c', 'sc']:
                df = pd.read_sql(sql.format(pday, c, s), db)
                df['pday'] = df['pday'].map(lambda x: x.strftime("%Y%m%d"))
                path = os.path.join(base_path, '{0}_{1}.csv'.format(c, s))
                df.to_csv(path, sep=',', index=False, encoding='utf-8', header=False)
    except Exception:
        import traceback
        logging.error(traceback.format_exc())
        exit(1)
    finally:
        db.close()


if __name__ == '__main__':
    pday = sys.argv[1]
    base_path = sys.argv[2]
    download(pday, base_path)
