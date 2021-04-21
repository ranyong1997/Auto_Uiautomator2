#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: 80243990
Date: 2020/11/30
File: test_setting.py
"""
import allure
import pytest

from wallet.v390.flow.setting_flow import SettingFlow


@allure.epic("设置")
class TestSetting:

    @allure.feature("实名认证")
    @allure.title("检查实名认证基本功能正常")
    @pytest.mark.release
    @pytest.mark.test
    # @pytest.mark.run(order=1)
    @pytest.mark.S
    def test_setting_0001(self, driver, start_stop_app, data, cancel_account2):
        setting_flow = SettingFlow(driver)
        # setting_flow.goto_setting_page()
        setting_flow.real_name_verification(scene=2, **data["test_setting_0001"])

    @allure.feature("双击唤醒")
    @allure.title("检查双击唤醒开关功能正常")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=24)
    def test_setting_0002(self, driver, start_stop_app):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.double_tap_power_switch()

    @allure.feature("自动切卡")
    @allure.title("检查自动切卡基本功能正常")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=25)
    def test_setting_0003(self, driver, start_stop_app):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.auto_switch_card()

    @allure.feature("一键修复")
    @allure.title("检查一键修复基本功能正常")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=2)
    def test_setting_0004(self, driver, start_stop_app):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.one_click_repair()

    @allure.feature("支付密码设置")
    @allure.title("更改支付密码")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=46)
    def test_setting_0005(self, driver, start_stop_app, data):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.change_wallet_password(**data["test_setting_0005"])

    @allure.feature("支付密码设置")
    @allure.title("通过身份信息找回密码")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=57)
    def test_setting_0006(self, driver, start_stop_app, data):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.forget_wallet_password(scene=1, **data["test_setting_0006"])

    @allure.feature("支付密码设置")
    @allure.title("通过密保和手机号找回密码")
    @pytest.mark.release
    @pytest.mark.run(order=47)
    def test_setting_0007(self, driver, start_stop_app, data):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.forget_wallet_password(scene=2, **data["test_setting_0007"])

    @allure.feature("支付密码设置")
    @allure.title("重置密保")
    @pytest.mark.release
    @pytest.mark.run(order=48)
    def test_setting_0008(self, driver, start_stop_app, data):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.reset_security(**data["test_setting_0008"])

    @allure.feature("服务管理")
    @allure.title("检查关闭首页若干服务入口后跳转正常")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=3)
    def test_setting_0009(self, driver, start_stop_app, data):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.close_function_entry(**data["test_setting_0009"])

    @allure.feature("版本号")
    @allure.title("检查版本号功能正常")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=4)
    def test_setting_0010(self, driver, start_stop_app):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.check_protocol_statement_version()

    @allure.feature("注销")
    @allure.title("注销钱包支付账户")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=59)
    def test_setting_0011(self, driver, start_stop_app, data):
        setting_flow = SettingFlow(driver)
        setting_flow.goto_setting_page()
        setting_flow.cancel_wallet_payment_account(**data["test_setting_0011"])
