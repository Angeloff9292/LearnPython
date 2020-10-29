from appium import webdriver


class Driver:

    def __init__(self):

        desired_caps = {
            "appActivity": "com.itomych.keen.splash.ui.SplashActivity",
            "platformName": "Android",
            "deviceName": "Android Emulator",
            "app": "/Users/olegzalipsky/Downloads/app/build/outputs/apk/stage/release/app-stage-release.apk",
            "noSign": True,
            "automatorName": "UiAutomator2"

        }

        self.instance = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)