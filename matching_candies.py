from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

dc = {
     "platformName": "Android",
     "deviceName": "Q89LFIZH7HT4S4NV",
     "app": "c:\\software\\com.king.candycrushsaga_12040021_apps.evozi.com.apk"
     }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', dc)

time.sleep(5)
TouchAction(driver).tap(None, 535, 1580, 1).perform()  # Click on Activate
time.sleep(5)
TouchAction(driver).tap(None, 535, 1150, 1).perform()  # Click on Play
time.sleep(10)
TouchAction(driver).tap(None, 535, 2150, 1).perform()  # tap anywhere
time.sleep(15)
TouchAction(driver).tap(None, 535, 2150, 1).perform()  # skip
time.sleep(5)
TouchAction(driver).press(x=315, y=1235).move_to(x=430, y=1235).release().perform()  # First move of first level
time.sleep(5)
driver.close_app()
