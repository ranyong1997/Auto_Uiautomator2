#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: 80243990
Date: 2020/10/22
File: test_key.py
"""
import allure
import pytest

from wallet.v390.flow.key_flow import KeyFlow


@allure.epic("门禁卡")
class TestKey:

    @allure.feature("添加门禁卡")
    @allure.title("添加实体门禁卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=20)
    def test_key_0001(self, driver, start_stop_app, data, clear_all_message):
        key_flow = KeyFlow(driver)
        key_flow.goto_add_card_page(scene=1)
        key_flow.open_physical_access_card(**data["common"])

    @allure.feature("添加门禁卡")
    @allure.title("生成空白卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=21)
    def test_key_0002(self, driver, start_stop_app):
        key_flow = KeyFlow(driver)
        key_flow.goto_add_card_page(scene=2)
        key_flow.open_manual_access_card()

    @allure.feature("编辑门禁卡")
    @allure.title("遍历编辑卡片所有功能")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=22)
    def test_key_0003(self, driver, start_stop_app, data):
        key_flow = KeyFlow(driver)
        key_flow.edit_access_card(**data["test_key_0003"])

    @allure.feature("迁移门禁卡")
    @allure.title("迁入门禁卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=23)
    def test_key_0004(self, driver, start_stop_app):
        key_flow = KeyFlow(driver)
        key_flow.goto_add_card_page(scene=3)
        key_flow.access_card_transfer_operation()

    @allure.feature("删除门禁卡")
    @allure.title("删除空白卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=24)
    def test_key_0005(self, driver, start_stop_app):
        key_flow = KeyFlow(driver)
        key_flow.delete_blank_card()

    @allure.feature("删除门禁卡")
    @allure.title("删除实体门禁卡,并注销钱包账户")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=26)
    def test_key_0006(self, driver, start_stop_app,):
        key_flow = KeyFlow(driver)
        key_flow.delete_access_card()
