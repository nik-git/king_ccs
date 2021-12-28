from appium import webdriver
dc = {
  "platformName": "Android",
  "deviceName": "Android Emulator"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', dc)
driver.remove_app('com.flipkart.android')
