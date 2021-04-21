#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/28
File: securepay_game_page.py
"""

import allure

from common.base_page import BasePage
from common.config_parser import ReadConfig
from soloop.v112.element.element_router import ElementRouter


class VideoExportPage(BasePage):

    def __init__(self, driver):
        super(VideoExportPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 首次进入(Native) -------------------
    @allure.step("点击同意")
    def click_agree(self):
        # i = 0
        # while i > 0:
        #     if self.check_element_existence(**self.element["agree"]):
        #         self.find_element_and_click(**self.element["agree"])
        #     else:
        #         self.find_element_and_click(**self.element["agree"])
        self.driver(**self.element["agree"]).wait()
        if self.check_element_existence(**self.element["agree"]):
            self.find_element_and_click(**self.element["agree"])

    @allure.step("点击进入首页")
    def click_enter_main_page(self):
        # i = 0
        # while i > 0:
        #     if self.check_element_existence(**self.element["enter_main_page"]):
        #         self.find_element_and_click(**self.element["enter_main_page"])
        #     else:
        #         self.find_element_and_click(**self.element["enter_main_page"])
        self.driver(**self.element["enter_main_page"]).wait()
        if self.check_element_existence(**self.element["enter_main_page"]):
            self.find_element_and_click(**self.element["enter_main_page"])

    @allure.step("点击快速成片")
    def click_fast_film(self):
        self.sleep(2)
        self.find_element_and_click(**self.element["fast_film"])
        self.find_element_and_click(**self.element["picture"])
        self.find_element_and_click(**self.element['select_image2'])

    @allure.step("点击下一步")
    def click_next(self):
        self.find_element_and_click(**self.element["next"])

    @allure.step("点击片段")
    def click_fragment(self):
        self.find_element_and_click(**self.element["fork"])
        self.driver(**self.element["fragment"]).wait()
        self.find_element_and_click(**self.element["fragment"])

    @allure.step("点击第一段")
    def click_first_paragraph(self):
        self.driver(**self.element["first_paragraph"]).wait()
        self.find_element_and_click(**self.element["first_paragraph"])
        self.find_element_and_click(**self.element["second"])
        self.find_element_and_click(**self.element["hook_fragment"])

    @allure.step("点击音乐")
    def click_music_fase(self):
        self.find_element_and_click(**self.element["music"])
        for j in range(6):
            self.swipe_screen("left", scale=0.8)
            j += 1
            for i in range(4):
                self.find_element_and_click(**self.element["collect_song"])
                self.swipe_screen("up", scale=0.15)
                self.find_element_and_click(**self.element["song"])
                i += 1
        self.find_element_and_click(**self.element["use_song"])

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
        self.find_element_and_click(**self.element["hook_filter"])

    @allure.step("点击画幅")
    def click_sd(self):
        self.find_element_and_click(**self.element["sd"])

    @allure.step("点击1:1")
    def click_sd1(self):
        self.find_element_and_click(**self.element["sd1"])

    @allure.step("点击4:3")
    def click_sd2(self):
        self.find_element_and_click(**self.element["sd2"])

    @allure.step("点击3:4")
    def click_sd3(self):
        self.find_element_and_click(**self.element["sd3"])

    @allure.step("点击16:9")
    def click_sd4(self):
        self.find_element_and_click(**self.element["sd4"])

    @allure.step("点击9:16")
    def click_sd5(self):
        self.find_element_and_click(**self.element["sd5"])

    @allure.step("点击生成")
    def click_generate(self):
        self.find_element_and_click(**self.element["generate"])

    @allure.step("点击完成")
    def click_bar_done(self):
        self.find_element_and_click(**self.element["bar_done"])
        self.sleep(1)

    @allure.step("点击自由剪辑")
    def click_free_edit(self):
        self.sleep(2)
        self.find_element_and_click(**self.element["free_edit"])
        self.find_element_and_click(**self.element["video"])
        self.find_element_and_click(**self.element['first_video'])

    @allure.step("点击下一步")
    def click_carry_out(self):
        self.find_element_and_click(**self.element["next"])

    @allure.step("点击分割")
    def click_cut_up(self):
        self.driver(**self.element["primitive"]).wait()
        self.sleep(1)
        self.driver.swipe(0.841, 0.751, 0.583, 0.748)
        self.find_element_and_click(**self.element["cut_up"])

    @allure.step("点击删除")
    def click_delete(self):
        self.find_element_and_click(**self.element["delete"])

    @allure.story("判断功能实现")
    def function_realization(self):
        if self.driver(**self.element["reverse"]).exists():
            print('检查到此元素')
        elif self.driver(**self.element["sort"]).exists():
            print('检查到此元素')
        elif self.driver(**self.element["delete"]).exists():
            print('检查到此元素')
        else:
            print('报错')

    @allure.step("点击排序")
    def click_sort(self):
        self.find_element_and_click(**self.element["sort"])
        self.sleep(1)
        self.driver.drag(0.295, 0.749, 0.041, 0.749, 0.1)
        self.find_element_and_click(**self.element['hook_sort'])

    @allure.step("点击动画")
    def click_cartoon(self):
        self.find_element_and_click(**self.element["cartoon"])
        self.find_element_and_click(**self.element['cartoon1'])
        self.find_element_and_click(**self.element['cartoon2'])
        self.find_element_and_click(**self.element['cartoon3'])
        self.find_element_and_click(**self.element['cartoon4'])
        self.find_element_and_click(**self.element['cartoon5'])
        self.find_element_and_click(**self.element['cartoon6'])
        self.find_element_and_click(**self.element['hook_cartoon'])

    @allure.step("点击变速")
    def click_speed(self):
        self.find_element_and_click(**self.element["speed"])
        # 区域滑动
        self.driver.swipe_ext('right', box=(0.575, 0.86, 0.709, 0.86))
        self.sleep(2)
        self.driver.swipe_ext('right', box=(0.709, 0.86, 0.835, 0.86))
        self.sleep(2)
        self.find_element_and_click(**self.element["hook_speed"])

    @allure.step("点击倒放")
    def click_reverse(self):
        self.driver.swipe(0.874, 0.637, 0.303, 0.637)
        self.find_element_and_click(**self.element["reverse"])

    @allure.step("点击旋转")
    def click_rotation(self):
        i = 1
        while i < 5:
            self.find_element_and_click(**self.element["rotation"])
            i += 1

    @allure.step("点击音乐")
    def click_music_free(self):
        self.find_element_and_click(**self.element["music"])
        self.find_element_and_click(**self.element["music_library"])
        for j in range(6):
            self.driver.swipe_ext("right", box=(0.904, 0.71, 0.097, 0.71))
            j += 1
            for i in range(2):
                self.find_element_and_click(**self.element["collect_song"])
                self.swipe_screen("up", scale=0.15)
                self.find_element_and_click(**self.element["song"])
                i += 1
        self.find_element_and_click(**self.element["use_song"])

    @allure.step("点击贴纸")
    def click_preview(self):
        self.find_element_and_click(**self.element["preview"])
        self.find_element_and_click(**self.element["add_preview"])
        self.sleep(2)
        self.find_element_and_click(**self.element["preview_first"])
        self.sleep(3)
        self.find_element_and_click(**self.element["hook_preview"])
        self.find_element_and_click(**self.element["copy"])
        self.find_element_and_click(**self.element["delete_preview"])

    @allure.step("点击字幕")
    def click_subtitle(self):
        self.find_element_and_click(**self.element["subtitle"])
        self.find_element_and_click(**self.element["add_subtitle"])
        self.find_element_and_input(plaintext="测试文字1", **self.element["input_subtitle"])
        self.find_element_and_click(**self.element["hood_subtitle"])
        self.find_element_and_click(**self.element["ai"])
        self.find_element_and_click(**self.element["hook_ai"])

    @allure.step("点击滤镜")
    def click_filter_free(self):
        self.find_element_and_click(**self.element["filter"])
        self.find_element_and_click(**self.element["filter"])
        self.find_element_and_click(**self.element["filter1"])
        self.find_element_and_click(**self.element["filter2"])
        self.find_element_and_click(**self.element["filter3"])
        self.find_element_and_click(**self.element["filter4"])
        self.find_element_and_click(**self.element["filter5"])
        self.find_element_and_click(**self.element["filter6"])
        self.find_element_and_click(**self.element["filter7"])
        self.find_element_and_click(**self.element["filter8"])

    @allure.step("点击特效")
    def click_fx(self):
        self.find_element_and_click(**self.element["fx"])
        self.find_element_and_click(**self.element["add_fx"])
        self.find_element_and_click(**self.element["first_fx"])
        self.find_element_and_click(**self.element["hook_fx"])
        self.find_element_and_click(**self.element["add"])
        self.find_element_and_click(**self.element["dream_fx"])
        self.find_element_and_click(**self.element["first_dream"])
        self.find_element_and_click(**self.element["hook_fx"])
        self.find_element_and_click(**self.element["add"])
        self.find_element_and_click(**self.element["dynamic_fx"])
        self.find_element_and_click(**self.element["first_dynamic"])
        self.find_element_and_click(**self.element["hook_fx"])
        self.find_element_and_click(**self.element["copy_fx"])
        self.find_element_and_click(**self.element["delete_fx"])
