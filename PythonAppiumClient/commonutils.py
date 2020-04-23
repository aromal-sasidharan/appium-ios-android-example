from appium import webdriver
import unittest
import os
# {
#   "deviceName": "appium_1",
#   "automationName": "XCUITest",
#   "platformName": "iOS",
#   "udid": "1C07E37F-D641-4605-8455-2C99025FD713",
#   "xcodeOrgId": "io.appium",
#   "xcodeSigningId": "iPhoneDeveloper",
#   "bundleId": "com.sppl.mobileapp.iossit",
#   "platformVersion": "13.3",
#   "app": "/Users/sandeep.chandra.babu/Library/Developer/Xcode/DerivedData/mobileapp-ffnmanbhpkfsbehdqfdfaxpzamgj/Build/Products/remoteSIT-iphonesimulator/SPPL-Mobile.app",
#   "useNewWDA": true
# }
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def setup(self):
    path = """/Volumes/leo/Xcode/DerivedData/LoginScreenTutorial-clucypowvvgmjqcreeeenpoydabo/Build/Products/Debug-iphonesimulator/LoginScreenTutorial.app"""
    desired_caps = {}
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = '13.3'
    desired_caps['udid'] = 'D3621250-0932-496C-BFC0-2DCEA9C46A4E'
    desired_caps['automationName'] = 'xcuitest'
    desired_caps['deviceName'] = 'appium'
    desired_caps['app'] = PATH(path)
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)