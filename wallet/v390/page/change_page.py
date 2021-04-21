'''
Descripttion: 
version: 
Author: 冉勇
Date: 2021-04-01 18:51:28
LastEditTime: 2021-04-01 18:56:30
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class ChangePage(BasePage):

    def __init__(self, driver):
        super(ChangePage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 欢迎页 -------------------
    @allure.step("点击立即开通")
    def click_acticate_now(self):
        self.find_element_and_click(check_toast=False, **self.element["acticate_now"])

    # ----------------- 添加银行卡(Native) -------------------
    @allure.step("点击拍照识别卡号")
    def click_take_photo(self):
        self.find_element_and_click(**self.element["take_photo"])

    @allure.step("点击支持的银行")
    def click_supported_bank(self):
        self.find_element_and_click(**self.element["supported_bank"])

    @allure.step("输入银行卡号")
    def input_bank_card_number(self, bank_card_number):
        self.find_element_and_input(bank_card_number, **self.element["bank_card_number"])

    @allure.step("点击下一步")
    def click_next_step(self):
        self.find_element_and_click(**self.element["next_step"])

    @allure.step("输入手机号码")
    def input_mobile_number(self, mobile_number):
        self.find_element_and_input(mobile_number, **self.element["mobile_number"])

    @allure.step("点击职业")
    def click_profession(self):
        self.find_element_and_click(**self.element["profession"])

    @allure.step("选择职业大类")
    def click_profession_group(self, profession_group):
        element = self.element["profession_group"]
        element["textContains"] = profession_group
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("选择职业小类")
    def click_profession_item(self, profession_item):
        element = self.element["profession_item"]
        element["textContains"] = profession_item
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("点击同意协议")
    def click_protocol_check_box(self):
        self.find_element_and_click(check_toast=False, **self.element["protocol_check_box"])

    @allure.step("点击开始验证")
    def click_start_verification(self):
        self.find_element_and_click(**self.element["start_verification"])

    @allure.step("人脸识别")
    def face_recognition(self):
        self.wait_until_element_gone(**self.element["face_recognition"])

    @allure.step("长按验证码框")
    def long_click_verification_code_box(self):
        self.find_element_and_long_click(**self.element["verification_code_box"])

    @allure.step("输入验证码")  # 测试环境
    def input_verify_code(self, verify_code):
        self.find_element_and_input(verify_code, **self.element["verification_code_box"])

    # ----------------- 零钱首页 -------------------
    @allure.step("点击充值")
    def click_recharge(self):
        self.find_element_and_click(**self.element["recharge"])

    @allure.step("点击提现")
    def click_withdraw(self):
        self.find_element_and_click(**self.element["withdraw"])

    @allure.step("点击零钱明细")
    def click_change_details(self):
        self.find_element_and_click(**self.element["change_details"])

    @allure.step("点击零钱绑定卡")
    def click_change_card_package(self):
        self.find_element_and_click(**self.element["change_card_package"])

    @allure.step("点击提升限额")
    def click_increase_limit(self):
        self.find_element_and_click(**self.element["increase_limit"])

    # ----------------- 关于零钱 -------------------
    @allure.step("点击绑定手机号")
    def click_bound_phone_number(self):
        self.find_element_and_click(**self.element["bound_phone_number"])

    @allure.step("点击更换手机号")
    def click_change_phone_number(self):
        self.find_element_and_click(**self.element["change_phone_number"])

    # ----------------- 零钱明细 -------------------
    @allure.step("点击提现")
    def click_withdraw_h5(self):
        self.find_element_and_click(**self.element["withdraw_h5"])

    @allure.step("点击充值")
    def click_recharge_h5(self):
        self.find_element_and_click(**self.element["recharge_h5"])

    # ----------------- 零钱绑定卡 -------------------
    @allure.step("点击+")
    def click_add_card(self):
        self.find_element_and_click(**self.element["add_card"])

    @allure.step("点击首张银行卡")
    def click_first_bank_card(self):
        self.find_element_and_click(**self.element["first_bank_card"])

    def bank_card_number(self):
        return len(self.find_element(**self.element["first_bank_card"]))

    # ----------------- 再次添加银行卡(H5) -------------------
    @allure.step("点击拍照识别卡号")
    def click_take_photo_h5(self):
        self.find_element_and_click(**self.element["take_photo_h5"])

    @allure.step("点击支持的银行")
    def click_supported_bank_h5(self):
        self.find_element_and_click(**self.element["supported_bank_h5"])

    @allure.step("输入银行卡号")
    def input_bank_card_number_h5(self, bank_card_number):
        self.find_element_and_input(bank_card_number, **self.element["bank_card_number_h5"])

    @allure.step("点击下一步")
    def click_next_step_h5(self):
        self.find_element_and_click(**self.element["next_step_h5"])

    @allure.step("输入手机号码")
    def input_mobile_number_h5(self, mobile_number):
        self.find_element_and_input(mobile_number, **self.element["mobile_number_h5"])

    @allure.step("点击广发银行电子账户协议")
    def click_cgb_account_agreement(self):
        self.find_element_and_click(**self.element["cgb_account_agreement"])

    @allure.step("长按验证码框")
    def long_click_verification_code_box_h5(self):
        self.find_element_and_long_click(**self.element["verification_code_box_h5"])

    @allure.step("输入验证码")  # 测试环境
    def input_verify_code_h5(self, verify_code):
        self.find_element_and_input(verify_code, **self.element["verification_code_box_h5"])

    # ----------------- 充值 提现-------------------
    @allure.step("输入金额")
    def input_amount(self, amount):
        self.find_element_and_input(amount, **self.element["amount"])

    @allure.step("点击立即充值/提现")
    def click_recharge_or_withdraw_now(self):
        self.find_element_and_click(**self.element["recharge_or_withdraw_now"])

    @allure.step("点击完成")
    def click_complete(self):
        self.find_element_and_click(**self.element["complete"])

    # ----------------- 提升限额 -------------------
    @allure.step("点击拍摄身份证")
    def click_identify_IDCard(self):
        self.find_element_and_click(**self.element["identify_IDCard"])

    @allure.step("扫描身份证人像面")
    def wait_scan_front_process(self):
        self.wait_until_element_gone(**self.element["scan_front_process"])

    @allure.step("扫描身份证国徽面")
    def wait_scan_back_process(self):
        self.wait_until_element_gone(**self.element["scan_back_process"])

    @allure.step("点击编辑住址")
    def click_edit_address(self):
        self.find_element_and_click(**self.element["edit_address"])

    @allure.step("点击省市区")
    def click_province_city_district(self):
        self.find_element_and_click(check_toast=False, **self.element["province_city_district"])

    @allure.step("点击省")
    def click_province(self, province):
        self.scroll_until_element_appear(textContains=province)
        self.find_element_and_click(check_toast=False, textContains=province)

    @allure.step("点击市")
    def click_city(self, city):
        self.scroll_until_element_appear(textContains=city)
        self.find_element_and_click(check_toast=False, textContains=city)

    @allure.step("点击区")
    def click_district(self, district):
        self.scroll_until_element_appear(textContains=district)
        self.find_element_and_click(check_toast=False, textContains=district)

    @allure.step("输入详细地址")
    def input_address(self, address):
        self.find_element_and_input(address, **self.element["address"])

    @allure.step("点击保存")
    def click_save(self):
        self.find_element_and_click(**self.element["save"])

    @allure.step("正在处理...")
    def wait_loading(self):
        self.wait_until_element_gone(**self.element["loading"])

    @allure.step("点击确认无误")
    def click_confirmed(self):
        self.find_element_and_click(**self.element["confirmed"])

    # ----------------- 注销零钱 -------------------
    @allure.step("点击解绑")
    def click_unbind(self):
        self.find_element_and_click(**self.element["unbind"])

    @allure.step("点击下一步")
    def click_next(self):
        self.find_element_and_click(**self.element["next"])

    @allure.step("正在注销...")
    def wait_cancel_account_process(self):
        self.wait_until_element_gone(**self.element["cancel_account_process"])
