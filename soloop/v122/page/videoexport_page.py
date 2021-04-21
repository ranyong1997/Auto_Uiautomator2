#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/28
File: securepay_game_page.py
"""

import allure
from common.base_page import BasePage
from soloop.v122.element.element_router import ElementRouter


class VideoExportPage(BasePage):

    def __init__(self, driver):
        super(VideoExportPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 首次进入(initialization) -------------------
    @allure.step("点击同意并使用、进入首页")
    def click_agree_and_use(self):
        self.driver(**self.element["agree_and_use"]).wait()
        if self.check_element_existence(**self.element["agree_and_use"]):
            self.find_element_and_click(**self.element["agree_and_use"])
        elif self.check_element_existence(**self.element["enter_main_page"]):
            self.find_element_and_click(**self.element["enter_main_page"])

    # ----------------- 快速成片(fast_film) -------------------
    @allure.step("点击快速成片")
    def click_fast_film(self):
        self.sleep(3)
        self.driver.click(0.565, 0.1)
        self.find_element_and_click(**self.element["fast_film"])

    @allure.step("选择素材")
    def fast_choose_material(self):
        self.find_element_and_click(**self.element["picture"])
        self.find_element_and_click(**self.element['select_image2'])

    @allure.step("点击完成")
    def click_finish(self):
        self.find_element_and_click(**self.element["carry_out"])

    @allure.step("清理一些带×的弹框")
    def click_fork(self):
        self.sleep(1)
        if self.check_element_existence(**self.element["fork"]):
            self.find_element_and_click(**self.element["fork"])

    @allure.step("点击片段")
    def click_fragment(self):
        self.driver(**self.element["fragment"]).wait()
        self.find_element_and_click(**self.element["fragment"])

    @allure.step("点击第一段")
    def click_first_paragraph(self):
        self.driver(**self.element["first_paragraph"]).wait()
        self.find_element_and_click(**self.element["first_paragraph"])

    @allure.step("选择第二张照片")
    def select_the_second_photo(self):
        self.find_element_and_click(**self.element["second"])
        self.find_element_and_click(**self.element["hook_fragment"])

    @allure.step("点击音乐")
    def click_music(self):
        self.sleep(1)
        self.find_element_and_click(**self.element["music"])
        for j in range(3):
            self.driver.swipe_ext("right", box=(0.846, 0.688, 0.175, 0.688))  # 区域滑动
            j += 1
            for i in range(4):
                self.find_element_and_click(check_toast=False, **self.element["collect_song"])
                self.swipe_screen("up", scale=0.2)
                self.find_element_and_click(**self.element["download_song"])
                i += 1
        self.find_element_and_click(check_toast=True, **self.element["use_song"])

    @allure.step("点击滤镜")
    def click_filter(self):
        self.find_element_and_click(**self.element["filter"])
        self.find_element_and_click(**self.element["filter1"])
        self.find_element_and_click(**self.element["filter2"])
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

    @allure.step("点击16:9")
    def click_sd3(self):
        self.find_element_and_click(**self.element["sd3"])

    @allure.step("点击9:16")
    def click_sd4(self):
        self.find_element_and_click(**self.element["sd4"])
        self.driver.click(113, 740)

    @allure.step("点击生成")
    def click_generate(self):
        self.find_element_and_click(**self.element["generate"])

    @allure.step("点击完成")
    def click_bar_done(self):
        self.find_element_and_click(ignore_toast="已保存到草稿箱", **self.element["bar_done"])
        self.sleep(2)

    # ----------------- 自由剪辑(free_edit) -------------------
    @allure.step("点击自由剪辑")
    def click_free_edit(self):
        self.sleep(2)
        self.find_element_and_click(**self.element["free_edit"])
        self.find_element_and_click(**self.element["go_back"])
        self.find_element_and_click(**self.element["free_edit"])

    @allure.step("自由剪辑选择素材")
    def free_choose_material(self):
        self.find_element_and_click(**self.element["picture"])
        self.find_element_and_click(**self.element['select_image2'])

    @allure.step("点击分割")
    def click_cut_up(self):
        self.driver(**self.element["primitive"]).wait()
        self.driver.swipe(0.841, 0.751, 0.583, 0.748)
        self.find_element_and_click(**self.element["cut_up"])
        self.sleep(1)
        self.driver.click(374, 2006)

    @allure.step("点击删除")
    def click_delete(self):
        self.find_element_and_click(**self.element["delete"])
        self.find_element_and_click(**self.element["undo"])

    @allure.step("点击剪辑")
    def click_film_editing(self):
        self.find_element_and_click(**self.element["film_editing"])

    @allure.step("点击排序")
    def click_sort(self):
        self.find_element_and_click(**self.element["sort"])
        self.sleep(1)
        self.driver.drag(0.085, 0.800, 0.365, 0.800, 0.1)
        self.find_element_and_click(**self.element['hook'])

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
        self.find_element_and_click(**self.element["swipe_speed"])
        # self.driver.click(540, 2133)
        self.find_element_and_click(**self.element['hook_speed'])

    @allure.step("点击背景")
    def click_background(self):
        self.sleep(1)
        self.find_element_and_click(**self.element["background"])

    def click_solid_color(self):
        """点击纯色"""
        self.find_element_and_click(**self.element["solid_color"])

    def click_blurry(self):
        """点击模糊"""
        self.find_element_and_click(**self.element["blurry"])

    def click_background_apply_all(self):
        """点击应用到全部片段"""
        self.find_element_and_click(ignore_toast="已应用到全部片段", **self.element["background_apply_all"])
        self.find_element_and_click(**self.element["hook_bg"])

    def click_pattern(self):
        """点击图案"""
        self.find_element_and_click(**self.element["pattern"])
        self.find_element_and_click(**self.element["pattern_one"])
        self.find_element_and_click(**self.element["hook_bg"])
        self.driver.swipe_ext("right", box=(880, 1660, 234, 1660))   # 区域滑动

    @allure.step("点击替换")
    def click_replace(self):
        self.driver.swipe_ext("right", box=(880, 1660, 234, 1660))   # 区域滑动
        self.find_element_and_click(**self.element["replace"])
        self.find_element_and_click(**self.element["video"])
        self.find_element_and_click(**self.element['replace_video'])
        self.find_element_and_click(**self.element['choose'])

    @allure.step("点击倒放")
    def click_reverse(self):
        self.driver.swipe_ext("right", box=(880, 1660, 234, 1660))   # 区域滑动
        self.find_element_and_click(**self.element["reverse"])
        self.sleep(3)

    @allure.step("点击旋转")
    def click_rotation(self):
        self.sleep(1)
        self.driver.swipe_ext("right", box=(880, 1660, 234, 1660))   # 区域滑动
        i = 1
        while i < 5:
            self.find_element_and_click(**self.element["rotation"])
            i += 1
            continue

    @allure.step("点击贴纸")
    def click_preview(self):
        self.sleep(1)
        self.find_element_and_click(**self.element["preview"])
        self.find_element_and_click(**self.element["preview_first"])
        self.sleep(2)
        self.find_element_and_click(**self.element["hook_preview"])
        self.find_element_and_click(**self.element["copy"])
        self.find_element_and_click(**self.element["delete_preview"])
        self.find_element_and_click(**self.element["text_preview"])
        self.find_element_and_input(plaintext="测试文字1", **self.element["input_text"])
        self.find_element_and_click(**self.element["hook_input"])
        # self.find_element_and_click(**self.element["ai"])
        self.find_element_and_click(**self.element["editor"])
        self.find_element_and_click(**self.element["hook_input"])
        self.find_element_and_click(**self.element["delete_text"])
        self.find_element_and_click(**self.element["track_preview"])

    @allure.step("点击文字")
    def click_text(self):
        self.find_element_and_click(**self.element["text"])

    @allure.step("点击滤镜")
    def click_filter_free(self):
        self.find_element_and_click(**self.element["filter"])
        self.find_element_and_click(**self.element["filter_first"])
        if self.check_element_existence(**self.element["hook_filter"]):
            self.find_element_and_click(**self.element["hook_filter"])

    @allure.step("点击特效")
    def click_fx(self):
        self.find_element_and_click(**self.element["fx"])
        self.find_element_and_click(**self.element["add_fx"])
        self.find_element_and_click(**self.element["first_fx"])
        self.find_element_and_click(**self.element["hook_fx"])
        self.find_element_and_click(**self.element["add_fx"])
        self.find_element_and_click(**self.element["dream_fx"])
        self.find_element_and_click(**self.element["first_dream"])
        self.find_element_and_click(**self.element["hook_fx"])
        self.find_element_and_click(**self.element["add_fx"])
        self.find_element_and_click(**self.element["dynamic_fx"])
        self.find_element_and_click(**self.element["first_dynamic"])
        self.find_element_and_click(**self.element["hook_fx"])
        self.find_element_and_click(**self.element["copy_fx"])
        self.find_element_and_click(**self.element["delete_fx"])

    @allure.step("点击画中画")
    def click_pip(self):
        self.find_element_and_click(**self.element["pip"])
        self.find_element_and_click(**self.element["add_pip"])
        self.find_element_and_click(**self.element["video"])
        self.find_element_and_click(**self.element["first_video"])
        self.driver(**self.element["cut_pip"]).wait()
        self.driver.swipe(0.841, 0.751, 0.583, 0.748)
        self.find_element_and_click(**self.element["cut_pip"])
        self.find_element_and_click(**self.element["volume_pip"])
        self.sleep(1)
        self.driver.click(0.695, 0.872)    # 画中画音量
        self.find_element_and_click(**self.element["hook_volume"])
        self.find_element_and_click(**self.element["cartoon_pip"])
        self.find_element_and_click(**self.element["up_swipe"])    # 向上滑动 动画
        self.find_element_and_click(**self.element["hook_cartoon"])
        self.find_element_and_click(**self.element["filter_pip"])   # 滤镜
        self.find_element_and_click(**self.element["filter_first"])   # 第一个滤镜
        self.find_element_and_click(**self.element["hook_filter_pip"])
        self.find_element_and_click(**self.element["hierarch_pip"])
        self.check_element_existence(**self.element["three_bars"])
        self.find_element_and_click(**self.element["hook_blend"])
        self.driver.swipe_ext('left', box=(0.387, 0.7, 0.884, 0.7))   # 区域滑动
        self.find_element_and_click(**self.element["blend_pip"])
        self.find_element_and_click(**self.element["second_blend"])
        self.find_element_and_click(**self.element["hook_blend"])
