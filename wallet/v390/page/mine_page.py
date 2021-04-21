#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class MinePage(BasePage):

    def __init__(self, driver):
        super(MinePage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- Tab -------------------
    @allure.step("点击我的")
    def click_mine_tab(self):
        self.sleep(3.0)
        self.find_element_and_click(check_toast=False, **self.element["mine_tab"])

    # ----------------- 消息中心入口 -------------------
    @allure.step("点击消息中心")
    def click_message_center(self):
        self.find_element_and_click(**self.element["message_center"])

    # ----------------- 设置入口 -------------------
    @allure.step("点击设置")
    def click_setting(self):
        self.find_element_and_click(**self.element["setting"])

    # ----------------- 账号&签到&积分 -------------------
    @allure.step("点击账号")
    def click_account_number(self):
        self.find_element_and_click(**self.element["account_number"])

    @allure.step("点击签到")
    def click_sign_in(self):
        self.find_element_and_click(**self.element["sign_in"])

    @allure.step("点击X关闭")
    def click_close(self):
        self.find_element_and_click(**self.element["close"])

    @allure.step("点击积分")
    def click_integration(self):
        self.find_element_and_click(**self.element["integration"])

    # ----------------- 红包入口 -------------------
    @allure.step("点击红包")
    def click_red_envelope(self):
        self.find_element_and_click(**self.element["red_envelope"])

    # ----------------- 优惠券入口 -------------------
    @allure.step("点击优惠券")
    def click_coupon(self):
        self.find_element_and_click(**self.element["coupon"])

    # ----------------- 我的资产 -------------------
    @allure.step("点击我的资产")
    def click_my_assets(self):
        self.find_element_and_click(check_toast=False, **self.element["my_assets"])

    @allure.step("点击我的保障")
    def click_my_protection(self):
        self.find_element_and_click(check_toast=False, **self.element["my_protection"])

    @allure.step("点击我的借钱")
    def click_my_loan(self):
        self.find_element_and_click(check_toast=False, **self.element["my_loan"])

    @allure.step("点击眼睛")
    def click_eye(self):
        self.find_element_and_click(check_toast=False, **self.element["eye"])

    @allure.step("点击零钱")
    def click_change(self):
        self.find_element_and_click(check_toast=False, **self.element["change"])
