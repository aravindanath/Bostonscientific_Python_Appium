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

driver.find_element_by_id("com.androidsample.generalstore:id/spinnerCountry").click()

driver.find_element_by_xpath("//android.widget.TextView[@text='Angola']").click()
driver.find_element_by_xpath("//*[@resource-id='com.androidsample.generalstore:id/nameField']").send_keys("Arvind")

driver.find_element_by_xpath("//*[@text='Male']").click()
time.sleep(3)
driver.find_element_by_xpath("//*[contains(@text,'Shop')]").click()
time.sleep(3)
list =  driver.find_elements_by_xpath("//*[@text='ADD TO CART']")
for l in list:
  l.click()

driver.find_element_by_id("com.androidsample.generalstore:id/appbar_btn_cart").click()

time.sleep(2)

total = driver.find_element_by_id("com.androidsample.generalstore:id/totalAmountLbl").text

print(total)

driver.find_element_by_id("com.androidsample.generalstore:id/btnProceed").click()
time.sleep(3)
cont = driver.contexts

for c in cont:
  print(c.title())

cont = driver.contexts[1]
driver.switch_to.context(cont)

print("Webview title "+driver.title)







