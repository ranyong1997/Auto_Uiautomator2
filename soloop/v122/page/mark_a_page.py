#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/11
File: mark_a_page.py
"""
import os
import allure

from common.base_page import BasePage
from common.config_parser import ReadConfig
from soloop.v122 import root_dir
from soloop.v122.element.element_router import ElementRouter


class Mark_A_Page(BasePage):

    def __init__(self, driver):
        super(Mark_A_Page, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    @allure.step("点击快速成片")
    def click_fast_film(self):
        self.find_element_and_click(**self.element["fast_film"])

    @allure.step("点击自由剪辑")
    def click_free_edit(self):
        self.find_element_and_click(**self.element["free_edit"])

    @allure.step("点击图片")
    def click_picture(self):
        self.find_element_and_click(**self.element["picture"])

    @allure.step("点击某一张图片")
    def click_select_image1(self):
        self.find_element_and_click(**self.element["select_image1"])

    @allure.step("点击返回上一层")
    def click_back2(self):
        self.find_element_and_click(ignore_toast="已保存到草稿箱", **self.element["back2"])

    @allure.step("点击视频")
    def click_video(self):
        self.find_element_and_click(**self.element["video"])

    @allure.step("点击某一个视频")
    def click_first_video(self):
        self.find_element_and_click(**self.element["first_video"])

    @allure.step("点击下一步")
    def click_pick_done(self):
        self.find_element_and_click(**self.element["pick_done"])
        self.sleep(10)

    @allure.step("点击完成")
    def click_carry_out(self):
        self.find_element_and_click(**self.element["carry_out"])
        self.sleep(3)

    @allure.step("点击模板")
    def click_video_template(self):
        self.find_element_and_click(**self.element["video_template"])

    @allure.step("查找一个片段模板")
    def find_video_template(self):
        self.driver.click(542, 1135)
        for i in range(5):
            if self.driver(**self.element["one_fragments"]).wait():
                self.find_element(**self.element["use_template"]).wait()
            else:
                self.driver.swipe_ext("up")
        self.find_element_and_click(**self.element["use_template"])
        i += 1

    @allure.step("点击使用模板")
    def click_use_template(self):
        self.find_element_and_click(**self.element["use_template"])

    @allure.step("点击生成")
    def click_generate(self):
        self.find_element_and_click(**self.element["generate"])

    @allure.step("点击完成")
    def click_bar_done(self):
        for i in range(3):
            if self.driver(**self.element["bar_done"]).wait():
                self.check_element_existence(**self.element["bar_done"])
            else:
                self.sleep(3)
        i += 1
        self.find_element_and_click(ignore_toast='已保存到草稿箱', **self.element["bar_done"])

    @allure.step("点击分享")
    def click_share(self):
        self.find_element_and_click(**self.element["share"])
        self.sleep(2)
        self.driver.click(164, 1884)
        self.driver.click(164, 1884)

    @allure.step("点击作者头像")
    def click_user_avatar(self):
        self.sleep(1)
        self.find_element_and_click(**self.element["user_avatar"])

    @allure.step("点击转场")
    def click_transitions(self):
        self.driver.click(0.349, 0.727)
        self.find_element_and_click(**self.element["transitions"])

    @allure.step("遍历转场")
    def list_transitions(self):
        self.find_element_and_click(**self.element["transitions_01"])
        self.sleep(1)
        self.find_element_and_click(**self.element["transitions_02"])
        self.sleep(1)
        self.find_element_and_click(**self.element["transitions_03"])
        self.sleep(1)
        self.find_element_and_click(**self.element["transitions_04"])
        self.sleep(1)

    @allure.step("转场-'X'")
    def click_cancel_transitions(self):
        self.find_element_and_click(**self.element["cancel_transitions"])

    @allure.step("转场-'√'")
    def click_hook(self):
        self.find_element_and_click(**self.element["hook"])

    @allure.step("点击音乐")
    def click_music(self):
        self.find_element_and_click(**self.element["music"])

    @allure.step("点击音乐-上下滑动")
    def music_swipe(self):
        for j in range(8):
            self.swipe_screen("left", scale=0.8)
            j += 1
            for i in range(4):
                self.swipe_screen("up", scale=0.2)
                i += 1
                self.sleep(1)

    @allure.step("点击音乐-收藏歌曲")
    def music_collect_song(self):
        self.find_element_and_click(ignore_toast="收藏成功", **self.element["collect_song"])

    @allure.step("点击音乐-下载歌曲")
    def music_download(self):
        self.find_element_and_click(**self.element["download_song"])

    @allure.step("点击音乐-使用歌曲")
    def music_use_song(self):
        self.find_element_and_click(**self.element["use_song"])

    @allure.step("点击画中画")
    def click_pip(self):
        self.find_element_and_click(**self.element["pip"])

    @allure.step("点击画中画-添加")
    def click_add_pip(self):
        self.find_element_and_click(**self.element["add_pip"])

    @allure.step("点击画中画-添加-添加")
    def click_add_pip2(self):
        self.find_element_and_click(**self.element["add_pip2"])

    @allure.step("点击画中画-点击缩略图气泡")
    def click_add_abbreviation(self):
        self.find_element_and_click(**self.element["abbreviation"])
