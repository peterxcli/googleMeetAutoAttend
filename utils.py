# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def Glogin(driver, mail_address, password):
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)

    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)

    driver.get('https://google.com/')
    driver.implicitly_wait(100)


def turnOffMicCam(driver):
    time.sleep(5)
    driver.implicitly_wait(2000)
    xpath_btn = '/html/body/div[1]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div[1]'
    driver.find_element_by_xpath(xpath_btn).click()
    driver.implicitly_wait(2000)
    xpath_btn = '/html/body/div[1]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div[1]'
    driver.find_element_by_xpath(xpath_btn).click()
    driver.implicitly_wait(2000)


def joinNow(driver):
    time.sleep(5)
    driver.implicitly_wait(2000)
    xpath_btn = '/html/body/div[1]/c-wiz/div/div/div[10]/div[3]/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/button'
    driver.find_element_by_xpath(xpath_btn).click()
    driver.implicitly_wait(2000)


def AskToJoin(driver):
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()


def openChat(driver):
    driver.implicitly_wait(2000)
    xpath_btn = '/html/body/div[1]/c-wiz/div[1]/div/div[10]/div[3]/div[10]/div[3]/div[3]/div/div/div[3]/span/button'
    btn = driver.find_element_by_xpath(xpath_btn)
    btn.click()
    driver.implicitly_wait(2000)


def sendMessage(driver, message):
    driver.implicitly_wait(2000)
    x_path = '/html/body/div[1]/c-wiz/div[1]/div/div[10]/div[3]/div[4]/div[2]/div[2]/div/div[5]/div/label/textarea'
    t_box = driver.find_element_by_xpath(x_path)
    # sending messages.
    t_box.send_keys(message, Keys.ENTER)
    driver.implicitly_wait(2000)

def getChatMessage(driver) :
    ret = []
    xpath = '/html/body/div[1]/c-wiz/div[1]/div/div[10]/div[3]/div[4]/div[2]/div[2]/div/div[3]'
    header = driver.find_element_by_xpath(xpath)
    sub_header = header.find_elements(By.XPATH, "./*")
    for chat in sub_header:
        chats = chat.find_elements(By.XPATH, "./*")
        for item in chats:
            items = item.find_elements(By.XPATH, "./*")
            for text in items:
                ret.append(text.text)

    return ret
