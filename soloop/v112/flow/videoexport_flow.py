#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/29
File: securepay_game_flow.py
"""

import allure

from soloop.v112.page.videoexport_page import VideoExportPage
from soloop.v112.page.main_page import MainPage


class VideoExportFlow(object):

    def __init__(self, driver):
        self.export = VideoExportPage(driver)
        self.mine = MainPage(driver)

    @allure.story("快速成片")
    def fast_filming(self):
        self.export.sleep(1)
        self.export.click_agree()
        self.export.click_enter_main_page()
        self.export.click_fast_film()
        self.export.click_next()
        self.export.click_fragment()
        self.export.click_first_paragraph()
        self.export.click_music_fase()
        self.export.click_filter()
        self.export.click_sd()
        self.export.click_sd1()
        self.export.click_sd2()
        self.export.click_sd3()
        self.export.click_sd4()
        self.export.click_sd()
        self.export.click_generate()
        self.export.click_bar_done()

    @allure.story("自由剪辑")
    def free_editing(self):
        self.export.sleep(1)
        self.export.click_free_edit()
        self.export.click_carry_out()
        self.export.click_cut_up()
        self.export.click_sort()
        self.export.click_cartoon()
        self.export.click_speed()
        self.export.click_reverse()
        self.export.click_rotation()
        self.export.click_music_free()
        self.export.click_preview()
        self.export.click_subtitle()
        self.export.click_filter_free()
        self.export.click_fx()
        self.export.click_generate()
        self.export.click_bar_done()

    @allure.story("点击我的-设置-xxx")
    def main_tab(self):
        self.export.sleep(1)
        self.mine.click_my_tab()
        self.mine.click_resolution()
        self.mine.click_video_watermark()
        self.mine.click_ui_edit()
        self.mine.click_clear_cache()
        self.mine.click_help()
        self.mine.click_user_agreement()
        self.mine.click_privacy_policy()
        self.mine.get_version()



