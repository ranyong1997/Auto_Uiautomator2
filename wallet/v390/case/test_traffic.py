#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: 80243990
Date: 2020/10/20
File: test_traffic.py
"""
import allure
import pytest

from wallet.v390.flow.traffic_flow import TrafficFlow


@allure.epic("公交卡")
class TestTraffic:

    @allure.feature("添加公交卡")
    @allure.title("开通京津冀互联互通卡")
    @pytest.mark.release
    @pytest.mark.nfc
    @pytest.mark.run(order=10)
    def test_traffic_0001(self, driver, start_stop_app, data):
        traffic_flow = TrafficFlow(driver)
        traffic_flow.goto_add_card_page(scene=1)
        traffic_flow.open_transit_card(**data["test_traffic_0001"])

    @allure.feature("充值公交卡")
    @allure.title("京津冀互联互通卡充值10元")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=11)
    def test_traffic_0002(self, driver, start_stop_app, data):
        traffic_flow = TrafficFlow(driver)
        traffic_flow.recharge_transit_card(**data["test_traffic_0002"])

    @allure.feature("查看公交卡")
    @allure.title("查看京津冀互联互通卡卡片详情页所有入口")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=12)
    def test_traffic_0003(self, driver, start_stop_app):
        traffic_flow = TrafficFlow(driver)
        traffic_flow.traverse_card_detail()

    @allure.feature("迁移公交卡")
    @allure.title("迁出京津冀互联互通卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=13)
    def test_traffic_0004(self, driver, start_stop_app, data):
        traffic_flow = TrafficFlow(driver)
        traffic_flow.shift_out_transit_card(**data["test_traffic_0004"])

    @allure.feature("迁移公交卡")
    @allure.title("迁入京津冀互联互通卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=14)
    def test_traffic_0005(self, driver, start_stop_app, data):
        traffic_flow = TrafficFlow(driver)
        traffic_flow.shift_in_transit_card(scene=2, **data["test_traffic_0005"])

    @allure.feature("删除公交卡")
    @allure.title("删除京津冀互联互通卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=60)
    def test_traffic_0006(self, driver, start_stop_app, data):
        traffic_flow = TrafficFlow(driver)
        traffic_flow.delete_transit_card(**data["test_traffic_0006"])
