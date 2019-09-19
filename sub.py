import pyautogui
from selenium import webdriver
import time

width,height = pyautogui.size()

br = webdriver.Chrome()
br.get('https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw')

pyautogui.moveTo(866,409, duration = 4)
time.sleep(3)
pyautogui.click()