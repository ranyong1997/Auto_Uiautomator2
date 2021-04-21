#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/11
File: securepay_flow.py
"""

import allure

from soloop.v112.page.videoexport_page import VideoExportPage
from soloop.v112.page.mark_a_page import Mark_A_Page


class Pytest_Mark_a_Flow(object):

    def __init__(self, driver):
        self.export = VideoExportPage(driver)
        self.A = Mark_A_Page(driver)

    @allure.story("检查素材可正常预览")
    def material_preview(self):
        self.A.click_fast_film()
        self.A.click_picture()
        self.A.click_preview_material()
        self.A.click_checkbox()
        self.A.click_back()
        self.A.click_video()
        self.A.click_preview_material()
        self.A.click_checkbox()
        self.A.click_back()
        self.A.click_next()
        self.A.driver.press("back")
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_preview_material()
        self.A.click_checkbox()
        self.A.click_back()
        self.A.click_video()
        self.A.click_preview_material()
        self.A.click_checkbox()
        self.A.click_back()
        self.A.click_next()

    @allure.story("检查滤镜功能是否正常")
    def filter_display(self):
        self.A.click_fast_film()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.A.click_filter()
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.A.click_filter()

    @allure.story("检查无操作返回的状态")
    def no_operation_returns(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.A.click_back2()
        self.A.sleep(10)

    @allure.story("检查有操作返回点击空白区域")
    def operation_blank(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.export.click_cut_up()
        self.A.click_back2()
        self.A.driver.click(500, 895)

    @allure.story("检查有操作返回直接退出的状态")
    def operation_returns_exit(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.export.click_cut_up()
        self.A.click_back2()
        self.A.click_exit_directly()

    @allure.story("检查有操作返回存为草稿的状态")
    def operation_returns_save(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.export.click_cut_up()
        self.A.click_back2()
        self.A.click_save_draft()

    @allure.story("检查手动剪辑删除功能")
    @allure.description('导入一个素材时，检查删除按钮是否可用')  # 注释说明
    def clip_delete1(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_next()
        # self.export.click_delete()
        self.export.function_realization()
        print('删除按钮置灰不可点击')

    @allure.story("检查手动剪辑删除功能")
    @allure.description('导入2个素材,点击删除,查看选中视频或片段是否删除成功')  # 注释说明
    def clip_delete2(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.export.click_delete()
        print('删掉对应的片段或者视频')

    @allure.story("检查手动剪辑删除功能")
    @allure.description('选择片尾，点击“删除”，查看片尾是否可以删除')  # 注释说明
    def clip_delete3(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.A.swipe_find_credits()
        self.export.click_delete()
        print('片尾删除，位置保留')

    @allure.story("检查手动剪辑排序功能")
    @allure.description('导入一个素材时，查看排序是否可用')  # 注释说明
    def sorting_function1(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_next()
        self.export.function_realization()

    @allure.story("检查手动剪辑排序功能")
    @allure.description('导入二个素材时，查看排序是否可用')  # 注释说明
    def sorting_function2(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.A.click_sort()

    @allure.story("检查剪辑tab动画，排序，变速等功能")
    @allure.description('点击动画，添加任意动画，查看是否可以正常预览和添加')  # 注释说明
    def click_cartoon(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_next()
        self.export.click_cartoon()

    @allure.story("检查剪辑tab动画，排序，变速等功能")
    @allure.description('点击变速，调节变速条，查看是否可以正常调节倍速')  # 注释说明
    def click_speed(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_next()
        self.A.click_speed()

    @allure.story("倒放素材后检查视频画面")
    @allure.description('选择图片，查看倒放按钮')  # 注释说明
    def click_reverse1(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_next()
        self.A.driver.swipe(872, 1533, 277, 1533)
        self.export.function_realization()

    @allure.story("倒放素材后检查视频画面")
    @allure.description('选择视频，查看倒放按钮')  # 注释说明
    def click_reverse2(self):
        self.A.click_free_edit()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.export.click_reverse()

    @allure.story("检查音乐分类功能")
    @allure.description('上下左右滑动音乐分类界面，正常滑动不卡顿')  # 注释说明
    def click_music(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_next()
        self.export.click_music_free()

    @allure.story("检查字幕功能可正常添加")
    @allure.description('添加字幕，下载并应用字幕样式，点击“√”产看是否回到字幕tab页')  # 注释说明
    def click_subtitle_style(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_next()
        self.A.click_subtitle_style()

    @allure.story("检查字幕功能可正常添加")
    @allure.description('在同一时间轴位置添加多个字幕，查看字幕轴下方字幕图标是否可以显示对应的图标数量')  # 注释说明
    def click_subtitle(self):
        self.A.click_free_edit()
        self.A.click_picture()
        self.A.click_select_image1()
        self.A.click_next()
        self.A.click_subtitle()

    @allure.story("检查AI字幕功能可正常添加")
    @allure.description('点击AI字幕按钮，查看是否可以识别出AI字幕')  # 注释说明
    def click_ai(self):
        self.A.click_free_edit()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.A.click_ai()

    @allure.story("查看打开音乐调整页面")
    @allure.description('选中音乐轨，查看是否可以拖动把手')  # 注释说明
    def click_music2(self):
        self.A.click_free_edit()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.A.click_music()

    @allure.story("查看贴纸可正常添加使用")
    def click_preview(self):
        self.A.click_free_edit()
        self.A.click_video()
        self.A.click_first_video()
        self.A.click_next()
        self.export.click_preview()

