#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from wallet.v390.flow.common_flow import CommonFlow
from wallet.v390.page import CommonPage, HomePage, UnionPayPage


class UnionPayFlow(object):

    def __init__(self, driver):
        self.home_page = HomePage(driver)
        self.unionpay_page = UnionPayPage(driver)
        self.common_page = CommonPage(driver)
        self.common_flow = CommonFlow(driver)

    @allure.story("进入添加银行卡页操作")
    def goto_add_card_page(self, scene):
        if scene == 1:
            # 付款码---立即开通
            self.home_page.click_payment_code()
            self.unionpay_page.click_acticate_now()
        elif scene == 2:
            # OPPO Pay---添加卡
            self.home_page.click_oppo_pay()
            self.common_page.click_add_card()
        elif scene == 3:
            # 卡包---添加卡(+)---添加银行卡
            self.home_page.click_card_package()
            self.home_page.click_add()
            self.home_page.click_add_bank_card()

    @allure.story("借记卡要素填写操作")
    def fill_in_debit_card_info(self, support_nfc, **kwargs):
        """ 填写借记卡信息并进行绑卡 """
        self.unionpay_page.input_bank_card_number(kwargs["bank_card_number"])
        self.unionpay_page.click_next_button()
        if support_nfc is True:
            self.unionpay_page.input_mobile_number(kwargs["mobile_number"])
            self.unionpay_page.input_bank_password(kwargs["bank_password"])
        else:
            # todo 非NFC绑卡流程，姓名、身份证、手机号、验证码
            pass
        self.unionpay_page.click_bind_card_button()
        self.unionpay_page.wait_add_bank_card_process()

    @allure.story("信用卡要素填写操作")
    def fill_in_credit_card_info(self, support_nfc, **kwargs):
        """ 填写信用卡信息并进行绑卡 """
        self.unionpay_page.input_bank_card_number(kwargs["bank_card_number"])
        self.unionpay_page.click_next_button()
        self.unionpay_page.input_mobile_number(kwargs["mobile_number"])
        self.unionpay_page.input_expire_date(kwargs["expire_date"])
        self.unionpay_page.input_cvn2(kwargs["cvn2"])
        if support_nfc is False:
            # todo 非NFC绑卡流程，验证码
            pass
        self.unionpay_page.click_bind_card_button()
        self.unionpay_page.wait_add_bank_card_process()

    @allure.story("安全信息填写操作")
    def fill_in_safety_info(self, scene, support_nfc, **kwargs):
        """ 输入验证码、密码、密保并完成 """
        if support_nfc is True:
            self.common_flow.copy_verification_code_from_notification()
            self.unionpay_page.long_click_verification_code_box()
            self.common_page.click_paste()
            self.unionpay_page.click_next_button()
        if scene == 1:
            # 账户未设置密码时
            self.common_page.input_wallet_password(kwargs["wallet_password"])
            self.common_page.input_wallet_password(kwargs["wallet_password"])
            self.unionpay_page.click_security_question()
            self.unionpay_page.click_specific_security_question(kwargs["security_question"])
            self.unionpay_page.input_security_answer(kwargs["security_answer"])
            self.unionpay_page.click_next_button()
        self.unionpay_page.click_next_time()

    @allure.story("遍历卡详情页")
    def traverse_card_detail(self, support_nfc):
        if support_nfc is True:
            self.home_page.click_oppo_pay()
            self.common_page.click_close()
            self.common_page.click_card_detail()
        else:
            # todo 非NFC的进入到卡详情操作
            pass
        self.unionpay_page.click_transaction_record()
        self.common_page.click_back_arrow()
        self.unionpay_page.check_device_card_number()
        self.unionpay_page.click_service_hotline()
        self.unionpay_page.press_key("back")
        self.common_page.click_back_arrow()

    @allure.story("关闭和开启付款码")
    def turn_off_and_on_payment_code(self, **kwargs):
        self.home_page.click_payment_code()
        self.unionpay_page.click_barcode()
        self.unionpay_page.click_big_barcode()
        self.unionpay_page.click_qrcode()
        self.unionpay_page.click_big_qrcode()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("暂停使用")
        self.common_page.click_button1("暂停使用")
        self.unionpay_page.click_turn_on()
        self.common_page.input_wallet_password(kwargs["wallet_password"])
        self.unionpay_page.check_payment_code_state()

    @allure.story("扫一扫支付流程")
    def scan_payment(self, **kwargs):
        self.home_page.click_scan_it()
        self.unionpay_page.click_flashlight()
        self.unionpay_page.click_flashlight()
        self.unionpay_page.click_photo_album()
        self.unionpay_page.click_qrcode_photo()
        self.unionpay_page.input_payment_amount(kwargs["payment_amount"])
        self.oppo_pay_online_payment(**kwargs)

    @allure.story("OPPO Pay线上支付流程")
    def oppo_pay_online_payment(self, **kwargs):
        self.unionpay_page.click_confirm_payment()
        self.common_page.input_wallet_password(kwargs["wallet_password"])
        self.unionpay_page.click_done()

    @allure.story("删除银行卡流程")
    def delete_bank_card(self):
        self.home_page.click_card_package()
        self.home_page.click_first_bank_card()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("删除银行卡")
        self.common_page.click_button3("删除银行卡")
        self.unionpay_page.wait_delete_bank_card_process()
        self.home_page.check_on_card_package_page()
