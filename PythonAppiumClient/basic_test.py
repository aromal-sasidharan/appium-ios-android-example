import unittest
import time
from commonutils import setup

class BasicTest(unittest.TestCase):
    test_name = "BasicTest"
    driver = None
    def test_basic_test(self):
        setup(self)
        time.sleep(5)
        email = self.driver.find_element_by_name("email")
        email.clear()
        email.send_keys("aromal.sasidharan@accenture.com")
        self.driver.back()
        time.sleep(5)