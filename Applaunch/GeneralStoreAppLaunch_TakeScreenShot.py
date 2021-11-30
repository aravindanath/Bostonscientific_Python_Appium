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

driver.find_element_by_xpath("//*[@resource-id='com.androidsample.generalstore:id/nameField']").send_keys("Arvind")

driver.find_element_by_xpath("//*[@text='Male']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@text,'Shop')]").click()
time.sleep(3)

driver.save_screenshot("demo.png")


