#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.messagebox import box
from wallet.v390.flow.common_flow import CommonFlow
from wallet.v390.flow.setting_flow import SettingFlow
from wallet.v390.page import CommonPage, MinePage, ChangePage, UnionPayPage


class ChangeFlow(object):

    def __init__(self, driver):
        self.mine_page = MinePage(driver)
        self.change_page = ChangePage(driver)
        self.common_page = CommonPage(driver)
        self.unionpay_page = UnionPayPage(driver)
        self.common_flow = CommonFlow(driver)
        self.setting_flow = SettingFlow(driver)

    @allure.story("进入零钱")
    def goto_change_page(self):
        self.mine_page.click_mine_tab()
        self.mine_page.click_my_assets()
        self.mine_page.click_change()

    @allure.story("开通三类户操作")
    def open_change_account(self, scene, support_nfc: bool, **kwargs):
        self.change_page.click_acticate_now()
        if self.change_page.assert_text_exist("实名认证"):
            self.setting_flow.real_name_verification(**kwargs)
            self.common_page.input_wallet_password_h5(kwargs["wallet_password"])
            self.common_page.input_wallet_password_h5(kwargs["wallet_password"])
        self.change_page.click_take_photo()
        self.change_page.press_key("back")
        self.change_page.click_supported_bank()
        self.common_page.click_back_arrow()
        self.change_page.input_bank_card_number(kwargs["bank_card_number"])
        self.change_page.click_next_step()
        self.change_page.input_mobile_number(kwargs["mobile_number"])
        self.change_page.click_profession()
        self.change_page.click_profession_group(kwargs["profession_group"])
        self.change_page.click_profession_item(kwargs["profession_item"])
        self.change_page.click_protocol_check_box()
        self.change_page.click_next_step()
        if scene == 1:
            # 生产环境
            self.change_page.click_start_verification()
            box('嗨！\n请进行人脸识别\n点击准备好了再让脸进入识别框里哈')
            self.change_page.face_recognition()
            self.common_flow.copy_verification_code_from_notification()
            self.change_page.long_click_verification_code_box()
            self.common_page.click_paste()
        elif scene == 2:
            # 测试环境
            self.change_page.input_verify_code(kwargs["verify_code"])
        self.change_page.click_next_step()
        if support_nfc is True:
            self.common_page.wait_loading()
            if self.change_page.check_text_existance("重试"):
                self.common_page.click_back_arrow()
            else:
                self.unionpay_page.wait_add_bank_card_process()
        self.change_page.assert_text_exist("充值")

    @allure.story('充值操作')
    def change_recharge(self, **kwargs):
        self.change_page.click_recharge()
        self.change_page.input_amount(kwargs["amount"])
        self.change_page.click_recharge_or_withdraw_now()
        if self.change_page.check_text_existance("首次充值需要填写验证码"):
            verify_code = "123521"  # todo 通过OCR识别获取验证码后输入到这里
            self.common_page.input_wallet_password(verify_code)
        self.common_page.input_wallet_password2(kwargs["wallet_password"])
        self.common_page.wait_loading()
        self.change_page.assert_text_exist("充值成功")
        self.change_page.click_complete()

    @allure.story('提现操作')
    def change_withdraw(self, **kwargs):
        self.change_page.click_withdraw()
        self.change_page.input_amount(kwargs["amount"])
        self.change_page.click_recharge_or_withdraw_now()
        self.common_page.input_wallet_password2(kwargs["wallet_password"])
        self.common_page.wait_loading()
        self.change_page.assert_text_exist("提现成功")
        self.change_page.click_complete()

    @allure.story('遍历零钱信息页面操作')
    def traverse_change_detail(self):
        self.change_page.click_change_details()
        if self.change_page.check_text_existance("提现"):
            self.change_page.click_withdraw_h5()
            self.change_page.assert_text_exist("提现成功")
            self.common_page.click_back_arrow()
        if self.change_page.check_text_existance("充值"):
            self.change_page.click_recharge_h5()
            self.change_page.assert_text_exist("充值成功")
            self.common_page.click_back_arrow()
        self.common_page.click_back_arrow()
        self.change_page.click_change_card_package()
        self.change_page.click_first_bank_card()
        self.change_page.assert_text_exist("每日消费限额")
        self.common_page.click_back_arrow()
        self.common_page.click_back_arrow()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("关于零钱")
        self.change_page.assert_text_exist("电子账户号")
        self.change_page.click_bound_phone_number()
        self.change_page.click_change_phone_number()
        self.change_page.assert_text_exist("添加银行卡")
        self.common_page.click_back_arrow()
        self.common_page.click_back_arrow()
        self.change_page.assert_text_exist("零钱")

    @allure.story('提升限额操作')
    def increase_limit(self, **kwargs):
        self.change_page.click_increase_limit()
        box('嗨！\n请进行身份证扫描\n点击准备好了再扫描哈')
        self.change_page.wait_scan_front_process()
        self.change_page.wait_scan_back_process()
        self.change_page.click_confirmed()
        self.change_page.assert_text_exist("请先编辑住址")
        self.change_page.click_edit_address()
        self.change_page.click_province_city_district()
        self.change_page.click_province(kwargs["province"])
        self.change_page.click_city(kwargs["city"])
        self.change_page.click_district(kwargs["district"])
        self.change_page.input_address(kwargs["address"])
        self.change_page.click_save()
        self.change_page.click_confirmed()
        self.change_page.wait_loading()
        assert self.change_page.check_text_existance("提升限额") is False, "提升限额入口依然存在"
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("关于零钱")
        self.change_page.assert_text_exist("二类户")

    @allure.story("再次绑卡操作")
    def bind_another_bank_card(self, scene, **kwargs):
        self.change_page.click_change_card_package()
        assert self.change_page.bank_card_number() == 1, "零钱卡包绑定了超过1张银行卡"
        self.change_page.click_add_card()
        self.change_page.click_take_photo_h5()
        self.change_page.press_key("back")
        self.change_page.click_supported_bank_h5()
        self.common_page.click_back_arrow()
        self.change_page.input_bank_card_number_h5(kwargs["bank_card_number"])
        self.change_page.click_next_step_h5()
        self.change_page.input_mobile_number_h5(kwargs["mobile_number"])
        self.change_page.click_cgb_account_agreement()
        self.change_page.scroll_to_boundary("end")
        self.change_page.assert_text_exist("其他")
        self.common_page.click_back_arrow()
        self.change_page.click_next_step_h5()
        if scene == 1:
            # 生产环境
            self.common_flow.copy_verification_code_from_notification()
            self.change_page.long_click_verification_code_box_h5()
            self.common_page.click_paste()
        elif scene == 2:
            # 测试环境
            self.change_page.input_verify_code_h5(kwargs["verify_code"])
        self.change_page.click_next_step_h5()
        assert self.change_page.bank_card_number() == 2, "零钱卡包期望有2张银行卡"
        self.common_page.click_back_arrow()
        self.change_page.assert_text_exist("零钱")

    @allure.story('删除绑卡操作')
    def delete_bound_card(self):
        self.change_page.click_change_card_package()
        self.change_page.click_first_bank_card()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("删除")
        self.common_page.click_button3("删除")
        if self.change_page.check_text_existance("卡片详情"):
            self.common_page.click_back_arrow()
        self.change_page.assert_text_exist("零钱绑定卡")
        assert self.change_page.bank_card_number() == 1, "零钱卡包还剩2张绑定卡，期望1张"
        self.common_page.click_back_arrow()
        self.change_page.assert_text_exist("零钱")

    @allure.story('注销零钱操作')
    def cancel_change_account(self, **kwargs):
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("关于")
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("注销")
        if self.change_page.check_text_existance("解绑"):
            self.change_page.click_unbind()
            self.common_page.wait_loading()
        self.change_page.click_next()
        self.common_page.input_wallet_password(kwargs["wallet_password"])
        box('嗨！\n请进行人脸识别\n点击准备好了再让脸进入识别框里哈')
        self.change_page.face_recognition()
        self.change_page.wait_cancel_account_process()
        self.change_page.assert_text_exist("注销完成")
        self.change_page.click_complete()
        self.mine_page.assert_text_exist("我的资产")

