# import required modules
from email import message
from typing import Iterator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import schedule
import logging
import selenium


from utils import *

# create chrome instance
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_argument("--use-fake-device-for-media-stream")
opt.add_argument("--use-fake-ui-for-media-stream")

opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=opt)

#################################################################
meet_url = 'https://meet.google.com/kbp-jdcg-ncz'

mail_address = ''
password = ''
target = ["7", "簽到"]
outputmessage = "hello"
##################################################################

Glogin(driver, mail_address, password)
driver.get(meet_url)
driver.refresh()

turnOffMicCam(driver)

joinNow(driver)

openChat(driver)

logging.basicConfig()
schedule_logger = logging.getLogger("schedule")
schedule_logger.setLevel(level = logging.DEBUG)

# schedule.every().day.at("08:02").do(sendMessage, driver=driver, message=outputmessage)
# schedule.every().day.at("09:02").do(sendMessage, driver=driver, message=outputmessage)
# schedule.every().day.at("10:12").do(sendMessage, driver=driver, message=outputmessage)
# schedule.every().day.at("11:12").do(sendMessage, driver=driver, message=outputmessage)
# schedule.every().day.at("13:02").do(sendMessage, driver=driver, message=outputmessage)
# schedule.every().day.at("14:02").do(sendMessage, driver=driver, message=outputmessage)
# schedule.every().day.at("15:02").do(sendMessage, driver=driver, message=outputmessage)

last = 0
while True:
    try:
        schedule.run_pending()
        chats = getChatMessage(driver)
        # print(chats)
        cur = len(chats)
        if cur > last:
            print(chats, last, cur)
            for content in chats[last:cur] :
                if content in target:
                    sendMessage(driver, outputmessage)
        last = cur
        if driver.session_id == None :
            break
        
        # time.sleep(10)
    except selenium.common.exceptions.StaleElementReferenceException:
        print("error")