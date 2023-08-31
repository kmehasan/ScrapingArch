from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import os
from selenium.webdriver.chrome.service import Service
class Browser:
    def getChromeBrowser():
        service = Service()
        isExist = os.path.exists('chrome_user_dir')
        if not isExist:
            os.makedirs('chrome_user_dir')
            print("Create new session for chromes")
        options = Options()
        # options.headless = True
        options.add_argument('--user-data-dir=chrome_user_dir')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(service=service, options=options)
        

