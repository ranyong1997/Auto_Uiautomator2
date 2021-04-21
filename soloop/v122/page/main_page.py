#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/3
File: securepay_page.py
"""

import allure

from common.base_page import BasePage
from common.utils import get_installed_package_name
from common.config_parser import ReadConfig
from soloop.v122.element.element_router import ElementRouter


class MainPage(BasePage):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    @allure.step("点击我的")
    def click_my_tab(self):
        self.sleep(2)
        self.driver(**self.element["my_tab"]).wait()
        self.find_element_and_click(**self.element["my_tab"])

    @allure.step("点击用户头像进行登录")
    def click_account(self):
        self.find_element_and_click(**self.element["account"])

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

    @allure.step("点击设置")
    def click_features(self):
        self.find_element_and_click(**self.element["features"])

    @allure.step("点击视频水印")
    def click_video_watermark(self):
        self.find_element_and_click(**self.element["video_watermark"])

    @allure.step("点击智能剪辑助手")
    def click_uiedit(self):
        self.find_element_and_click(**self.element["uiedit"])

    @allure.step("点击清理缓存")
    def click_clear_cache(self):
        self.find_element_and_click(ignore_toast="缓存清理成功", **self.element["clear_cache"])

    @allure.step("点击帮助与反馈")
    def click_help(self):
        self.find_element_and_click(**self.element["help"])
        self.sleep(1)

    @allure.step("点击我要反馈")
    def click_feedback(self):
        self.find_element_and_click(**self.element["feedback"])

    @allure.step("反馈内容")
    def click_feedback_content(self):
        self.driver.click(0.439, 0.297)
        # self.find_element_and_input(plaintext="测试反馈", **self.element["feedback"])
        self.driver.send_keys("测试反馈")
        self.find_element_and_swipe("up", scale=0.5)

    @allure.step("联系方式")
    def input_contact_details(self):
        self.driver.click(0.483, 0.512)
        # self.find_element_and_input(plaintext="123456", **self.element["contact_details"])
        self.driver.send_keys("123456")

    @allure.step("提交")
    def click_submit(self):
        self.find_element_and_click(**self.element["submit"])
        self.press_key("back")
        self.press_key("back")

    @allure.step("点击用户协议")
    def click_user_agreement(self):
        self.find_element_and_click(**self.element["user_agreement"])
        self.press_key("back")

    @allure.step("点击隐私政策")
    def click_privacy_policy(self):
        self.sleep(1)
        self.find_element_and_click(**self.element["privacy_policy"])
        self.scroll_to_boundary("end", "fast")
        self.find_element_and_click(**self.element["back"])

    @allure.step("获取版本号")
    def get_version(self):
        version = self.driver.app_info("com.coloros.videoeditor")
        print(version)
