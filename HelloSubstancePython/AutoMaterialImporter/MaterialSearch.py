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

# ChromeDriver�̃t���p�X
CHROMEDRIVER_PATH = "C:\\Users\\shouy\\Desktop\\Tools\\chromedriver.exe"
# �J�ڊԊu(�b)
INTERVAL_TIME = 3
# �w�b�h���X���[�h
IS_HEADLESS = True

# �h���C�o�[����
def get_driver():
    if (IS_HEADLESS):
        # �w�b�h���X���[�h�Ńu���E�U���N��
        options = Options()
        options.add_argument('--headless')

        # �u���E�U���N��
        driver = webdriver.Chrome(CHROMEDRIVER_PATH,options=options)
    else:
        driver = webdriver.Chrome(CHROMEDRIVER_PATH)
    
    return drive

if __name_=="__main__":
    # �u���E�U��driver�擾
    driver = get_driver()

