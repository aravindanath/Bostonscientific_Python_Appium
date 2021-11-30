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

driver.open_notifications()
time.sleep(2)
driver.find_element_by_xpath("//*[@text='089044 83799']").click()




