#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/11
File: test_level_a.py
"""

import allure
import pytest
from soloop.v128.flow.mark_a_flow import Pytest_Mark_a_Flow


@allure.epic("即录素材浏览")
class TestFastFilm:

    @allure.feature("即录")
    @allure.story('使用模板')
    @allure.title("检查“使用模板”可以正常使用")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=1)
    @pytest.mark.A
    def test_levelA_use_cases_01(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.use_template()

    @allure.feature("即录")
    @allure.story('主页模板')
    @allure.title("检查“使用模板”点赞及分享功能")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=2)
    @pytest.mark.A
    def test_levelA_use_cases_02(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.like_share()

    @allure.feature("即录")
    @allure.story('主页模板')
    @allure.title("点击达人头像进入达人主页，查看达人主页视频是否可以正常播放和使用")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=3)
    @pytest.mark.A
    def test_levelA_use_cases_03(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.like_share2()

    @allure.feature("即录")
    @allure.story('账号')
    @allure.title("检查账号可正常登录")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=22)
    @pytest.mark.A
    def test_levelA_use_cases_04(self, driver, start_stop_app, data):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_mine()
        A_Flow.login(**data["common_data"])

    @allure.feature("即录")
    @allure.story('账号')
    @allure.title("检查账号可签到")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=23)
    @pytest.mark.A
    def test_levelA_use_cases_05(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_sign_in()

    @allure.feature("即录")
    @allure.story('自由剪辑')
    @allure.title("检查无操作返回的状态")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=4)
    @pytest.mark.A
    def test_levelA_use_cases_06(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.no_operation_returns()

    @allure.feature("即录")
    @allure.story('自由剪辑')
    @allure.title("检查有操作返回的状态")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=5)
    @pytest.mark.A
    def test_levelA_use_cases_07(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.operation_returns()

    @allure.feature("即录")
    @allure.story('转场')
    @allure.title("查看是否弹出弹层默认选中情况")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=6)
    @pytest.mark.A
    def test_levelA_use_cases_08(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_transitions_1()

    @allure.feature("即录")
    @allure.story('转场')
    @allure.title("查看是否支持预览")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=7)
    @pytest.mark.A
    def test_levelA_use_cases_09(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_transitions_2()

    @allure.feature("即录")
    @allure.story('转场')
    @allure.title('点击“X”，不应用已预览的转场效果')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=8)
    @pytest.mark.A
    def test_levelA_use_cases_10(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_transitions_3()

    @allure.feature("即录")
    @allure.story('转场')
    @allure.title('点击“√”，应用已预览的转场效果')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=9)
    @pytest.mark.A
    def test_levelA_use_cases_11(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_transitions_4()

    @allure.feature("即录")
    @allure.story('动画')
    @allure.title('检查剪辑tab动画功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=10)
    @pytest.mark.A
    def test_levelA_use_cases_12(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_cartoon()

    @allure.feature("即录")
    @allure.story('排序')
    @allure.title('检查剪辑tab排序功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=11)
    @pytest.mark.A
    def test_levelA_use_cases_13(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_sort()

    @allure.feature("即录")
    @allure.story('变速')
    @allure.title('检查剪辑tab变速功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=12)
    @pytest.mark.A
    def test_levelA_use_cases_14(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_speed()

    @allure.feature("即录")
    @allure.story('背景')
    @allure.title('检查剪辑tab背景功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=13)
    @pytest.mark.A
    def test_levelA_use_cases_15(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_background()

    @allure.feature("即录")
    @allure.story('倒放')
    @allure.title('检查剪辑tab倒放功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=14)
    @pytest.mark.A
    def test_levelA_use_cases_16(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_reverse()

    @allure.feature("即录")
    @allure.story('替换')
    @allure.title('检查剪辑tab替换功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=15)
    @pytest.mark.A
    def test_levelA_use_cases_17(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_replace()

    @allure.feature("即录")
    @allure.story('旋转')
    @allure.title('检查剪辑tab旋转功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=16)
    @pytest.mark.A
    def test_levelA_use_cases_18(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_rotation()

    @allure.feature("即录")
    @allure.story('音乐')
    @allure.title('检查音乐上下左右滑动功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=17)
    @pytest.mark.A
    def test_levelA_use_cases_19(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_music_swipe()

    @allure.feature("即录")
    @allure.story('音乐')
    @allure.title('检查音乐收藏功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=18)
    @pytest.mark.A
    def test_levelA_use_cases_20(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_collect()

    @allure.feature("即录")
    @allure.story('音乐')
    @allure.title('检查音乐下载功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=19)
    @pytest.mark.A
    def test_levelA_use_cases_21(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_download()

    @allure.feature("即录")
    @allure.story('音乐')
    @allure.title('检查音乐使用功能')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=20)
    @pytest.mark.A
    def test_levelA_use_cases_22(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_use_song()

    @allure.feature("即录")
    @allure.story('画中画')
    @allure.title('检查剪辑tab画中画气泡')
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=21)
    @pytest.mark.A
    def test_levelA_use_cases_23(self, driver, start_stop_app):
        A_Flow = Pytest_Mark_a_Flow(driver)
        A_Flow.click_pip()

