#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

import pytest

from common.config_parser import ReadConfig
from common.utils import get_installed_package_name
from common.yaml_parser import ReadYaml
from wallet.v390 import root_dir
from wallet.v390.flow.setting_flow import SettingFlow

package_name = get_installed_package_name()


@pytest.fixture(scope="session")
def change_environment(driver):
    driver.app_start(package_name, "com.nearme.wallet.envswitch.EnvSwitchTestActivity")
    driver(text="测试4").click()
    driver.sleep(1.0)
    driver(text="测试4").click()
    driver.press("recent")
    driver.swipe_ext("up", 0.5)


@pytest.fixture(scope="function")
def data():
    filename = "data.yaml"
    return ReadYaml().read(os.path.join(root_dir, "data", filename))


@pytest.fixture(scope="function")
def clear_all_message(driver):
    driver.open_notification()
    if ReadConfig().get_platform == "android":
        element = driver(resourceId="com.android.systemui:id/shelf_dismiss_text")
        if element.wait(timeout=3.0):
            element.click()
        else:
            driver.press("back")


@pytest.fixture(scope="function")
def cancel_account(driver, data):
    yield
    driver.app_start(package_name, "com.nearme.wallet.bank.payment.WalletSettingActivity")
    setting_flow = SettingFlow(driver)
    setting_flow.cancel_wallet_payment_account(scene=1, **data["test_setting_0011"])


@pytest.fixture(scope="function")
def cancel_account2(driver, data):
    yield
    driver.app_start(package_name, "com.nearme.wallet.bank.payment.WalletSettingActivity")
    setting_flow = SettingFlow(driver)
    setting_flow.cancel_wallet_payment_account(scene=2, **data["test_setting_0011"])
