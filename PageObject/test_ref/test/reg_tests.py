import unittest
from appium.webdriver.common.mobileby import MobileBy
from utils.setup_env.init_appium import Driver
import pytest



class RegistrationTestCases(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_spalsh_activity(self):
        self.driver.instance.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout")
    
    def onboarding_screen(self):
        self.driver.instance.find_element_by_id(MobileBy.ID, "com.ingenio.keen.stage:id/btnSignIn").click()
    # def tearDown(self):
    #     self.driver.instance.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(RegistrationTestCases)
    unittest.TextTestRunner(verbosity=2).run(suite)