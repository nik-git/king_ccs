from appium import webdriver
# install on Real device.
dc = {
     "platformName": "Android",
     "deviceName": "Q89LFIZH7HT4S4NV" # real device id
     }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', dc)
driver.install_app("c:\\software\\com.king.candycrushsaga_12040021_apps.evozi.com.apk")
