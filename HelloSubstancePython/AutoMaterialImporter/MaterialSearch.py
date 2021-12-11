import bs4
import traceback
import re
import time
import mojimoji
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    
    return driver

if __name__=="__main__":
    # ブラウザのdriver取得
    driver = get_driver()

    driver.get('https://www.google.com/')
    print(driver.title)

    # driverを閉じる
    driver.quit()
