#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from wallet.v390.flow.unionpay_flow import UnionPayFlow
from wallet.v390.page import HomePage, TrafficPage, CommonPage


class TrafficFlow(object):

    def __init__(self, driver):
        self.home_page = HomePage(driver)
        self.common_page = CommonPage(driver)
        self.traffic_page = TrafficPage(driver)
        self.unionpay_flow = UnionPayFlow(driver)

    @allure.story("进入添加公交卡页操作")
    def goto_add_card_page(self, scene):
        if scene == 1:
            # 去乘车---立即开通
            self.home_page.click_go_by_bus()
            # self.traffic_page.click_add_transit_card()
        elif scene == 2:
            # 去乘车---添加卡
            self.home_page.click_go_by_bus()
            self.common_page.click_add_card()
        elif scene == 3:
            # 卡包---添加卡(+)---添加公交卡
            self.home_page.click_card_package()
            self.home_page.click_add()
            self.home_page.click_add_transit_card()

    @allure.story("添加公交卡操作(通过搜索)")
    def open_transit_card(self, **kwargs):
        self.traffic_page.click_search_for_city_or_transit_card()
        self.traffic_page.input_search_info(kwargs["search_info"])
        self.traffic_page.click_specified_transit_card_by_search(kwargs["transit_card_name"])
        self.traffic_page.click_recharge_amount(kwargs["recharge_amount"])
        self.traffic_page.click_open()
        if kwargs["transit_card_name"] == "京津冀互联互通卡":
            # self.traffic_page.input_mobile_number(kwargs["mobile_number"])  # 这里默认会自动填充会员账号的手机号
            self.traffic_page.click_confirm()
        if kwargs["recharge_amount"] != "0":
            self.payment_channel_recharge(**kwargs)
        self.traffic_page.wait_generate_transit_card_process()
        self.traffic_page.click_finish()
        self.traffic_page.assert_text_exist("靠近读卡器")

    @allure.story("充值公交卡操作")
    def recharge_transit_card(self, **kwargs):
        self.home_page.click_go_by_bus()
        self.common_page.click_recharge()
        self.traffic_page.click_recharge_amount(kwargs["recharge_amount"])
        self.traffic_page.click_pay()
        self.payment_channel_recharge(**kwargs)

    @allure.story("支付渠道充值操作")
    def payment_channel_recharge(self, **kwargs):
        self.traffic_page.click_specified_recharge_channel(kwargs["recharge_channel"])
        self.traffic_page.click_recharge_button()
        if kwargs["recharge_channel"] == "OPPO Pay":
            self.unionpay_flow.oppo_pay_online_payment(**kwargs)
        elif kwargs["recharge_channel"] == "支付宝":
            pass
            # todo 使用支付宝支付流程，需要写在ThirdPartyFlow中
        elif kwargs["recharge_channel"] == "微信":
            pass
            # todo 使用微信支付流程，需要写在ThirdPartyFlow中

    @allure.story("遍历卡片详情页")
    def traverse_card_detail(self):
        self.home_page.click_go_by_bus()
        self.common_page.click_card_detail()
        self.traffic_page.click_card_info()
        self.traffic_page.assert_text_exist("卡号")
        self.common_page.click_back_arrow()
        self.traffic_page.click_transaction_record()
        self.traffic_page.assert_text_exist("无消费记录")
        self.traffic_page.swipe_screen("left")
        self.traffic_page.sleep(1.5)
        self.traffic_page.assert_text_exist("无充值记录")
        self.common_page.click_back_arrow()
        self.traffic_page.click_swipe_card()
        self.common_page.click_card_detail()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("问题帮助")
        self.traffic_page.assert_text_exist("公交卡刷卡失败怎么办？")
        self.traffic_page.swipe_screen("left")
        self.traffic_page.swipe_screen("left")
        self.traffic_page.swipe_screen("right")
        self.common_page.click_back_arrow()
        self.traffic_page.click_recharge()
        self.traffic_page.assert_text_exist("选择充值金额")
        self.traffic_page.click_cancel()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("用户协议")
        self.traffic_page.scroll_to_boundary("end")
        self.traffic_page.scroll_to_boundary("beginning")
        self.traffic_page.click_done()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("切卡设置")
        self.traffic_page.assert_text_exist("公交")
        self.common_page.click_back_arrow()
        self.common_page.click_back_arrow()
        self.common_page.click_exit()
        self.home_page.assert_text_exist("去乘车")

    @allure.story("迁出公交卡操作")
    def shift_out_transit_card(self, **kwargs):
        self.home_page.click_go_by_bus()
        self.common_page.click_card_detail()
        self.traffic_page.click_migrate_transit_card()
        self.traffic_page.scroll_to_boundary("end")
        self.traffic_page.click_start_migrate()
        self.traffic_page.input_activate_card_mobile_number(kwargs["mobile_number"])
        self.traffic_page.click_submit()
        self.traffic_page.wait_shift_out_transit_card_process()
        self.traffic_page.assert_text_exist("迁出完成")
        self.traffic_page.click_shift_out_finish()
     #   self.traffic_page.assert_text_exist("卡包")

    @allure.story("迁入公交卡操作")
    def shift_in_transit_card(self, scene, **kwargs):
        self.home_page.click_go_by_bus()
        self.traffic_page.click_transferable_transit_card()
        self.traffic_page.click_shift_in_this_device()
        self.traffic_page.input_mobile_number2(kwargs["mobile_number"])
        self.traffic_page.click_open()
        # self.traffic_page.click_continue()  # 弹窗检测会点
        self.traffic_page.wait_shift_in_transit_card_process()
        if scene == 1:
            # 从卡包迁卡
            self.traffic_page.assert_text_exist("迁入成功")
            self.traffic_page.click_shift_in_finish()
            self.traffic_page.assert_text_exist("卡包")
        elif scene == 2:
            # 从去乘车迁卡
            self.traffic_page.assert_text_exist("公交")
            self.common_page.click_exit()
            self.traffic_page.assert_text_exist("首页")


    @allure.story("删除公交卡操作")
    def delete_transit_card(self, **kwargs):
        self.home_page.click_go_by_bus()
        self.common_page.click_card_detail()
        self.common_page.click_more_options()
        self.common_page.click_popup_list_item("删卡")
        self.traffic_page.sleep(10)
        self.traffic_page.click_continue_deleting_card()
        self.common_page.click_button1("继续删除")
        # self.traffic_page.input_delete_card_mobile_number(kwargs["mobile_number"])
        self.traffic_page.click_delete_reason_checkbox()
        self.traffic_page.swipe_screen("up")
        # self.traffic_page.click_other_reason_checkbox()
        # self.traffic_page.input_delete_card_reason(kwargs["delete_reason"])
        self.traffic_page.click_continue_deleting_card()
        self.common_page.click_button1("确认删除")
        self.traffic_page.wait_delete_transit_card_process()
        # assert self.traffic_page.get_toast() == "删除成功", "删除公交卡卡异常"
        self.home_page.assert_text_exist("首页")
