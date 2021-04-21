'''
Descripttion: 
version: 
Author: 冉勇
Date: 2021-04-01 18:51:28
LastEditTime: 2021-04-01 18:56:24
'''
'''
Descripttion: 
version: 
Author: 冉勇
Date: 2021-04-01 18:51:28
LastEditTime: 2021-04-01 18:56:12
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class ThirdPartyPage(BasePage):

    def __init__(self, driver):
        super(ThirdPartyPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 三方服务 -------------------
    @allure.step('点击{0}服务')
    def click_service(self, service_name):
        element = self.element["service_name"]
        element["textContains"] = service_name
        # self.scroll_until_element_appear(**element)
        self.scroll_to_boundary("end")
        self.find_element_and_click(**element)

    @allure.step('点击关闭(快应用)')
    def click_quickapp_close(self):
        self.find_element_and_click(**self.element["quickapp_close"])

    @allure.step('点击退出(可币充值)')
    def click_cocoin_exit(self):
        self.find_element_and_click(**self.element["cocoin_exit"])
