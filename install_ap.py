from appium import webdriver
# install Android studio, Appium desktop server
# Create a Android emulator
# Downlaod .apk file of Flipkart App
# Run Android emulator and Appium server
# install Appium-Python-Client
dc = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "app": "c:\\software\\flipkart.apk"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', dc)
