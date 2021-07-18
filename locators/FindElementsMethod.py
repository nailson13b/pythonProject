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

element = driver.find_elements_by_class_name("android.widget.Button")

for x in element:
    print(x.text)

for x in element:
    button = x.text
    if button == "ScrollView":
        x.click()
        break

time.sleep(5)
driver.quit()