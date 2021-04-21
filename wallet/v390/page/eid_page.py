#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class EIDPage(BasePage):

    def __init__(self, driver):
        super(EIDPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 欢迎页 -------------------
    @allure.step("点击开通eID")
    def click_activate_now(self):
        self.find_element_and_click(**self.element["activate_now"])

    @allure.step("点击常见问题")
    def click_common_problem(self):
        self.find_element_and_click(**self.element["common_problem"])

    # ----------------- 添加eID -------------------
    @allure.step("将身份证贴近手机背面感应区")
    def IDCard_recognition(self):
        self.wait_until_element_gone(**self.element["IDCard_recognition"])
        if self.check_text_existance("重试"):
            self.click_retry()
            self.IDCard_recognition()

    @allure.step("将人脸对准取景框保持不动")
    def face_recognition(self):
        self.wait_until_element_gone(**self.element["face_recognition"])
        if self.check_text_existance("重试"):
            self.click_retry()
            self.face_recognition()

    @allure.step("点击重试")
    def click_retry(self):
        self.find_element_and_click(**self.element["retry"])

    @allure.step("校验身份信息...")
    def wait_verify_identity_information(self):
        self.wait_until_element_gone(**self.element["verify_identity_information"])

    @allure.step("正在生成eID...")
    def wait_write_in_eID_card_process(self):
        self.wait_until_element_gone(**self.element["write_in_eID_card_process"])

    @allure.step("点击完成")
    def click_finish(self):
        self.find_element_and_click(**self.element["finish"])

    # ----------------- 查看eID -------------------
    @allure.step("点击眼睛")
    def click_eye_switch(self):
        self.find_element_and_click(**self.element["eye_switch"])

    @allure.step("点击eID电子证照")
    def click_eID_license(self):
        self.find_element_and_click(**self.element["eID_license"])
