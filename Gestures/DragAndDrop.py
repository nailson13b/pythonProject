import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

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

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])

wait.until(lambda x: x.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()).scrollIntoView(text("DRAGANDDROP"))')).click()
ele_kw = wait.until(lambda x: x.find_element_by_id("com.skill2lead.appiumdemo:id/ingvw"))
ele_lay = wait.until(lambda x: x.find_element_by_id("com.skill2lead.appiumdemo:id/layout2"))

actions = TouchAction(driver)
actions.long_press(ele_kw).move_to(ele_lay).release().perform()

time.sleep(4)

driver.quit()