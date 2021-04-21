#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9006360
Date: 2020/10/10
File: test_change.py
"""
import allure
import pytest

from wallet.v390.flow.change_flow import ChangeFlow


@allure.epic("零钱")
class TestChange:

    @allure.feature('开户')
    @allure.title("使用借记卡开通零钱(生产环境)")
    @pytest.mark.release
    @pytest.mark.nfc
    @pytest.mark.run(order=50)
    def test_change_0001(self, driver, start_stop_app, data, clear_all_message):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.open_change_account(scene=1, support_nfc=True, **data["test_change_0001"])

    @allure.feature('开户')
    @allure.title("使用借记卡开通零钱(测试环境)")
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=50)
    def test_change_0002(self, driver, start_stop_app, data):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.open_change_account(scene=2, support_nfc=True, **data["test_change_0002"])

    @allure.feature('充值')
    @allure.title("使用借记卡充值")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.skip
    @pytest.mark.run(order=51)
    def test_change_0003(self, driver, start_stop_app, data, clear_all_message):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.change_recharge(**data["test_change_0003"])

    @allure.feature('提现')
    @allure.title("全部提现到借记卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=52)
    def test_change_0004(self, driver, start_stop_app, data):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.change_withdraw(**data["test_change_0004"])

    @allure.feature('查看信息')
    @allure.title("遍历零钱明细、零钱绑定卡、关于零钱的内容")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=53)
    def test_change_0005(self, start_stop_app, driver):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.traverse_change_detail()

    @allure.feature('账户升级')
    @allure.title("提升零钱限额")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=54)
    def test_change_0006(self, driver, start_stop_app, data):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.increase_limit(**data["test_change_0006"])

    @allure.feature('绑卡')
    @allure.title("再次添加一张借记卡(生产环境)")
    @pytest.mark.release
    @pytest.mark.run(order=55)
    def test_change_0007(self, driver, start_stop_app, data):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.bind_another_bank_card(scene=1, **data["test_change_0007"])

    @allure.feature('绑卡')
    @allure.title("再次添加一张借记卡(测试环境)")
    @pytest.mark.test
    @pytest.mark.run(order=55)
    def test_change_0008(self, driver, start_stop_app, data):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.bind_another_bank_card(scene=2, **data["test_change_0008"])

    @allure.feature('删卡')
    @allure.title("删除零钱绑定卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=56)
    def test_change_0009(self, driver, start_stop_app):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.delete_bound_card()

    @allure.feature('注销')
    @allure.title("注销零钱账户")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=58)
    def test_change_0010(self, driver, start_stop_app, data):
        change_flow = ChangeFlow(driver)
        change_flow.goto_change_page()
        change_flow.cancel_change_account(**data["test_change_0010"])

