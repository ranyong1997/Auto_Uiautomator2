#!/usr/bin/env python
# -*- coding:utf-8 -*-


import allure
import pytest_check as check

from wallet.v390.page import ThirdPartyPage, HomePage, MinePage


class ThirdPartyFlow(object):

    def __init__(self, driver):
        self.third_party_page = ThirdPartyPage(driver)
        self.home_page = HomePage(driver)
        self.mine_page = MinePage(driver)

    def goto_services_page(self, scene):
        if scene == 1:
            self.home_page.click_all()
        elif scene == 2:
            self.mine_page.click_mine_tab()

    @allure.story("进出所有Webview服务")
    def in_out_all_webview_services(self, **kwargs):
        for service in kwargs["webview_services"]:
            self.enter_service_and_swipe_screen(service)
            self.third_party_page.press_key("back")

    @allure.story("进出所有QuickApp服务")
    def in_out_all_quickapp_services(self, **kwargs):
        for service in kwargs["quickapp_services"]:
            self.enter_service_and_swipe_screen(service)
            self.third_party_page.click_quickapp_close()

    @allure.story("进出可币充值服务")
    def in_out_cocoin_recharge_service(self, **kwargs):
        self.enter_service_and_swipe_screen(kwargs["cocoin_recharge"])
        self.third_party_page.press_key("back")
        self.third_party_page.click_cocoin_exit()

    def enter_service_and_swipe_screen(self, service):
        self.third_party_page.click_service(service)
        self.third_party_page.sleep(4.5)
        self.third_party_page.swipe_screen("up")
        self.third_party_page.swipe_screen("down")
        self.third_party_page.swipe_screen("left")
        self.third_party_page.swipe_screen("right")
        check.is_false(self.third_party_page.check_blank_screen(), "screen is blank")
        self.third_party_page.sleep(1.0)
