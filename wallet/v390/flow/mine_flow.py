#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure

from wallet.v390.page import MinePage, CommonPage


class MineFlow(object):

    def __init__(self, driver):
        self.mine_page = MinePage(driver)
        self.common_page = CommonPage(driver)

    @allure.story("遍历我的页面入口")
    def traverse_mine_page(self):
        self.mine_page.click_mine_tab()
        self.mine_page.click_account_number()
        self.mine_page.assert_text_exist("信息")
        self.mine_page.press_key("back")
        self.mine_page.click_sign_in()
        if self.mine_page.check_text_existance("签到成功"):
            self.mine_page.click_close()
        self.mine_page.assert_text_exist("已签")
        self.mine_page.swipe_screen("up")
        self.common_page.click_back_arrow()
        self.mine_page.assert_text_exist("已签")
        self.mine_page.click_red_envelope()
        self.mine_page.assert_text_exist("总计")
        self.common_page.click_back_arrow()
        self.mine_page.click_coupon()
        self.mine_page.assert_text_exist("活动")
        self.common_page.click_back_arrow()
        self.mine_page.click_integration()
        self.mine_page.assert_text_exist("积分明细")
        self.common_page.click_back_arrow()
        self.mine_page.click_eye()
        self.mine_page.assert_text_exist("****")
        self.mine_page.click_my_protection()
        # self.mine_page.assert_text_exist("保单")
        self.common_page.click_back_arrow()
        self.mine_page.click_my_loan()
        self.mine_page.assert_text_exist("额度")
        self.common_page.click_back_arrow()
