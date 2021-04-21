#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: 80243990
Date: 2020/12/1
File: test_mine.py
"""
import allure
import pytest

from wallet.v390.flow.mine_flow import MineFlow


@allure.epic("我的")
class TestMine:

    @allure.feature("我的")
    @allure.title("遍历我的页面所有入口均跳转正常，页面可正常打开")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=5)
    def test_mine_0001(self, driver, start_stop_app):
        mine_flow = MineFlow(driver)
        mine_flow.traverse_mine_page()
