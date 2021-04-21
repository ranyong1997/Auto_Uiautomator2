#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/15
File: test_third_party.py
"""
import allure
import pytest

from wallet.v390.flow.third_party_flow import ThirdPartyFlow


@allure.epic("第三方服务")
class TestThirdParty:

    @allure.feature("生活服务")
    @allure.title("遍历首页全部中的所有服务入口")
    @pytest.mark.release
    @pytest.mark.run(order=6)
    def test_third_party_0001(self, driver, start_stop_app, data):
        third_party_flow = ThirdPartyFlow(driver)
        third_party_flow.goto_services_page(1)
        third_party_flow.in_out_all_webview_services(**data["test_third_party_0001"])
        third_party_flow.in_out_all_quickapp_services(**data["test_third_party_0001"])
        third_party_flow.in_out_cocoin_recharge_service(**data["test_third_party_0001"])

    @allure.feature("生活服务")
    @allure.title("遍历我的页面下的我的服务入口")
    @pytest.mark.release
    @pytest.mark.run(order=7)
    def test_third_party_0002(self, driver, start_stop_app, data):
        third_party_flow = ThirdPartyFlow(driver)
        third_party_flow.goto_services_page(2)
        third_party_flow.in_out_all_webview_services(**data["test_third_party_0002"])
