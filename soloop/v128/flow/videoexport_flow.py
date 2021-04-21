#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/29
File: securepay_game_flow.py
"""

import allure

from soloop.v128.page.videoexport_page import VideoExportPage
from soloop.v128.page.main_page import MainPage


class VideoExportFlow(object):

    def __init__(self, driver):
        self.export = VideoExportPage(driver)
        self.mine = MainPage(driver)

    @allure.story("快速成片")
    def fast_filming(self):
        self.export.click_agree_and_use()
        self.export.click_fast_film()
        self.export.fast_choose_material()
        self.export.click_finish()
        self.export.click_fork()
        self.export.click_fragment()
        self.export.click_first_paragraph()
        self.export.select_the_second_photo()
        self.export.click_music()
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
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.export.click_sort()
        self.export.click_cartoon()
        self.export.click_speed()
        self.export.click_sd()
        self.export.click_sd2()
        self.export.click_sd()
        self.export.click_background()
        self.export.click_solid_color()
        self.export.click_blurry()
        self.export.click_pattern()
        self.export.click_replace()
        self.export.click_reverse()
        self.export.click_rotation()
        self.export.click_preview()
        self.export.click_text()
        self.export.click_filter_free()
        self.export.click_fx()
        self.export.click_pip()
        self.export.click_music()
        self.export.click_generate()
        self.export.click_bar_done()

    @allure.story("点击我的-设置-xxx")
    def main_tab(self):
        self.mine.click_my_tab()
        self.mine.click_features()
        self.mine.click_video_watermark()
        self.mine.click_uiedit()
        self.mine.click_clear_cache()
        self.mine.click_help()
        self.mine.click_feedback()
        self.mine.click_contact_details()
        self.mine.click_feedback_content()
        self.mine.input_contact_details()
        self.mine.click_submit()
        self.mine.click_user_agreement()
        self.mine.click_privacy_policy()
        self.mine.get_version()






