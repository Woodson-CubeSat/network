from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from common.constants import script_dir
import time
import subprocess
import pickle
import base64
#from general_db.common.constants import script_dir

script_dir = str(subprocess.check_output(["pwd"])).replace("b'", "").replace("n'", "")[:-1]

# For testing only
#fix this function later, and add it to user side
def saveCookies():
    #it only works if you get cookies with firefox
    firefox = webdriver.Firefox()
    #get website and wait for you to enter username and password
    firefox.get('https://db.satnogs.org/')
    print('got here')
    time.sleep(30)
    #save cookies
    with open(f"{script_dir}/satnogs_cookies", 'wb') as filehandler:
        print(f"{script_dir}/satnogs_cookies")
        pickle.dump(firefox.get_cookies(), filehandler)
    for cookie in firefox.get_cookies():
        print(cookie)

    print(firefox.get_cookies())

class Webbot:
        
    def __init__(self):
        self.web = webdriver.Chrome()

    def encodeCookies(self):
        with open(f"{script_dir}/satnogs_cookies", 'rb') as file:
            blobData = file.read()
            print(blobData)
            # encode bin object into base64 and turn resulting bytestring into str
            final_str = str(base64.encodebytes(blobData), 'utf-8')
            print("\n"+final_str)
        return final_str

    def loadCookies(self, cookiestring):
        # decode from string
        cookies = base64.decodebytes(bytes(cookiestring, 'utf-8'))
        #print("\n\n cookies: "+cookies)
        loaded_cookies = pickle.loads(cookies)
        print(loaded_cookies)
        for cookie in loaded_cookies:
            print(cookie)
            print("adding cookie")
            self.web.add_cookie(cookie)
    



    def clicker(self, norad_id:int, satnogs_cookies: str):
        norad_id = str(norad_id)
        self.web.get('https://db.satnogs.org/')
        print('hi')
        time.sleep(1)
        self.loadCookies(satnogs_cookies)
        self.web.get('https://db.satnogs.org/')
        time.sleep(1)
        search_box = self.web.find_element(By.ID, "search")
        search_box.send_keys(norad_id + Keys.RETURN)
        time.sleep(1)
        self.web.find_element(By.ID, "data-tab").click()
        time.sleep(1)
        self.web.find_element(By.LINK_TEXT, "Everything").click()
        time.sleep(1)
#cookiestring = encodeCookies()

#clicker(25544, cookiestring)

#saveCookies()
    




# #fix this function later
# # def loadCookies():

# #      with open(f"{script_dir}/satnogs_cookies", 'rb') as cookiesfile:
# #          cookies = pickle.load(cookiesfile)
# #          print("loaded cookies")
# #          for cookie in cookies:
# #             print("adding cookie")
# #             web.add_cookie(cookie)

#     script_dir = str(subprocess.check_output(["pwd"])).replace("b'", "").replace("n'", "")[:-1]
# """
# with open(f"{script_dir}/satnogs_cookies", 'rb') as cookiesfile:
#          cookies = pickle.load(cookiesfile)
#          print("loaded cookies")
#          print(cookies)
#          for cookie in cookies:
#             print(cookie)"""

#     # for testing only