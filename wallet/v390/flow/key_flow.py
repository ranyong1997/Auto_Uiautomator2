#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.messagebox import box
from wallet.v390.flow.setting_flow import SettingFlow
from wallet.v390.page import HomePage, KeyPage, SettingPage, CommonPage


class KeyFlow(object):

    def __init__(self, driver):
        self.key_page = KeyPage(driver)
        self.home_page = HomePage(driver)
        self.common_page = CommonPage(driver)
        self.setting_page = SettingPage(driver)
        self.setting_flow = SettingFlow(driver)

    @allure.story("进入添加门禁卡页操作")
    def goto_add_card_page(self, scene):
        if scene == 1:
            # 去开门---立即开通
            self.home_page.click_go_open_door()
        elif scene == 2:
            # 去开门---添加卡
            self.home_page.click_go_open_door()
            self.common_page.click_add_card()
        elif scene == 3:
            # 卡包---添加卡(+)---添加门禁卡
            self.home_page.click_card_package()
            self.home_page.click_add()
            self.home_page.click_add_key()

    @allure.story("添加实体门禁卡操作")
    def open_physical_access_card(self, **kwargs):
        self.key_page.click_physical_access_card()

        self.key_page.click_add_access_card()
        box('嗨！\n请用实体门禁卡靠近测试机NFC区域\n点击准备好了再贴卡哈')
        self.key_page.sense_access_card()
        if self.setting_page.check_text_existance("姓名和身份证号码"):
            self.setting_flow.real_name_verification(**kwargs)
            self.setting_page.press_key("back")
            box('嗨！\n请用实体门禁卡靠近测试机NFC区域\n点击准备好了再贴卡哈')
            self.key_page.sense_access_card()
        self.key_page.wait_import_access_card_process()
        self.key_page.click_save()
        self.key_page.assert_text_exist("靠近读卡器")

    @allure.story("生成空白卡操作")
    def open_manual_access_card(self):
        self.key_page.click_manual_access_card()
        self.key_page.click_add_access_card()
        self.key_page.wait_create_white_card_process()
        self.key_page.scroll_to_boundary()
        self.key_page.click_write_in_now()
        self.key_page.sleep(3.0)
        self.key_page.click_unrecognized_device()
        self.key_page.scroll_to_boundary()
        self.key_page.click_finish_on_tips_page()
        self.key_page.sleep(2.0)
        self.common_page.click_back_arrow()
        self.key_page.click_write_in_later()

    @allure.story("编辑门禁卡操作")
    def edit_access_card(self, **kwargs):
        self.home_page.click_go_open_door()
        self.common_page.click_card_detail()
        self.key_page.click_card_name()
        self.key_page.input_card_name(kwargs["card_name"])
        self.key_page.click_save()
        self.key_page.click_display_switch()
        self.key_page.click_card_cover_style()
        self.key_page.click_random_cover()
        self.key_page.scroll_until_element_appear(textContains="自定义")
        self.key_page.click_random_cover()
        self.key_page.click_custom_cover()
        self.key_page.click_first_picture()
        self.key_page.click_save_picture()
        self.key_page.click_save_cover()
        self.key_page.sleep(4.0)
        self.key_page.click_card_tips()
        self.key_page.click_finish_on_tips_page()
        self.key_page.press_key("back")
        self.home_page.assert_text_exist("卡包")

    @allure.story("门禁卡迁卡操作")
    def access_card_transfer_operation(self, **kwargs):
        self.key_page.click_physical_access_card()
        self.key_page.click_Access_card_1()
        self.key_page.click_Move_in_to_this_machine()
        self.key_page.wait_Moving_in_card()
        self.key_page.click_carry_out()

    @allure.story("删除门禁卡操作")
    def delete_access_card(self, **kwargs):
        self.home_page.click_go_open_door()
        self.common_page.click_card_detail()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("删除")
        self.key_page.click_delete_reason_checkbox()
     #   self.key_page.input_delete_card_reason(kwargs["delete_reason"])
        self.key_page.click_confirm_delete()
        self.key_page.wait_delete_process()
    #  self.key_page.assert_text_exist("选择开通类型")

    @allure.story("删除空白卡操作")
    def delete_blank_card(self):
        self.home_page.click_card_package()
        self.home_page.scroll_until_element_appear(textContains="待录入")
        self.home_page.click_write_in_of_blank_card()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("删除")
        self.common_page.click_button1("删除")
        self.key_page.wait_delete_process()
        assert not self.key_page.check_text_existance("待录入")
