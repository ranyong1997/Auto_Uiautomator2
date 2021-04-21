#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.messagebox import box
from wallet.v390.page import EIDPage, HomePage, CommonPage, UnionPayPage


class EIDFlow(object):

    def __init__(self, driver):
        self.eid_page = EIDPage(driver)
        self.home_page = HomePage(driver)
        self.common_page = CommonPage(driver)
        self.unionpay_page = UnionPayPage(driver)

    @allure.story("添加eID操作")
    def open_eid_card(self, scene, **kwargs):
        self.home_page.click_card_package()
        self.home_page.click_add()
        self.home_page.click_add_eID()
        self.eid_page.click_common_problem()
        self.eid_page.scroll_to_boundary("end")
        self.common_page.click_back_arrow()
        self.eid_page.click_activate_now()
        # self.common_page.click_button1("同意")  # 弹出检测会自动点掉
        self.eid_page.sleep(1.0)
        if scene == 1:
            # 未设置密码密保
            self.common_page.input_wallet_password2(kwargs["wallet_password"])
            self.common_page.input_wallet_password2(kwargs["wallet_password"])
            self.unionpay_page.click_security_question()
            self.unionpay_page.click_specific_security_question(kwargs["security_question"])
            self.unionpay_page.input_security_answer(kwargs["security_answer"])
            self.unionpay_page.click_next_button()
        elif scene == 2:
            # 已设置密码密保
            self.common_page.input_wallet_password(kwargs["wallet_password"])
        box('嗨！\n请用身份证靠近测试机NFC区域\n点击准备好了再贴卡哈')
        self.eid_page.IDCard_recognition()
        box('嗨！\n请进行人脸识别\n点击准备好了再让脸进入识别框里哈')
        self.eid_page.face_recognition()
        self.eid_page.wait_verify_identity_information()
        self.eid_page.wait_write_in_eID_card_process()
        if self.eid_page.check_text_existance("开卡成功"):
            self.eid_page.click_finish()
            self.eid_page.assert_text_exist("卡包")
        else:
            self.eid_page.assert_text_exist("姓名：")
            self.eid_page.assert_text_exist("公民身份号码：")

    @allure.story("遍历我的eID页面操作")
    def traverse_my_eid_card(self, **kwargs):
        self.home_page.click_card_package()
        self.home_page.click_eID()
        self.eid_page.click_eye_switch()
        self.common_page.input_wallet_password(kwargs["wallet_password"])
        self.eid_page.assert_text_exist("姓名：")
        self.eid_page.assert_text_exist("公民身份号码：")
        self.eid_page.click_eID_license()
        self.common_page.input_wallet_password(kwargs["wallet_password"])
        self.eid_page.assert_text_exist("点击收起")
        self.unionpay_page.click_qrcode()
        self.unionpay_page.click_big_qrcode()
        self.common_page.click_pack_up()
        self.common_page.click_unfold_qrcode()
        self.common_page.click_card_detail()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("常见问题")
        self.eid_page.scroll_to_boundary("end")
        self.eid_page.scroll_to_boundary("beginning")
        self.common_page.click_back_arrow()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("用户协议")
        self.eid_page.scroll_to_boundary("end")
        self.eid_page.scroll_to_boundary("beginning")
        self.common_page.click_back_arrow()
        assert self.eid_page.check_text_existance("姓名：") is False, "用户二要素敏感信息未遮挡"
        self.common_page.click_back_arrow()
        self.eid_page.assert_text_exist("卡包")

    @allure.story("删除eID操作")
    def delete_eid_card(self):
        self.home_page.click_card_package()
        self.home_page.click_eID()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("注销")
        self.common_page.click_button1("注销")
        self.common_page.wait_loading()
        self.eid_page.assert_text_exist("开通 eID")
