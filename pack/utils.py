'''
/*
** create by `@d1y` in 2019-09-17
** 公共方法
*/
'''

import os

def load_langs(lang = 'cn'):
  '''
  ** @tips 加载语言设置
  ** @param <str> - lang
  ** @return <dict>
  '''
  current_path = os.path.abspath('./pack/config/lang')