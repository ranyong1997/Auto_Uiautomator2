#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/11
File: test_level_a.py
"""

import allure
import pytest
from soloop.v112.flow.mark_a_flow import Pytest_Mark_a_Flow


@allure.epic("即录遍历功能")
class TestFastFilm:

    @allure.feature("即录")
    @allure.story('素材预览')
    @allure.title("检查素材可正常预览")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_01(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.material_preview()

    @allure.feature("即录")
    @allure.story('滤镜')
    @allure.title("检查滤镜功能是否正常")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_02(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.filter_display()

    @allure.feature("即录")
    @allure.story('手动剪辑-返回')
    @allure.title("检查无操作返回的状态")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_03(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.no_operation_returns()

    @allure.feature("即录")
    @allure.story('手动剪辑-返回')
    @allure.title("检查有操作返回点击空白区域")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_04(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.operation_blank()

    @allure.feature("即录")
    @allure.story('手动剪辑-返回')
    @allure.title("检查有操作返回直接退出的状态")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_05(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.operation_returns_exit()

    @allure.feature("即录")
    @allure.story('手动剪辑-返回')
    @allure.title("检查有操作返回存为草稿的状态")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_06(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.operation_returns_save()

    @allure.feature("即录")
    @allure.story('手动剪辑-删除')
    @allure.title("导入一个素材时,检查手动剪辑删除功能")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_07(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.clip_delete1()

    @allure.feature("即录")
    @allure.story('手动剪辑-删除')
    @allure.title("导入两个素材时,检查手动剪辑删除功能")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_08(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.clip_delete2()

    @allure.feature("即录")
    @allure.story('手动剪辑-删除')
    @allure.title("删除片尾，检查手动剪辑删除功能")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_09(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.clip_delete3()

    @allure.feature("即录")
    @allure.story('手动剪辑-排序')
    @allure.title("导入一个素材时，查看排序是否可用")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_10(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.sorting_function1()

    @allure.feature("即录")
    @allure.story('手动剪辑-排序')
    @allure.title("导入二个素材时，查看排序是否可用")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_11(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.sorting_function2()

    @allure.feature("即录")
    @allure.story('手动剪辑-动画')
    @allure.title("检查剪辑tab动画功能")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_12(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_cartoon()

    @allure.feature("即录")
    @allure.story('手动剪辑-变速')
    @allure.title("检查剪辑tab变速等功能")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_13(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_speed()

    @allure.feature("即录")
    @allure.story('手动剪辑-倒放')
    @allure.title("选择图片，查看倒放按钮")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_14(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_reverse1()

    @allure.feature("即录")
    @allure.story('手动剪辑-倒放')
    @allure.title("选择视频，查看倒放按钮")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_15(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_reverse2()

    @allure.feature("即录")
    @allure.story('手动剪辑-音乐')
    @allure.title("检查音乐分类功能")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_16(self, driver, start_stop_app):
        # 如果报错就注释
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_music()

    @allure.feature("即录")
    @allure.story('手动剪辑-字幕')
    @allure.title("检查字幕功能可正常添加")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_17(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_subtitle_style()

    @allure.feature("即录")
    @allure.story('手动剪辑-字幕')
    @allure.title("检查字幕功能可正常添加")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_18(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_subtitle()

    @allure.feature("即录")
    @allure.story('手动剪辑-字幕')
    @allure.title("检查AI字幕功能可正常")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_19(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_ai()

    @allure.feature("即录")
    @allure.story('手动剪辑-音乐')
    @allure.title("查看打开音乐调整页面")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_20(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_music2()

    @allure.feature("即录")
    @allure.story('手动剪辑-贴纸')
    @allure.title("查看贴纸可正常添加使用")
    @pytest.mark.release
    @pytest.mark.A
    def test_levelA_use_cases_21(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_preview()



