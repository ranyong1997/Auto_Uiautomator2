#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/29
File: test_securepay_game.py
"""


import allure
import pytest
from soloop.v122.flow.videoexport_flow import VideoExportFlow


@pytest.mark.run(order=1)
@allure.epic("即录导出")
class TestFastFilm:

    @allure.feature("即录")
    @allure.story('导出')
    @allure.title("快速成片")
    @pytest.mark.release
    @pytest.mark.S
    def test_fastfilm_001(self, driver, start_stop_app):
        fast_flow = VideoExportFlow(driver)
        fast_flow.fast_filming()

    @allure.feature("即录")
    @allure.story('我的')
    @allure.title("设置")
    @pytest.mark.release
    @pytest.mark.S
    def test_main_tab_002(self, driver, start_stop_app):
        main_flow = VideoExportFlow(driver)
        main_flow.main_tab()

    @allure.feature("即录")
    @allure.story('导出')
    @allure.title("自由剪辑")
    @pytest.mark.release
    @pytest.mark.S
    def test_fastfilm_003(self, driver, start_stop_app):
        free_flow = VideoExportFlow(driver)
        free_flow.free_editing()
