import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

desireCap = {
  "automationName": "UiAutomator2",
  "platformName": "Android",
  "platformVersion": "7.0",
  "deviceName": "Moto G4",
  "appActivity": "com.androidsample.generalstore.SplashActivity",
  "appPackage": "com.androidsample.generalstore",
  "udid": "ZY223CPDLT"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desireCap)
driver.implicitly_wait(30)


driver.find_element_by_xpath("//*[@resource-id='com.androidsample.generalstore:id/nameField']").click()
time.sleep(2)
name = [29,44,29,33,45,43,55]

for x  in name:
  driver.press_keycode(x)


driver.hide_keyboard()



