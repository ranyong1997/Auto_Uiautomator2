#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/11
File: securepay_flow.py
"""

import allure

from soloop.v122.page.videoexport_page import VideoExportPage
from soloop.v122.page.mark_a_page import Mark_A_Page
from soloop.v122.page.main_page import MainPage


class Pytest_Mark_a_Flow(object):

    def __init__(self, driver):
        self.export = VideoExportPage(driver)
        self.A = Mark_A_Page(driver)
        self.mine = MainPage(driver)

    @allure.story("检查“使用模板”可以正常使用")
    def use_template(self):
        self.A.click_video_template()
        self.A.find_video_template()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_pick_done()
        self.A.click_generate()
        self.A.click_bar_done()

    @allure.story("检查“使用模板”点赞及分享功能")
    def like_share(self):
        self.A.click_video_template()
        self.A.driver.double_click(653, 1171, duration=0.1)
        self.A.click_share()

    @allure.story("点击达人头像进入达人主页")
    def like_share2(self):
        self.A.click_video_template()
        self.A.click_user_avatar()
        self.A.click_video_template()
        self.A.find_video_template()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_pick_done()
        self.A.click_generate()
        self.A.click_bar_done()

    @allure.story("查看是否可以正常登录")
    def click_mine(self):
        self.mine.click_my_tab()
        self.mine.click_account()

    @allure.story("查看是否可以正常登录")
    def login(self, **kwargs):
        self.mine.click_user(kwargs["mobile_number"])
        self.mine.click_u_p_login()
        self.mine.click_password(kwargs["password"])
        self.mine.click_login()

    @allure.story("登录后是否可以签到")
    def click_sign_in(self):
        self.mine.click_my_tab()
        self.mine.click_sign_in()

    @allure.story("检查无操作返回的状态")
    def no_operation_returns(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.A.click_back2()

    @allure.story("检查有操作返回的状态")
    def operation_returns(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.A.click_back2()

    @allure.story("检查转场效果功能")
    @allure.description('点击转场按钮，查看是否弹出弹层默认选中情况')  # 注释说明
    def click_transitions_1(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.A.click_transitions()

    @allure.story("检查转场效果功能")
    @allure.description('切换其它转场效果，查看是否支持预览')  # 注释说明
    def click_transitions_2(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.A.click_transitions()
        self.A.list_transitions()

    @allure.story("检查转场效果功能")
    @allure.description('点击“X”，不应用已预览的转场效果')  # 注释说明
    def click_transitions_3(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.A.click_transitions()
        self.A.click_cancel_transitions()

    @allure.story("检查转场效果功能")
    @allure.description('点击“√”，应用已预览的转场效果')  # 注释说明
    def click_transitions_4(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.A.click_transitions()
        self.A.list_transitions()
        self.A.click_hook()

    @allure.story("点击动画，添加任意动画，查看是否可以正常预览和添加")
    def click_cartoon(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.export.click_cartoon()

    @allure.story("点击动画，添加任意动画，查看是否可以正常预览和添加")
    def click_sort(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.export.click_sort()

    @allure.story("点击排序，更换片段顺序，查看是否可以正常排序")
    def click_speed(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.export.click_speed()

    @allure.story("点击背景，缩小视频画面，点击模糊背景，应用到全部片段，查看背景是否生效")
    def click_background(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_cut_up()
        self.export.click_sd()
        self.export.click_sd2()
        self.export.click_sd()
        self.export.click_background()
        self.export.click_blurry()
        self.export.click_background_apply_all()

    @allure.story("点击倒放，查看是否可以正常倒放")
    def click_reverse(self):
        self.A.click_free_edit()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_carry_out()
        self.export.click_reverse()

    @allure.story("点击替换，查看是否可以正常替换片段")
    def click_replace(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_replace()

    @allure.story("点击旋转，查看是否可以正常旋转视频片段")
    def click_rotation(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.export.click_rotation()

    @allure.story("上下左右滑动音乐分类界面，查看是否可以正常滑动不卡顿")
    def click_music_swipe(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.A.click_music()
        self.A.music_swipe()

    @allure.story("点击收藏按钮，查看收藏分类里是否有收藏的音乐")
    def click_collect(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.A.click_music()
        self.A.music_collect_song()

    @allure.story("点击下载歌曲，查看是否可以正常下载歌曲")
    def click_download(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.A.click_music()
        self.A.music_download()

    @allure.story("点击使用，查看是否可以使用选中的音乐")
    def click_use_song(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.A.click_music()
        self.A.music_download()
        self.A.music_use_song()

    @allure.story("检查剪辑tab画中画气泡")
    def click_pip(self):
        self.export.click_free_edit()
        self.export.free_choose_material()
        self.export.click_finish()
        self.A.click_pip()
        self.A.click_add_pip()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_add_pip2()
        self.A.click_video()
        self.A.click_first_video()
        self.export.click_film_editing()
        self.A.click_add_abbreviation()



