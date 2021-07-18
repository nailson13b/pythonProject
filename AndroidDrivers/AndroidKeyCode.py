import time

from appium import webdriver

# Part 1 "Desired Capabilities"

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '11'
desired_caps['deviceName'] = 'Pixel 2 API 30'
desired_caps['app'] = ('C:\workspace\Automation\Android_Appium_Demo.apk')
desired_caps['appPackage'] = 'com.skill2lead.appiumdemo'
desired_caps['appActivity'] = 'com.skill2lead.appiumdemo.MainActivity'

# Part 2 "WebDriver object"
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

ele_id = driver.find_element_by_id("com.skill2lead.appiumdemo:id/EnterValue")
ele_id.click()

time.sleep(2)

ele_classname = driver.find_element_by_class_name("android.widget.EditText")
ele_classname.send_keys("HelloWorld")
ele_classname.click()
time.sleep(2)
driver.press_keycode(67)
driver.press_keycode(67)
time.sleep(2)
driver.press_keycode(4)
driver.press_keycode(4)