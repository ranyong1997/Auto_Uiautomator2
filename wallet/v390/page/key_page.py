#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class KeyPage(BasePage):

    def __init__(self, driver):
        super(KeyPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 添加门禁卡 -------------------
    @allure.step("点击录入实体门禁卡")
    def click_physical_access_card(self):
        self.find_element_and_click(**self.element["physical_access_card"])

    @allure.step("点击线上开通门禁卡")
    def click_online_access_card(self):
        self.find_element_and_click(**self.element["online_access_card"])

    @allure.step("点击人工录入")
    def click_manual_access_card(self):
        self.find_element_and_click(**self.element["manual_access_card"])

    @allure.step("点击添加门禁卡/生成空白卡")
    def click_add_access_card(self):
        if self.check_text_existance("迁入"):
            # 有待迁入的卡片时，开通新卡
            self.find_element_and_click(**self.element["activate_new_card"])
            self.find_element_and_click(**self.element["add_access_card"])
        else:
            self.find_element_and_click(**self.element["add_access_card"])

    @allure.step("检测门禁卡")
    def sense_access_card(self):
        self.wait_until_element_gone(**self.element["sense_access_card"])
        if self.check_text_existance("重试"):
            self.click_retry()
            self.sense_access_card()

    @allure.step("点击重试")
    def click_retry(self):
        self.find_element_and_click(**self.element["retry"])

    @allure.step("正在录入门禁卡...")
    def wait_import_access_card_process(self):
        self.wait_until_element_gone(**self.element["import_process_title"])

    @allure.step("正在生成空白卡...")
    def wait_create_white_card_process(self):
        self.wait_until_element_gone(**self.element["create_white_card_process"])

    @allure.step("点击立即录入")
    def click_write_in_now(self):
        self.find_element_and_click(**self.element["write_in_now"])

    @allure.step("点击稍后录入")
    def click_write_in_later(self):
        self.find_element_and_click(**self.element["write_in_later"])

    @allure.step("点击无法识别设备?")
    def click_unrecognized_device(self):
        self.find_element_and_click(**self.element["unrecognized_device"])

    @allure.step("点击保存")
    def click_save(self):
        self.find_element_and_click(ignore_toast="设置成功", **self.element["save"])

    # ----------------- 编辑门禁卡 -------------------
    @allure.step("点击卡片名称")
    def click_card_name(self):
        self.find_element_and_click(**self.element["card_name"])

    @allure.step("输入卡片名称")
    def input_card_name(self, card_name):
        self.find_element_and_input(card_name, **self.element["card_name_editbox"])

    @allure.step("点击不显示名称开关")
    def click_display_switch(self):
        self.find_element_and_click(**self.element["display_switch"])

    @allure.step("点击封面")
    def click_card_cover_style(self):
        self.find_element_and_click(**self.element["card_cover_style"])

    @allure.step("随机点击一张封面")
    def click_random_cover(self):
        self.find_element_and_click(**self.element["random_cover"])

    @allure.step("点击自定义卡面")
    def click_custom_cover(self):
        self.find_element_and_click(**self.element["custom_cover"])

    @allure.step("点击第一张图")
    def click_first_picture(self):
        self.find_element_and_click(**self.element["first_picture"])

    @allure.step("点击保存(编辑照片)")
    def click_save_picture(self):
        self.find_element_and_click(**self.element["save_picture"])

    @allure.step("点击保存(封面)")
    def click_save_cover(self):
        self.find_element_and_click(ignore_toast="设置成功", **self.element["save_cover"])

    # ----------------- 删除门禁卡 -------------------
    @allure.step("遍历点击删卡原因")
    def click_delete_reason_checkbox(self):
        for element in self.find_element(**self.element["delete_reason_checkbox"]):
            element.click()

    @allure.step("输入具体原因")
    def input_delete_card_reason(self, delete_reason):
        self.find_element_and_input(delete_reason, **self.element["delete_card_reason"])

    @allure.step("点击确认删除")
    def click_confirm_delete(self):
        self.find_element_and_click(**self.element["confirm_delete"])

    @allure.step("正在删除")
    def wait_delete_process(self):
        self.wait_until_element_gone(**self.element["delete_process"])

    # ----------------- 使用技巧 -------------------
    @allure.step("点击使用技巧")
    def click_card_tips(self):
        self.find_element_and_click(**self.element["card_tips"])

    @allure.step("点击完成(使用技巧)")
    def click_finish_on_tips_page(self):
        self.find_element_and_click(**self.element["finish_on_tips_page"])

    # ----------------- 迁移门禁卡 -------------------
    @allure.step("点击门禁卡1")
    def click_access_card_1(self):
        self.find_element_and_click(**self.element["access_card_1"])

    @allure.step("点击迁移至本机")
    def click_move_in_to_this_machine(self):
        self.find_element_and_click(**self.element["move_in_to_this_machine"])

    @allure.step("正在迁入卡片")
    def wait_moving_in_card(self):
        self.wait_until_element_gone(**self.element["moving_in_card"])

    @allure.step("点击完成")
    def click_carry_out(self):
        self.find_element_and_click(**self.element["carry_out"])