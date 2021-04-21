#!/usr/bin/env python
# -*- coding:utf-8 -*-

import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class MessagePage(BasePage):

    def __init__(self, driver):
        super(MessagePage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 消息分类 -------------------
    @allure.step("点击系统消息")
    def click_system_message(self):
        self.find_element_and_click(check_toast=False, **self.element["system_message"])

    @allure.step("点击活动提醒")
    def click_activity_message(self):
        self.find_element_and_click(check_toast=False, **self.element["activity_msg"])

    @allure.step("点击动账提醒")
    def click_bill_message(self):
        self.find_element_and_click(check_toast=False, **self.element["bill_message"])

    @allure.step("点击银行卡")
    def click_bank_card(self):
        self.find_element_and_click(check_toast=False, **self.element["bank_card"])

    @allure.step("长按银行卡")
    def long_click_bank_card(self):
        self.find_element_and_long_click(**self.element["bank_card"])

    @allure.step("点击公交卡")
    def click_transit_card(self):
        self.find_element_and_click(check_toast=False, **self.element["transit_card"])

    @allure.step("长按公交卡")
    def long_click_transit_card(self):
        self.find_element_and_long_click(**self.element["transit_card"])

    @allure.step("点击门禁卡")
    def click_door_card(self):
        self.find_element_and_click(check_toast=False, **self.element["door_card"])

    @allure.step("长按门禁卡")
    def long_click_door_card(self):
        self.find_element_and_long_click(**self.element["door_card"])

    # ----------------- 消息详情 -------------------
    @allure.step("检查消息主标题")
    def check_message_main_title(self, message_main_title):
        element = self.element["message_main_title"]
        element["textContains"] = message_main_title
        self.check_element_existence(**element)

