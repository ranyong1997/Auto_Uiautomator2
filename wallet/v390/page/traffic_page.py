#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from common.base_page import BasePage
from wallet.v390.element import ElementRouter


class TrafficPage(BasePage):

    def __init__(self, driver):
        super(TrafficPage, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    # ----------------- 欢迎页 -------------------
    @allure.step("点击添加公交卡")
    def click_add_transit_card(self):
        if self.check_element_existence(**self.element["activate_new_card"]):
            # 有待迁入的卡片时，开通新卡
            self.find_element_and_click(**self.element["activate_new_card"])
        else:
            self.find_element_and_click(**self.element["add_transit_card"])

    # ----------------- 添加公交卡 -------------------
    @allure.step("点击搜索城市或公交卡名称")
    def click_search_for_city_or_transit_card(self):
        self.find_element_and_click(check_toast=False, **self.element["search_for_city_or_transit_card"])

    @allure.step("搜索框输入公交卡/城市名称")
    def input_search_info(self, search_info):
        self.find_element_and_input(search_info, **self.element["search_box"])

    @allure.step("点击指定的公交卡(搜索结果页)")
    def click_specified_transit_card_by_search(self, card_name="京津冀互联互通卡"):
        element = self.element["card_name"]
        element["textContains"] = card_name
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("点击指定的公交卡(开卡页)")
    def click_specified_transit_card_without_search(self, card_name="京津冀互联互通卡"):
        element = self.element["card_name"]
        element["textContains"] = card_name
        self.scroll_until_element_appear(**element)
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("点击立即开通/支付(开卡页)")
    def click_open(self):
        self.find_element_and_click(**self.element["open"])

    @allure.step("输入登记手机号")
    def input_mobile_number(self, mobile_number):
        self.find_element_and_input(mobile_number, **self.element["mobile_number"])

    @allure.step("点击√确认")
    def click_confirm(self):
        self.find_element_and_click(**self.element["confirm"])

    @allure.step("选择支付宝")
    def click_alipay(self):
        self.find_element_and_click(**self.element["alipay"])

    @allure.step("正在生成公交卡...")
    def wait_generate_transit_card_process(self):
        self.wait_until_element_gone(**self.element["process_title"])

    @allure.step("点击完成")
    def click_finish(self):
        self.find_element_and_click(**self.element["finish"])

    # ----------------- 充值 -------------------
    @allure.step("点击取消(充值页)")
    def click_cancel(self):
        self.find_element_and_click(**self.element["cancel"])

    @allure.step("点击充值金额(默认0元)")
    def click_recharge_amount(self, recharge_amount="0"):
        element = self.element["recharge_amount"]
        element["text"] = recharge_amount
        self.find_element_and_click(check_toast=False, **element)

    @allure.step("点击支付(充值页)")
    def click_pay(self):
        self.find_element_and_click(**self.element["pay"])

    @allure.step("点击充值渠道")
    def click_specified_recharge_channel(self, recharge_channel):
        element = self.element["recharge_channel"]
        element["textContains"] = recharge_channel
        self.find_element_and_click(**element)

    @allure.step("点击支付￥xx元")
    def click_recharge_button(self):
        self.find_element_and_click(**self.element["recharge_button"])

    # ----------------- 卡片详情 -------------------
    @allure.step("点击充值")
    def click_recharge(self):
        self.find_element_and_click(**self.element["recharge"])

    @allure.step("点击卡片信息")
    def click_card_info(self):
        self.find_element_and_click(**self.element["card_info"])

    @allure.step("点击交易记录")
    def click_transaction_record(self):
        self.find_element_and_click(**self.element["transaction_record"])

    @allure.step("点击迁移公交卡")
    def click_migrate_transit_card(self):
        self.find_element_and_click(**self.element["move_transit_card"])

    @allure.step("点击刷卡")
    def click_swipe_card(self):
        self.find_element_and_click(**self.element["swipe_card"])

    @allure.step("点击乘车优惠")
    def click_ride_discount(self):
        # self.find_element_and_click(**self.element["ride_discount"])
        # 详情 无法准确获取坐标，暂时写死用相对值
        self.driver.click(0.87, 0.548)

    @allure.step("点击适用范围")
    def click_scope_of_application(self):
        self.find_element_and_click(**self.element["scope_of_application"])

    @allure.step("点击支持的城市")
    def click_supported_cities(self):
        self.find_element_and_click(**self.element["supported_cities"])

    @allure.step("点击完成(服务协议)")
    def click_done(self):
        self.find_element_and_click(**self.element["done"])

    # ----------------- 迁出公交卡 -------------------
    @allure.step("点击开始迁移")
    def click_start_migrate(self):
        self.find_element_and_click(**self.element["start_migrate"])

    @allure.step("输入开卡手机号")
    def input_activate_card_mobile_number(self, mobile_number):
        self.find_element_and_input(mobile_number, **self.element["activate_card_mobile_number"])

    @allure.step("点击提交")
    def click_submit(self):
        self.find_element_and_click(**self.element["submit"])

    @allure.step("正在迁出公交卡...")
    def wait_shift_out_transit_card_process(self):
        self.wait_until_element_gone(**self.element["shift_out_transit_card_process"])

    @allure.step("点击完成")
    def click_shift_out_finish(self):
        self.find_element_and_click(**self.element["shift_out_finish"])

    # ----------------- 迁入公交卡 -------------------
    @allure.step("点击可迁入的公交卡")
    def click_transferable_transit_card(self):
        self.find_element_and_click(**self.element["transferable_transit_card"])

    @allure.step("点击迁入至本机")
    def click_shift_in_this_device(self):
        self.find_element_and_click(**self.element["shift_in_this_device"])

    @allure.step("输入登记手机号")
    def input_mobile_number2(self, mobile_number):
        self.find_element_and_input(mobile_number, **self.element["mobile_number2"])

    @allure.step("点击继续")
    def click_continue(self):
        self.find_element_and_click(**self.element["continue"])

    @allure.step("正在迁入卡片...")
    def wait_shift_in_transit_card_process(self):
        self.wait_until_element_gone(**self.element["shift_in_transit_card_process"])

    @allure.step("点击完成")
    def click_shift_in_finish(self):
        self.find_element_and_click(ignore_toast="迁入成功", **self.element["shift_in_finish"])

    # ----------------- 删除公交卡 -------------------
    @allure.step("点击继续(确认)删卡")
    def click_continue_deleting_card(self):
        self.find_element_and_click(**self.element["continue_deleting_card"])

    @allure.step("输入手机号")
    def input_delete_card_mobile_number(self, mobile_number):
        self.find_element_and_input(mobile_number, **self.element["delete_card_mobile_number"])

    @allure.step("遍历点击删卡原因")
    def click_delete_reason_checkbox(self):
        for element in self.find_element(**self.element["delete_reason_checkbox"]):
            element.click()

    @allure.step("点击其他原因")
    def click_other_reason_checkbox(self):
        self.find_element_and_click(**self.element["other_reason_checkbox"])

    @allure.step("输入具体原因")
    def input_delete_card_reason(self, delete_reason):
        self.find_element_and_input(delete_reason, **self.element["delete_card_reason"])

    @allure.step("正在删除...")
    def wait_delete_transit_card_process(self):
        self.wait_until_element_gone(**self.element["delete_transit_card_process"])
