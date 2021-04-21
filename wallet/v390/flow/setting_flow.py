#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from wallet.v390.flow.common_flow import CommonFlow
from wallet.v390.page import CommonPage, SettingPage, HomePage, MinePage


class SettingFlow(object):

    def __init__(self, driver):
        self.setting_page = SettingPage(driver)
        self.common_page = CommonPage(driver)
        self.home_page = HomePage(driver)
        self.mine_page = MinePage(driver)
        self.common_flow = CommonFlow(driver)

    def goto_setting_page(self):
        self.mine_page.click_mine_tab()
        self.mine_page.click_setting()

    @allure.story("实名认证操作")
    def real_name_verification(self, scene=1, **kwargs):
        if scene == 2:
            # 设置入口
            self.setting_page.click_real_name_verification()
        self.setting_page.click_username()
        # self.setting_page.input_username(kwargs["username"])
        # self.setting_page.input_identification_number(kwargs["username"])    # 输入身份证

        self.setting_page.click_next_step()
        self.common_flow.copy_verification_code_from_notification()
        self.setting_page.long_click_verification_code_box()
        self.common_page.click_paste()
        self.setting_page.click_finish()
        # 点完成按钮后会跳转到认证信息页
        self.setting_page.check_on_certification_information_page()

    @allure.story("双击唤醒开关操作")
    def double_tap_power_switch(self):
        self.common_page.double_click_power_key()
        self.common_page.assert_text_exist("靠近读卡器")
        self.common_page.click_exit()
        self.setting_page.click_double_tap_power_switch()
        self.common_page.double_click_power_key()
        self.common_page.swipe_screen("up")
        self.setting_page.assert_text_exist("设置")
        self.setting_page.click_double_tap_power_switch()

    @allure.story("自动切卡操作")
    def auto_switch_card(self):
        self.setting_page.click_auto_switch()
        self.setting_page.click_auto_switch_switch()
        self.setting_page.click_loop_switch()
        self.setting_page.swipe_screen("up")
        self.setting_page.assert_text_exist("选择要切换的")
        self.setting_page.click_smart_switch()
        assert self.setting_page.check_text_existance("选择要切换的") is False, "列表未收起"
        self.setting_page.click_loop_switch()
        self.setting_page.click_door_card()
        self.setting_page.click_specified_card(index=0)
        self.setting_page.click_dont_choose()
        self.setting_page.assert_text_exist("请选择")
        self.setting_page.click_door_card()
        self.setting_page.click_specified_card(index=0)
        self.setting_page.click_done()
        assert self.setting_page.check_text_existance("请选择") is False, "未选择到指定的卡"

    @allure.story("一键修复操作")
    def one_click_repair(self):
        self.setting_page.click_one_click_repair()
        self.setting_page.click_start_repair()
        self.setting_page.assert_text_exist("未发现问题")
        self.setting_page.click_help_feedback()
        if self.setting_page.check_text_existance("加载中"):
            self.setting_page.wait_loading()
        self.setting_page.assert_text_exist("全部问题")
        self.setting_page.press_key("back")
        self.setting_page.click_complete()
        self.setting_page.assert_text_exist("设置")

    @allure.story("更改支付密码操作")
    def change_wallet_password(self, **kwargs):
        self.setting_page.click_password_setting()
        self.setting_page.click_change_password()
        self.common_page.input_wallet_password_h5(kwargs["wallet_password"])
        self.common_page.input_wallet_password_h5(kwargs["new_wallet_password"])
        self.common_page.input_wallet_password_h5(kwargs["new_wallet_password"])
        assert self.setting_page.get_toast() == "密码修改成功", "密码修改toast提示异常"
        self.setting_page.assert_text_exist("更改支付密码")

    @allure.story("忘记支付密码操作")
    def forget_wallet_password(self, scene, **kwargs):
        self.setting_page.click_password_setting()
        self.setting_page.click_forget_password()
        if scene == 1:
            # 通过身份信息找回
            self.setting_page.click_retrieve_through_id_info()
            self.setting_page.input_bank_card_number(kwargs["bank_card_number"])
            self.setting_page.input_username2(kwargs["username"])
            self.setting_page.input_identification_number2(kwargs["identification_number"])
            self.setting_page.input_mobile_number(kwargs["mobile_number"])
            self.setting_page.click_next()
        elif scene == 2:
            # 通过密保与手机号找回
            self.setting_page.click_retrieve_through_security()
            self.setting_page.click_security_question()
            self.setting_page.input_security_answer(kwargs["security_answer"])
            self.setting_page.click_next()
            self.common_flow.copy_verification_code_from_notification()
            self.setting_page.long_click_verification_code_box()
            self.common_page.click_paste()
            self.setting_page.click_next_step()
        self.common_page.input_wallet_password_h5(kwargs["new_wallet_password"])
        self.common_page.input_wallet_password_h5(kwargs["new_wallet_password"])
        assert self.setting_page.get_toast() == "密码重置成功", "密码重置toast提示异常"
        self.setting_page.assert_text_exist("更改支付密码")

    @allure.story("重置密保操作")
    def reset_security(self, **kwargs):
        self.setting_page.click_password_setting()
        self.setting_page.click_reset_security()
        self.common_page.input_wallet_password_h5(kwargs["wallet_password"])
        self.setting_page.click_security_question(kwargs["new_security_question"])
        self.setting_page.input_security_answer(kwargs["new_security_answer"])
        self.setting_page.click_next()
        self.common_flow.copy_verification_code_from_notification()
        self.setting_page.long_click_verification_code_box()
        self.common_page.click_paste()
        self.setting_page.click_next_step()
        self.setting_page.assert_text_exist("注销")

    @allure.story("关闭服务入口操作")
    def close_function_entry(self, **kwargs):
        self.setting_page.click_service_management()
        self.setting_page.click_function_item()
        for function_name in kwargs["entry_list"]:
            self.setting_page.click_specific_function_item_switch(function_name)
            self.common_page.click_button2("关闭")
        for num in range(3):
            self.common_page.click_back_arrow()
        self.home_page.click_home_tab()
        assert self.home_page.check_text_existance("精选专区") is False, "关闭精选专区后依然存在精选专区"
        self.home_page.scroll_to_boundary("end")
        self.home_page.click_open_more_services()
        self.setting_page.click_open_all()
        self.common_page.click_back_arrow()
        self.home_page.assert_text_exist("精选专区")

    @allure.story("协议、声明、版本核查操作")
    def check_protocol_statement_version(self):
        self.setting_page.swipe_screen("up")
        self.setting_page.assert_text_exist("版本号")
        self.setting_page.click_version()
        self.setting_page.click_service_management()
        self.setting_page.click_service_agreement()
        self.setting_page.scroll_to_boundary("end")
        self.common_page.click_back_arrow()
        self.setting_page.click_privacy_statement()
        self.setting_page.scroll_to_boundary("end")
        self.common_page.click_back_arrow()
        self.common_page.click_back_arrow()
        self.setting_page.assert_text_exist("设置")

    @allure.story("注销操作")
    def cancel_wallet_payment_account(self, scene=1, **kwargs):
        if scene == 2:
            # 实名认证入口
            self.setting_page.click_real_name_verification()
        self.setting_page.click_cancel_account()
        self.setting_page.click_confirm_logout()
        self.common_page.input_wallet_password_h5(kwargs["wallet_password"])
        assert self.setting_page.check_text_existance("注销钱包支付账户") is False, "注销入口依然存在，注销失败"
        self.common_page.click_back_arrow()
        self.home_page.click_home_tab()
