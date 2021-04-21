#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/11
File: mark_a_page.py
"""

import allure
import random
from common.base_page import BasePage
from common.config_parser import ReadConfig
from soloop.v112.element.element_router import ElementRouter


class Mark_A_Page(BasePage):

    def __init__(self, driver):
        super(Mark_A_Page, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    @allure.step("点击快速成片")
    def click_fast_film(self):
        self.find_element_and_click(**self.element["fast_film"])

    @allure.step("点击自由剪辑")
    def click_free_edit(self):
        self.sleep(1)
        self.find_element_and_click(**self.element["free_edit"])

    @allure.step("点击某一张图片")
    def click_select_image1(self):
        self.find_element_and_click(**self.element["select_image1"])

    @allure.step("点击某一个视频")
    def click_first_video(self):
        self.find_element_and_click(**self.element["first_video"])

    @allure.step("点击图片")
    def click_picture(self):
        self.find_element_and_click(**self.element["picture"])

    @allure.step("点击预览")
    def click_preview_material(self):
        self.find_element_and_click(**self.element["preview_material"])

    @allure.step("点击播放")
    def click_play(self):
        self.find_element_and_click(**self.element["play"])

    @allure.step("点击复选框")
    def click_checkbox(self):
        i = 0
        j = 0
        for i in range(3):
            self.find_element_and_click(**self.element["checkbox"])
            self.swipe_screen("left", scale=0.7)
        i += 1
        for j in range(4):
            self.driver.click(0.868, 0.225)
        j += 1

    @allure.step("点击返回")
    def click_back(self):
        # self.find_element_and_click(**self.element["back"])
        self.driver.press('back')

    @allure.step("点击返回上一层")
    def click_back2(self):
        self.find_element_and_click(**self.element["back2"])

    @allure.step("点击视频")
    def click_video(self):
        self.find_element_and_click(**self.element["video"])

    @allure.step("点击下一步")
    def click_next(self):
        self.sleep(1)
        self.find_element_and_click(**self.element["next"])
        self.sleep(2)

    @allure.step("点击排序")
    def click_sort(self):
        self.find_element_and_click(**self.element["sort"])
        self.sleep(1)
        self.driver.drag(110, 1754, 298, 1754, 0.1)
        self.find_element_and_click(**self.element['hook_sort'])

    @allure.step("点击滤镜")
    def click_filter(self):
        self.find_element_and_click(**self.element["filter"])
        self.find_element_and_click(**self.element["filter1"])
        self.find_element_and_click(**self.element["filter2"])
        self.find_element_and_click(**self.element["filter3"])
        self.find_element_and_click(**self.element["filter4"])
        self.find_element_and_click(**self.element["filter5"])
        self.find_element_and_click(**self.element["filter6"])
        self.find_element_and_click(**self.element["filter7"])
        self.find_element_and_click(**self.element["filter8"])
        if self.check_element_existence(**self.element["hook_filter"]):
            self.find_element_and_click(**self.element["hook_filter"])
        else:
            pass
        self.find_element_and_click(**self.element["back2"])

    @allure.step("点击存为草稿")
    def click_save_draft(self):
        self.find_element_and_click(**self.element["save_draft"])

    @allure.step("点击直接退出")
    def click_exit_directly(self):
        self.find_element_and_click(**self.element["exit_directly"])

    @allure.step("滑动找到'片尾'")
    def swipe_find_credits(self):
        for i in range(10):
            self.driver.swipe_ext("right", box=(0.841, 0.748, 0.183, 0.748))
        i += 1

    @allure.step("点击变速")
    def click_speed(self):
        self.find_element_and_click(**self.element["speed"])
        # 区域滑动
        self.driver.swipe_ext('right', box=(0.565, 0.915, 0.709, 0.915))
        self.sleep(2)
        self.driver.swipe_ext('right', box=(0.709, 0.915, 0.855, 0.915))
        self.sleep(2)
        self.find_element_and_click(**self.element["hook_speed"])

    @allure.step("点击字幕-下载字幕样式")
    def click_subtitle_style(self):
        self.find_element_and_click(**self.element["subtitle"])
        self.find_element_and_click(**self.element["add_subtitle"])
        self.find_element_and_click(**self.element["subtitle_style1"])
        self.find_element_and_click(**self.element["subtitle_style2"])
        self.find_element_and_click(**self.element["subtitle_style3"])
        # self.find_element_and_input(plaintext="测试文字1", **self.element["input_subtitle"])
        self.find_element_and_click(**self.element["hood_subtitle"])

    @allure.step("点击字幕-添加多条字幕")
    def click_subtitle(self):
        for i in ['一', '二', '三', '四', '五']:
            self.find_element_and_click(**self.element["subtitle"])
            self.find_element_and_click(**self.element["add_subtitle"])
            self.find_element_and_input(plaintext="测试文字" + i, **self.element["input_subtitle"])
            self.find_element_and_click(**self.element["hood_subtitle"])
            self.sleep(1)

    @allure.step("点击字幕-AI字幕")
    def click_ai(self):
        self.find_element_and_click(**self.element["subtitle"])
        self.find_element_and_click(**self.element["ai"])
        if self.check_element_existence(**self.element["hook_ai"]):
            self.find_element_and_click(**self.element["hook_ai"])

    @allure.step("点击音乐-音乐库")
    def click_music(self):
        self.find_element_and_click(**self.element["music"])
        self.find_element_and_click(**self.element["music_library"])
        self.find_element_and_click(**self.element["use_song"])
        self.driver.swipe_ext('right', box=(513, 1819, 714, 1819))
        for i in range(1, 10):
            self.driver.swipe_ext("left", box=(60, 1831, 748, 1831))
        self.driver.swipe_ext('left', box=(330, 1840, 565, 1840, ))
        self.find_element_and_click(**self.element["copy_music"])



