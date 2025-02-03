import os
import time
import pickle
import base64
#from common.constants import script_dir
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

script_dir = os.getcwd()

def saveCookies():
    """ Open a website, let the user log in, and save cookies for future use. """
    firefox = webdriver.Firefox(service=FirefoxService())

    firefox.get('https://db.satnogs.org/')
    print('Waiting for login...')
    time.sleep(30)  # Wait for user login (improve this later)

    # Save cookies after login
    cookie_path = f"{script_dir}/satnogs_cookies"
    with open(cookie_path, 'wb') as filehandler:
        pickle.dump(firefox.get_cookies(), filehandler)
    
    print(f"Cookies saved to: {cookie_path}")
    firefox.quit()

class Webbot:
    def __init__(self):
        """ Initializes WebDriver for Chrome """
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Optional: Run in the background
        chrome_options.add_argument("--disable-gpu")  # Helps in headless mode
        chrome_options.add_argument("--no-sandbox")  # Helps in some environments
        self.web = webdriver.Chrome(service=Service(), options=chrome_options)

    def encodeCookies(self):
        """ Encode cookies as a base64 string """
        with open(f"{script_dir}/satnogs_cookies", 'rb') as file:
            blobData = file.read()
            final_str = base64.b64encode(blobData).decode('utf-8')
        return final_str

    def loadCookies(self, cookiestring):
        """ Load and set cookies from a base64-encoded string """
        cookies = base64.b64decode(cookiestring.encode('utf-8'))
        loaded_cookies = pickle.loads(cookies)

        for cookie in loaded_cookies:
            print(f"Adding cookie: {cookie}")
            self.web.add_cookie(cookie)

    def clicker(self, norad_id: int, satnogs_cookies: str):
        """ Automates website navigation and data clicking """
        norad_id = str(norad_id)
        self.web.get('https://db.satnogs.org/')

        # Wait for page to load before adding cookies
        WebDriverWait(self.web, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        self.loadCookies(satnogs_cookies)  # Load cookies

        # Refresh to apply cookies
        self.web.get('https://db.satnogs.org/')
        WebDriverWait(self.web, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        search_box = self.web.find_element(By.ID, "search")
        search_box.send_keys(norad_id + Keys.RETURN)

        # Wait and click on the "Data" tab
        WebDriverWait(self.web, 5).until(
            EC.element_to_be_clickable((By.ID, "data-tab"))
        ).click()

        # Wait and click on "Everything"
        WebDriverWait(self.web, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Everything"))
        ).click()
