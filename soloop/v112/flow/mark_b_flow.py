#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/11
File: securepay_flow.py
"""

import allure

from soloop.v112.page.videoexport_page import VideoExportPage
from soloop.v112.page.mark_b_page import Mark_B_Page
from soloop.v112.page.main_page import MainPage


class Pytest_Mark_b_Flow(object):

    def __init__(self, driver):
        self.export = VideoExportPage(driver)
        self.B = Mark_B_Page(driver)
        self.mine = MainPage(driver)

    @allure.story("查看是否可以正常登录")
    def login(self, **kwargs):
        self.mine.click_my_tab()
        self.mine.click_account()
        self.mine.click_user(kwargs["mobile_number"])
        self.mine.click_u_p_login()
        self.mine.click_password(kwargs["password"])
        self.mine.click_login()

    @allure.story("登录后是否可以签到")
    def click_sign_in(self):
        self.mine.click_my_tab()
        self.mine.click_sign_in()



