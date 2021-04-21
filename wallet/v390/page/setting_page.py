#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class SettingPage(BasePage):

    def __init__(self, driver):
        super(SettingPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 实名认证 -------------------
    @allure.step("点击实名认证")
    def click_real_name_verification(self):
        self.find_element_and_click(**self.element["real_name_verification"])
        self.sleep(2)
        print("这是姓名")
        self.find_element_and_click(**self.element["username"])
        self.sleep(2)
        print("这是身份证")
        self.find_element_and_click(**self.element["identification_number"])



    # @allure.step("输入姓名")
    # def input_username(self, identification_number):
    #     self.find_element_and_input(identification_number, **self.element["identification_number"])

    @allure.step("输入身份证")
    def input_identification_number(self, identification_number):
        self.find_element_and_input(identification_number, **self.element["username"])

    @allure.step("点击下一步")
    def click_next_step(self):
        self.find_element_and_click(check_toast=False, **self.element["next_step"])

    @allure.step("长按验证码输入栏")
    def long_click_verification_code_box(self):
        self.find_element_and_long_click(**self.element["verification_code_box"])

    @allure.step("点击完成")
    def click_finish(self):
        self.find_element_and_click(**self.element["finish"])

    # ----------------- 双击电源键打开刷卡 -------------------
    @allure.step("点击双击电源键打开刷卡开关")
    def click_double_tap_power_switch(self):
        self.find_element_and_click(**self.element["double_tap_power_switch"])

    # ----------------- 自动切卡 -------------------
    @allure.step("点击自动切卡")
    def click_auto_switch(self):
        self.find_element_and_click(**self.element["auto_switch"])

    @allure.step("点击自动切卡开关")
    def click_auto_switch_switch(self):
        self.find_element_and_click(check_toast=False, **self.element["auto_switch_switch"])

    @allure.step("点击智能切卡")
    def click_smart_switch(self):
        self.find_element_and_click(check_toast=False, **self.element["smart_switch"])

    @allure.step("点击循环切卡")
    def click_loop_switch(self):
        self.find_element_and_click(check_toast=False, **self.element["loop_switch"])

    @allure.step("点击公交卡")
    def click_bus_card(self):
        self.find_element_and_click(**self.element["bus_card"])

    @allure.step("点击门禁卡")
    def click_door_card(self):
        self.find_element_and_click(**self.element["door_card"])

    @allure.step("点击第{0}张卡")
    def click_specified_card(self, index=0):
        self.find_element(**self.element["specified_card"])[index].click()

    @allure.step("点击完成")
    def click_done(self):
        self.find_element_and_click(**self.element["done"])

    @allure.step("点击不选择")
    def click_dont_choose(self):
        self.find_element_and_click(**self.element["dont_choose"])

    # ----------------- 一键修复 -------------------
    @allure.step("点击一键修复")
    def click_one_click_repair(self):
        self.find_element_and_click(**self.element["one_click_repair"])

    @allure.step("点击开始修复")
    def click_start_repair(self):
        self.find_element_and_click(**self.element["start_repair"])

    @allure.step("点击帮助与反馈")
    def click_help_feedback(self):
        self.find_element_and_click(**self.element["help_feedback"])

    @allure.step("加载中")
    def wait_loading(self):
        self.wait_until_element_gone(**self.element["loading"])

    @allure.step("点击完成")
    def click_complete(self):
        self.find_element_and_click(**self.element["complete"])

    # ----------------- 指纹支付 -------------------
    @allure.step("点击指纹支付开关")
    def click_finger_pay_switch(self):
        self.find_element_and_click(**self.element["finger_pay_switch"])

    # ----------------- 支付密码设置 -------------------
    @allure.step("点击支付密码设置")
    def click_password_setting(self):
        self.find_element_and_click(**self.element["password_setting"])

    @allure.step("点击更改支付密码")
    def click_change_password(self):
        self.find_element_and_click(**self.element["change_password"])

    @allure.step("点击忘记支付密码")
    def click_forget_password(self):
        self.find_element_and_click(**self.element["forget_password"])

    @allure.step("点击重置密保")
    def click_reset_security(self):
        self.find_element_and_click(**self.element["reset_security"])

    @allure.step("点击通过身份信息找回")
    def click_retrieve_through_id_info(self):
        self.find_element_and_click(**self.element["retrieve_through_id_info"])

    @allure.step("点击通过密保与手机号找回")
    def click_retrieve_through_security(self):
        self.find_element_and_click(**self.element["retrieve_through_security"])

    @allure.step("输入银行卡号")
    def input_bank_card_number(self, bank_card_number):
        self.find_element_and_input(bank_card_number, **self.element["bank_card_number"])

    @allure.step("输入开户姓名")
    def input_username2(self, username):
        self.find_element_and_input(username, **self.element["username2"])

    @allure.step("输入身份证号码")
    def input_identification_number2(self, identification_number):
        self.find_element_and_input(identification_number, **self.element["identification_number2"])

    @allure.step("输入手机号码")
    def input_mobile_number(self, mobile_number):
        self.find_element_and_input(mobile_number, **self.element["mobile_number"])

    @allure.step("点击下一步")
    def click_next(self):
        self.find_element_and_click(**self.element["next"])

    @allure.step("点击密保问题")
    def click_security_question(self, security_question=None):
        self.find_element_and_click(check_toast=False, **self.element["security_question"])
        element = self.element["sepcific_question"]
        if security_question is not None:
            element["textContains"] = security_question
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("输入密保答案")
    def input_security_answer(self, security_answer):
        self.find_element_and_input(security_answer, **self.element["security_answer"])

    # ----------------- 服务管理 -------------------
    @allure.step("点击服务管理")
    def click_service_management(self):
        self.find_element_and_click(**self.element["service_management"])

    @allure.step("点击功能项")
    def click_function_item(self):
        self.find_element_and_click(**self.element["function_item"])

    @allure.step("点击个性化推荐设置")
    def click_personalized_recommendation(self):
        self.find_element_and_click(**self.element["personalized_recommendation"])

    @allure.step("点击系统权限")
    def click_system_authority(self):
        self.find_element_and_click(**self.element["system_authority"])

    @allure.step("点击服务协议")
    def click_service_agreement(self):
        self.find_element_and_click(**self.element["service_agreement"])

    @allure.step("点击隐私声明")
    def click_privacy_statement(self):
        self.find_element_and_click(**self.element["privacy_statement"])

    @allure.step("点击个性化推荐开关")
    def click_personalized_recommendation_switch(self):
        self.find_element_and_click(**self.element["personalized_recommendation_switch"])

    @allure.step("点击{0}开关")
    def click_specific_function_item_switch(self, function_name):
        element = self.element["specific_function_item_switch"]
        element["right"][0]["textContains"] = function_name
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("点击全部开启")
    def click_open_all(self):
        self.find_element_and_click(check_toast=False, **self.element["open_all"])

    # ----------------- 注销钱包支付账户 -------------------
    @allure.step("点击注销钱包支付账户")
    def click_cancel_account(self):
        self.find_element_and_click(**self.element["cancel_account"])

    @allure.step("点击解绑")
    def click_unbind(self):
        self.find_element_and_click(**self.element["unbind"])

    @allure.step("点击查看")
    def click_examine(self):
        self.find_element_and_click(**self.element["examine"])

    @allure.step("点击确认注销")
    def click_confirm_logout(self):
        self.find_element_and_click(**self.element["confirm_logout"])

    # ----------------- 版本号 -------------------
    @allure.step("点击版本号")
    def click_version(self):
        self.find_element_and_click(**self.element["version"])

    # ----------------- 检查 -------------------
    def check_on_certification_information_page(self):
        return self.check_element_existence(**self.element["cancel_account"])
