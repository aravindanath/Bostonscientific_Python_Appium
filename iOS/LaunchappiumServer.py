import time
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


service = AppiumService()
service.start(args=['--address','0.0.0.0','-p','4723'])
print(service.is_running)
time.sleep(3)


desireCap = {
  "automationName": "XCUITest",
  "platformName": "iOS",
  "platformVersion": "15.1.1",
  "deviceName": "Iphone 13",
  "bundleId":"com.apollo.apollo247",
  "udid": "00008110-000529C83CA2801E"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desireCap)
driver.implicitly_wait(30)
time.sleep(2)
driver.find_element_by_ios_class_chain('**/XCUIElementTypeOther[`label == "MEDICINES"`][2]').click()

time.sleep(2)
# down,right,left,up
driver.execute_script("mobile: scroll",{'direction': 'down'})

print(service.stop())