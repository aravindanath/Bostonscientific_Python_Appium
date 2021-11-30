import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'chromedriver')

print(filename)

desireCap = {
  "automationName": "UiAutomator2",
  "platformName": "Android",
  "platformVersion": "7.0",
  "deviceName": "Moto G4",
  "chromedriverExecutable":filename,
  "udid": "ZY223CPDLT",
  "browserName":"chrome"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desireCap)
driver.implicitly_wait(30)

driver.get("https://www.google.com")
time.sleep(2)
driver.find_element_by_xpath("//input[@name='q']").send_keys("Iphone 13")


