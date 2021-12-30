import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

SLEEP_SMALL = 5
SLEEP_MEDIUM = 10
SLEEP_LARGE = 15
AAPIUM_SERVER_URL = 'http://127.0.0.1:4723/wd/hub'
CLICK_TIME = 1
APP_ID = "com.king.candycrushsaga"

"""
Run this command to run this test : pytest test_ccs.py --brand Samsung
"""
DATA = {"Samsung": {"desired_capability": {"platformName": "Android",
                                           "deviceName": "Q89LFIZH7HT4S4NV",
                                           "app": "c:\\software\\com.king.candycrushsaga_12040021_apps.evozi.com.apk"
                                           },
                    "generic_x_cord": 535,
                    "move_init_x_cord": 315,
                    "move_init_y_cord": 1235,
                    "activate_y_cord": 1580,
                    "play_y_cord": 1150,
                    "anywhere_y_cord": 2150,
                    "skip_y_cord": 2150,
                    "move_final_x_cord": 430,
                    "move_final_y_cord": 1235
                    },

        "Apple": {"desired_capability": {"platformName": "iOS",
                                         "deviceName": "someDeviceName",
                                         "app": "c:\\software\\com.king.candycrushsaga_12040021_apps.evozi.com.apk"
                                         },
                  "generic_x_cord": 535,
                  "move_init_x_cord": 315,
                  "move_init_y_cord": 1235,
                  "activate_y_cord": 1580,
                  "play_y_cord": 1150,
                  "anywhere_y_cord": 2150,
                  "skip_y_cord": 2150,
                  "move_final_x_cord": 430,
                  "move_final_y_cord": 1235
                  }
        }


@pytest.fixture()
def brand(pytestconfig):
    return pytestconfig.getoption("brand")


def test_make_first_move_in_cand_crush_saga(brand):
    data = DATA[brand]
    driver = webdriver.Remote(AAPIUM_SERVER_URL, data['desired_capability'])
    time.sleep(SLEEP_SMALL)
    # Click on Activate
    TouchAction(driver).tap(None, data['generic_x_cord'], data['activate_y_cord'], CLICK_TIME).perform()
    time.sleep(SLEEP_SMALL)
    TouchAction(driver).tap(None, data['generic_x_cord'], data['play_y_cord'], CLICK_TIME).perform()  # Click on Play
    time.sleep(SLEEP_MEDIUM)
    # Tap anywhere
    TouchAction(driver).tap(None, data['generic_x_cord'], data['anywhere_y_cord'], CLICK_TIME).perform()
    time.sleep(SLEEP_LARGE)
    TouchAction(driver).tap(None, data['generic_x_cord'], data['skip_y_cord'], CLICK_TIME).perform()  # Skip tutorial
    time.sleep(SLEEP_SMALL)
    # First move of first level
    TouchAction(driver).press(x=data['move_init_x_cord'],
                              y=data['move_init_y_cord']).move_to(x=data['move_final_x_cord'],
                                                                  y=data['move_final_y_cord']).release().perform()
    time.sleep(SLEEP_SMALL)
    driver.close_app()
    time.sleep(SLEEP_SMALL)
    driver.remove_app(APP_ID)

