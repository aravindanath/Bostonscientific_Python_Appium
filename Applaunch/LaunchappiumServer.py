import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


service = AppiumService()
service.start(args=['--address','0.0.0.0','-p','4724'])
print(service.is_running)
time.sleep(3)


desireCap = {
  "automationName": "UiAutomator2",
  "platformName": "Android",
  "platformVersion": "7.0",
  "deviceName": "Moto G4",
  "appActivity": "com.androidsample.generalstore.SplashActivity",
  "appPackage": "com.androidsample.generalstore",
  "udid": "ZY223CPDLT"
}
driver = webdriver.Remote("http://0.0.0.0:4724/wd/hub",desireCap)
driver.implicitly_wait(30)
time.sleep(2)

driver.save_screenshot("demo.png")
time.sleep(2)
print(service.stop())