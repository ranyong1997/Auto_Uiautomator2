#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/3
File: securepay_page.py
"""

import allure

from common.base_page import BasePage
from common.config_parser import ReadConfig
from soloop.v112.element.element_router import ElementRouter


class MainPage(BasePage):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    @allure.step("点击设置")
    def click_my_tab(self):
        self.driver(**self.element["my_tab"]).wait()
        self.find_element_and_click(**self.element["my_tab"])

    @allure.step("点击用户头像进行登录")
    def click_account(self):
        self.find_element_and_click(**self.element["account"])

    @allure.step("点击导出分辨率")
    def click_resolution(self):
        self.find_element_and_click(**self.element["resolution"])
        self.find_element_and_click(**self.element["720P"])

    @allure.step("点击视频水印")
    def click_video_watermark(self):
        self.find_element_and_click(**self.element["video_watermark"])

    @allure.step("点击智能剪辑助手")
    def click_ui_edit(self):
        self.find_element_and_click(**self.element["ui_edit"])

    @allure.step("点击清理缓存")
    def click_clear_cache(self):
        self.find_element_and_click(ignore_toast="缓存清理成功", **self.element["clear_cache"])

    @allure.step("点击帮助与反馈")
    def click_help(self):
        self.find_element_and_click(**self.element["help"])
        self.sleep(1)
        self.press_key("back")

    @allure.step("点击用户协议")
    def click_user_agreement(self):
        self.find_element_and_click(**self.element["user_agreement"])
        self.sleep(1)
        self.press_key("back")

    @allure.step("点击隐私政策")
    def click_privacy_policy(self):
        self.find_element_and_click(**self.element["privacy_policy"])
        self.sleep(1)
        self.find_element_and_click(**self.element["back"])

    @allure.step("获取版本号")
    def get_version(self):
        version = self.driver.app_info("com.coloros.videoeditor")
        print(version)

    @allure.step("未登录oppo账号")
    def get_version(self):
        version = self.driver.app_info("com.coloros.videoeditor")
        print(version)

    @allure.step("点击账号")
    def click_user(self, mobile_number):
        self.find_element_and_click(**self.element["user"])
        self.driver.send_keys(mobile_number, clear=True)

    @allure.step("点击账号密码登录")
    def click_u_p_login(self):
        self.find_element_and_click(**self.element["u_p_login"])

    @allure.step("点击输入密码")
    def click_password(self, password):
        self.driver.send_keys(password, clear=True)

    @allure.step("点击登录")
    def click_login(self):
        self.find_element_and_click(**self.element["login"])

    @allure.step("点击签到")
    def click_sign_in(self):
        if not self.driver(**self.element['signed']).wait():
            self.find_element_and_click(**self.element["sign_in"])
        else:
            pass
