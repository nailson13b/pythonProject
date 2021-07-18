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

print("Check if device is locked or not: ", driver.is_locked())
print("Current Package: ", driver.current_package)
print("Current Package: ", driver.current_activity)
print("Current Package: ", driver.current_context)
print("Current Package: ", driver.orientation)