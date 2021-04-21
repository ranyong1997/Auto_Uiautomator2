#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class HomePage(BasePage):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- Tab -------------------
    @allure.step("点击首页")
    def click_home_tab(self):
        self.find_element_and_click(**self.element["home_tab"])

    # ----------------- 工具栏 -------------------
    @allure.step("点击OPPO Pay")
    def click_oppo_pay(self):
        self.find_element_and_click(**self.element["oppo_pay"])

    @allure.step("点击付款码")
    def click_payment_code(self):
        self.find_element_and_click(**self.element["payment_code"])

    @allure.step("点击扫一扫")
    def click_scan_it(self):
        self.find_element_and_click(**self.element["scan_it"])

    @allure.step("点击卡包")
    def click_card_package(self):
        self.sleep(3.0)
        self.find_element_and_click(**self.element["card_package"])

    @allure.step("点击去乘车")
    def click_go_by_bus(self):
        self.find_element_and_click(**self.element["go_by_bus"])

    @allure.step("点击去开门")
    def click_go_open_door(self):
        self.find_element_and_click(**self.element["go_open_door"])

    # ----------------- 卡包 -------------------
    @allure.step("点击+(顶部)")
    def click_add(self):
        self.find_element_and_click(**self.element["add"])

    @allure.step("点击其他设备的卡片")
    def click_Cards_for_other_devices(self):
        self.find_element_and_click(**self.element["Cards_for_other_devices"])

    @allure.step("点击添加门禁卡")
    def click_add_key(self):
        self.find_element_and_click(**self.element["add_key"])

    @allure.step("点击添加银行卡")
    def click_add_bank_card(self):
        self.find_element_and_click(**self.element["add_bank_card"])

    @allure.step("点击添加公交卡")
    def click_add_transit_card(self):
        self.find_element_and_click(**self.element["add_transit_card"])

    @allure.step("点击添加eID")
    def click_add_eID(self):
        self.find_element_and_click(**self.element["add_eID"])

    @allure.step("点击管理其他设备的卡片")
    def click_manager_other_device_card(self):
        self.find_element_and_click(**self.element["manager_other_device_card"])

    @allure.step("点击空白卡的待录入")
    def click_write_in_of_blank_card(self):
        self.find_element_and_click(**self.element["write_in_of_blank_card"])

    @allure.step("点击银行卡中的第一张卡")
    def click_first_bank_card(self):
        self.find_element_and_click(**self.element["first_bank_card"])

    @allure.step("点击公交卡的充值")
    def click_recharge(self):
        self.find_element_and_click(**self.element["recharge"])

    @allure.step("点击公民网络电子身份标识")
    def click_eID(self):
        self.scroll_until_element_appear(**self.element["eID"])
        self.find_element_and_click(**self.element["eID_image"])

    # ----------------- 浮标 -------------------

    # ----------------- 生活服务 -------------------
    @allure.step("点击全部")
    def click_all(self):
        self.find_element_and_click(**self.element["all_service"])

    # ----------------- Banner -------------------

    # ----------------- 精选专区 -------------------

    # ----------------- 精选专区 -------------------

    # ----------------- 热销理财 -------------------

    # ----------------- 精彩活动 -------------------

    # ----------------- 咨询推荐 -------------------

    # ----------------- 其他 -------------------
    @allure.step("点击开启更多服务")
    def click_open_more_services(self):
        self.find_element_and_click(**self.element["open_more_services"])

    # ----------------- 检查 -------------------
    @allure.step("检查位于卡包页")
    def check_on_card_package_page(self):
        self.assert_element_exist(**self.element["card_package_page"])
