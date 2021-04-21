#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from wallet.v390.page import CommonPage


class CommonFlow(object):

    def __init__(self, driver):
        self.common_page = CommonPage(driver)

    @allure.story("从通知栏复制验证码操作")
    def copy_verification_code_from_notification(self):
        self.common_page.sleep(5.0)
        self.common_page.open_notification()
        self.common_page.click_sys_copy_verification_code()
        self.common_page.press_key("back")

    @allure.story("从短信复制验证码操作")
    def copy_verification_code_from_mms(self):
        # 注意这个需要事先清理信息中的heytap短信，否则每次都会点第一个复制验证码按钮，不推荐使用
        self.common_page.start_mms()
        self.common_page.click_notices()
        self.common_page.click_heytap()
        self.common_page.click_mms_copy_verification_code()
        self.common_page.start_wallet()
