#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: 80243990
Date: 2020/9/11
File: test_unionpay.py
"""
import allure
import pytest

from wallet.v390.flow.unionpay_flow import UnionPayFlow


@allure.epic("银联支付")
class TestUnionPay:

    @allure.feature("添加银行卡")
    @allure.title("使用借记卡开通OPPO Pay(生产环境)(NFC)")
    @pytest.mark.release
    @pytest.mark.nfc
    @pytest.mark.run(order=40)
    def test_unionpay_0001(self, driver, start_stop_app, data, clear_all_message):
        kwargs = data["test_unionpay_0001"]
        union_pay_flow = UnionPayFlow(driver)
        union_pay_flow.goto_add_card_page(scene=1)
        union_pay_flow.fill_in_debit_card_info(support_nfc=True, **kwargs)
        union_pay_flow.fill_in_safety_info(scene=1, support_nfc=True, **kwargs)

    @allure.feature("添加银行卡")
    @allure.title("再次添加信用卡(生产环境)(NFC)")
    @pytest.mark.release
    @pytest.mark.nfc
    @pytest.mark.run(order=41)
    def test_unionpay_0002(self, driver, start_stop_app, data, clear_all_message):
        kwargs = data["test_unionpay_0002"]
        union_pay_flow = UnionPayFlow(driver)
        union_pay_flow.goto_add_card_page(scene=2)
        union_pay_flow.fill_in_credit_card_info(support_nfc=True, **kwargs)
        union_pay_flow.fill_in_safety_info(scene=2, support_nfc=True, **kwargs)

    @allure.feature("查看银行卡")
    @allure.title("查看卡片详情页各项功能是否正常(NFC)")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.nfc
    @pytest.mark.run(order=42)
    def test_unionpay_0003(self, driver, start_stop_app):
        union_pay_flow = UnionPayFlow(driver)
        union_pay_flow.traverse_card_detail(support_nfc=True)

    @allure.feature("付款码")
    @allure.title("遍历付款码基本功能")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=43)
    def test_unionpay_0004(self, driver, start_stop_app, data):
        kwargs = data["test_unionpay_0004"]
        union_pay_flow = UnionPayFlow(driver)
        union_pay_flow.turn_off_and_on_payment_code(**kwargs)

    @allure.feature("扫一扫")
    @allure.title("使用扫一扫支付")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=44)
    def test_unionpay_0005(self, driver, start_stop_app, data):
        kwargs = data["test_unionpay_0005"]
        union_pay_flow = UnionPayFlow(driver)
        union_pay_flow.scan_payment(**kwargs)

    @allure.feature("删除银行卡")
    @allure.title("删除卡包中的首张银行卡")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=45)
    def test_unionpay_0006(self, driver, start_stop_app):
        union_pay_flow = UnionPayFlow(driver)
        union_pay_flow.delete_bank_card()

    @allure.feature("删除银行卡")
    @allure.title("删除卡包中的剩余银行卡,并注销钱包账户")
    @pytest.mark.release
    @pytest.mark.test
    @pytest.mark.run(order=49)
    def test_unionpay_0007(self, driver, start_stop_app, cancel_account):
        union_pay_flow = UnionPayFlow(driver)
        union_pay_flow.delete_bank_card()
