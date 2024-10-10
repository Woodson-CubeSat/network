from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pickle
from general_db.common.constants import script_dir

web = webdriver.Chrome()

#fix this function later
def loadCookies():

     with open(f"{script_dir}/satnogs_cookies", 'rb') as cookiesfile:
         cookies = pickle.load(cookiesfile)
         print("loaded cookies")
         for cookie in cookies:
            print("adding cookie")
            web.add_cookie(cookie)

#fix this function later, and add it to user side
def saveCookies():
    #it only works if you get cookies with firefox
    firefox = webdriver.Firefox()
    #get website and wait for you to enter username and password
    firefox.get('https://db.satnogs.org/')
    time.sleep(30)
    #save cookies
    # with open(f"{script_dir}/satnogs_cookies", 'wb') as filehandler:
    #     pickle.dump(firefox.get_cookies(), filehandler)

    print(firefox.get_cookies)





def clicker(norad_id:int):
    norad_id = str(norad_id)
    web.get('https://db.satnogs.org/')
    time.sleep(1)
    loadCookies()
    web.get('https://db.satnogs.org/')
    time.sleep(1)
    search_box = web.find_element(By.ID, "search")
    search_box.send_keys(norad_id + Keys.RETURN)
    time.sleep(1)
    web.find_element(By.ID, "data-tab").click()
    time.sleep(1)
    web.find_element(By.LINK_TEXT, "Everything").click()
    time.sleep(1)


saveCookies()