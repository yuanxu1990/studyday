from appium import webdriver
import time

desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:7555',
    'platformVersion': '6.0.1',
    'appPackage': 'com.taobao.taobao',
    'appActivity': 'com.taobao.tao.TBMainActivity'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(5)
driver.implicitly_wait(2)
ele=driver.find_element_by_accessibility_id('ins运动鞋')
ele.click()
ele.send_keys('1111')
