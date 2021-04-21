'''
Descripttion: 
version: 
Author: 冉勇
Date: 2021-04-01 18:51:27
LastEditTime: 2021-04-06 19:10:09
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: 80243990
Date: 2020/11/24
File: test_eid.py
"""
import allure
import pytest

from wallet.v390.flow.eid_flow import EIDFlow


@allure.epic("EID")
class TestEID:

    @allure.feature("开通eID")
    @allure.title("首次开通eID")
    @pytest.mark.release
    @pytest.mark.nfc
    # @pytest.mark.run(order=30)
    @pytest.mark.S
    def test_eid_0001(self, driver, start_stop_app, data):
        eid_flow = EIDFlow(driver)
        eid_flow.open_eid_card(scene=1, **data["test_eid_0001"])

    @allure.feature("查看eID")
    @allure.title("遍历我的eID页面所有入口")
    @pytest.mark.release
    @pytest.mark.nfc
    @pytest.mark.run(order=31)
    def test_eid_0002(self, driver, start_stop_app, data):
        eid_flow = EIDFlow(driver)
        eid_flow.traverse_my_eid_card(**data["test_eid_0002"])

    @allure.feature("删除eID")
    @allure.title("删除eID")
    @pytest.mark.release
    @pytest.mark.nfc
    @pytest.mark.run(order=32)
    def test_eid_0003(self, driver, start_stop_app):
        eid_flow = EIDFlow(driver)
        eid_flow.delete_eid_card()

    @allure.feature("开通eID")
    @allure.title("再次开通eID")
    @pytest.mark.release
    @pytest.mark.nfc
    @pytest.mark.run(order=33)
    def test_eid_0004(self, driver, start_stop_app, data):
        eid_flow = EIDFlow(driver)
        eid_flow.open_eid_card(scene=2, **data["test_eid_0004"])

    @allure.feature("删除eID")
    @allure.title("删除eID,并注销钱包账户")
    @pytest.mark.release
    @pytest.mark.nfc
    @pytest.mark.run(order=34)
    def test_eid_0005(self, driver, start_stop_app, cancel_account):
        eid_flow = EIDFlow(driver)
        eid_flow.delete_eid_card()
