import bs4
import traceback
import re
import time
import mojimoji
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# ChromeDriverのフルパス
CHROMEDRIVER_PATH = "C:\\Users\\shouy\\Desktop\\Tools\\chromedriver.exe"
# 遷移間隔(秒)
INTERVAL_TIME = 3
# ヘッドレスモード
IS_HEADLESS = True

# ドライバー準備
def get_driver():
    if (IS_HEADLESS):
        # ヘッドレスモードでブラウザを起動
        options = Options()
        options.add_argument('--headless')

        # ブラウザを起動
        driver = webdriver.Chrome(CHROMEDRIVER_PATH,options=options)
    else:
        driver = webdriver.Chrome(CHROMEDRIVER_PATH)
    
    return drive

if __name_=="__main__":
    # ブラウザのdriver取得
    driver = get_driver()

