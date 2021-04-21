#!/usr/bin/env python
# -*- coding:utf-8 -*-


import os

import allure

from common.base_page import BasePage
from common.utils import get_installed_package_name
from wallet.v390 import root_dir
from wallet.v390.element import ElementRouter


class CommonPage(BasePage):

    def __init__(self, driver):
        super(CommonPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 启停应用 -------------------
    @allure.step("启动信息")
    def start_mms(self):
        self.driver.app_start("com.android.mms")

    @allure.step("启动钱包")
    def start_wallet(self):
        package_name = get_installed_package_name()
        self.driver.app_start(package_name)

    # ----------------- 页面标题栏 -------------------
    @allure.step("点击标题栏返回箭头")
    def click_back_arrow(self):
        self.find_element_and_click(check_toast=False, **self.element["back_arrow"])
        self.sleep(0.5)

    @allure.step("点击标题栏更多选项")
    def click_more_options(self):
        self.find_element_and_click(check_toast=False, **self.element["more_options"])

    @allure.step("点击弹框列表:{0}")
    def click_popup_list_item(self, item_name=None):
        element = self.element["popup_list_item"]
        if item_name is not None:
            element["textContains"] = item_name
        self.find_element_and_click(check_toast=False, **element)

    # ----------------- 双击唤醒 -------------------
    @allure.step("双击电源键")
    def double_click_power_key(self):
        self.press_key("power")
        self.press_key("power")

    # ----------------- 刷卡页 -------------------
    @allure.step("点击详情(卡面)")
    def click_card_detail(self):
        self.find_element_and_click(**self.element["card_detail"])

    @allure.step("点击退出(顶部左侧)")
    def click_exit(self):
        self.find_element_and_click(**self.element["exit"])

    @allure.step("点击切换卡片(底部卡面)")
    def click_change_card(self):
        self.find_element_and_click(check_toast=False, index=1, **self.element["change_card"])

    @allure.step("点击切换卡片(底部半弹窗)")
    def click_change_card2(self):
        self.find_element_and_click(check_toast=False, **self.element["change_card2"])

    @allure.step("点击x(底部半弹窗)")
    def click_close(self):
        self.find_element_and_click(check_toast=False, **self.element["close"])

    @allure.step("点击添加卡(顶部+)")
    def click_add_card(self):
        self.find_element_and_click(**self.element["add_card"])

    @allure.step("点击更多(顶部)")
    def click_more(self):
        self.find_element_and_click(check_toast=False, **self.element["more"])

    @allure.step("点击取消(顶部左侧)")
    def click_cancel(self):
        self.find_element_and_click(**self.element["cancel"])

    @allure.step("点击充值")
    def click_recharge(self):
        self.find_element_and_click(**self.element["recharge"])

    @allure.step("点击展开二维码")
    def click_unfold_qrcode(self):
        self.find_element_and_click(**self.element["unfold_qrcode"])

    @allure.step("点击点击收起")
    def click_pack_up(self):
        self.find_element_and_click(**self.element["pack_up"])

    # ----------------- 密码键盘 -------------------
    @allure.step("输入支付密码(白底黑字)")
    def input_wallet_password(self, wallet_password):
        for num in list(wallet_password):
            image_dir = os.path.join(root_dir, "image", "keyboard", num + ".jpg")
            self.find_element_and_click(check_toast=False, image=image_dir)

    @allure.step("输入支付密码(黑底白字)")
    def input_wallet_password2(self, wallet_password):
        for num in list(wallet_password):
            image_dir = os.path.join(root_dir, "image", "keyboard_black", num + ".png")
            self.find_element_and_click(check_toast=False, image=image_dir)

    @allure.step("输入支付密码(H5)")
    def input_wallet_password_h5(self, wallet_password):
        for num in list(wallet_password):
            self.find_element_and_click(check_toast=False, text=num)

    # ----------------- 弹窗(系统) -------------------
    @allure.step("点击{0}")
    def click_button1(self, buttom_name=None):
        element = self.element["button1"]
        if buttom_name is not None:
            element["textContains"] = buttom_name
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("点击{0}")
    def click_button2(self, buttom_name=None):
        element = self.element["button2"]
        if buttom_name is not None:
            element["textContains"] = buttom_name
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("点击{0}")
    def click_button3(self, buttom_name=None):
        element = self.element["button3"]
        if buttom_name is not None:
            element["textContains"] = buttom_name
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("正在加载...")
    def wait_loading(self):
        self.wait_until_element_gone(**self.element["loading"])

    # ----------------- 信息 -------------------
    @allure.step("点击通知")
    def click_notices(self):
        self.find_element_and_click(**self.element["notices"])

    @allure.step("点击HeyTap")
    def click_heytap(self):
        self.find_element_and_click(**self.element["heytap"])

    @allure.step("点击复制验证码")
    def click_mms_copy_verification_code(self):
        self.find_element_and_click(check_toast=False, **self.element["mms_copy_verification_code"])

    # ----------------- 通知栏(系统) -------------------
    @allure.step("点击复制验证码")
    def click_sys_copy_verification_code(self):
        self.find_element_and_click(check_toast=False, **self.element["sys_copy_verification_code"])

    # ----------------- 粘贴(系统) -------------------
    @allure.step("点击粘贴")
    def click_paste(self):
        self.find_element_and_click(check_toast=False, **self.element["paste"])
