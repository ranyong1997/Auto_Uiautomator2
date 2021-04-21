#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/11/11
File: mark_a_page.py
"""

import allure
import random
from common.base_page import BasePage
from common.config_parser import ReadConfig
from soloop.v112.element.element_router import ElementRouter


class Mark_B_Page(BasePage):

    def __init__(self, driver):
        super(Mark_B_Page, self).__init__(driver)
        self.element = ElementRouter.select(self.__class__.__name__)

    @allure.step("点击快速成片")
    def click_fast_film(self):
        self.find_element_and_click(**self.element["fast_film"])




