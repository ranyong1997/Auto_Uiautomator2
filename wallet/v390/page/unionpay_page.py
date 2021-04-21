#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class UnionPayPage(BasePage):

    def __init__(self, driver):
        super(UnionPayPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 欢迎页 -------------------
    @allure.step("点击立即开通")
    def click_acticate_now(self):
        self.find_element_and_click(**self.element["acticate_now"])

    # ----------------- 添加银行卡 -------------------
    @allure.step("输入银行卡号")
    def input_bank_card_number(self, bank_card_number):
        self.find_element_and_input(bank_card_number, **self.element["bank_card_number"])

    @allure.step("点击下一步")
    def click_next_button(self):
        self.find_element_and_click(ignore_toast="移除成功", **self.element["next_button"])

    @allure.step("输入手机号码")
    def input_mobile_number(self, mobile_number):
        self.find_element_and_input(mobile_number, **self.element["mobile_number"])

    @allure.step("输入取款密码")
    def input_bank_password(self, bank_password):
        self.find_element_and_click(**self.element["bank_password"])
        for num in list(bank_password):
            self.find_element_and_click(check_toast=False, text=num)

    @allure.step("输入有效期")
    def input_expire_date(self, expire_date):
        self.find_element_and_input(expire_date, **self.element["expire_date"])

    @allure.step("输入CVN2")
    def input_cvn2(self, cvn2):
        self.find_element_and_click(**self.element["cvn2"])
        for num in list(cvn2):
            self.find_element_and_click(check_toast=False, text=num)

    @allure.step("点击同意协议并绑卡")
    def click_bind_card_button(self):
        self.find_element_and_click(**self.element["next_button"])

    @allure.step("正在添加银行卡...")
    def wait_add_bank_card_process(self):
        self.wait_until_element_gone(**self.element["add_bank_card_process"])

    @allure.step("点击验证码输入栏")
    def long_click_verification_code_box(self):
        self.find_element_and_long_click(**self.element["verification_code_box"])

    @allure.step("点击选择密保问题")
    def click_security_question(self):
        self.find_element_and_click(**self.element["security_question"])

    @allure.step("点击具体的密保问题")
    def click_specific_security_question(self, security_question):
        element = self.element["specific_security_question"]
        element["textContains"] = security_question
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("输入密保答案")
    def input_security_answer(self, security_answer):
        self.find_element_and_input(security_answer, **self.element["security_answer"])

    @allure.step("点击下一步(设置密保页)")
    def click_next_button2(self):
        self.find_element_and_click(**self.element["next_button"])

    @allure.step("点击下次再说")
    def click_next_time(self):
        self.find_element_and_click(**self.element["next_time"])

    # ----------------- 银行卡详情 -------------------
    @allure.step("点击交易记录")
    def click_transaction_record(self):
        self.find_element_and_click(**self.element["transaction_record"])

    @allure.step("点击银行客服热线")
    def click_service_hotline(self):
        self.find_element_and_click(**self.element["service_hotline"])

    # ----------------- 付款码 -------------------
    @allure.step("点击条形码")
    def click_barcode(self):
        self.find_element_and_click(**self.element["barcode"])

    @allure.step("点击放大的条形码")
    def click_big_barcode(self):
        self.find_element_and_click(**self.element["big_barcode"])

    @allure.step("点击二维码")
    def click_qrcode(self):
        self.find_element_and_click(**self.element["qrcode"])

    @allure.step("点击放大的二维码")
    def click_big_qrcode(self):
        self.find_element_and_click(**self.element["big_qrcode"])

    @allure.step("点击卡片切换")
    def click_change_card(self):
        self.scroll_to_boundary()
        self.find_element_and_click(**self.element["change_card"])

    @allure.step("点击立即开启")
    def click_turn_on(self):
        self.find_element_and_click(**self.element["turn_on"])

    # ----------------- 扫一扫 -------------------
    @allure.step("点击手电筒")
    def click_flashlight(self):
        self.find_element_and_click(**self.element["flashlight"])

    @allure.step("点击相册")
    def click_photo_album(self):
        self.find_element_and_click(**self.element["photo_album"])

    @allure.step("点击二维码图片")
    def click_qrcode_photo(self):
        self.driver.sleep(2.0)
        self.driver.click(0.20, 0.18)
        self.driver.sleep(2.0)
        self.driver.click(0.12, 0.18)

    @allure.step("输入付款金额并确定")
    def input_payment_amount(self, payment_amount):
        for num in list(payment_amount):
            self.find_element_and_click(check_toast=False, text=num)
        self.find_element_and_click(check_toast=False, text="确定")

    @allure.step("点击确认付款")
    def click_confirm_payment(self):
        self.find_element_and_click(**self.element["confirm_payment"])

    @allure.step("点击完成")
    def click_done(self):
        self.find_element_and_click(ignore_toast="支付成功", **self.element["done"])

    # ----------------- 删除银行卡 -------------------
    @allure.step("正在删除...")
    def wait_delete_bank_card_process(self):
        self.wait_until_element_gone(**self.element["delete_bank_card_process"])
        assert self.get_toast() == "移除成功", "删除银行卡toast提示异常"

    # ----------------- 检查 -------------------
    @allure.step("检查设备卡号非空")
    def check_device_card_number(self):
        assert self.find_element(**self.element["device_card_number"]).get_text() is not None, "设备卡号为空"

    @allure.step("检查付款码开启状态")
    def check_payment_code_state(self):
        self.assert_element_exist(**self.element["qrcode"])
