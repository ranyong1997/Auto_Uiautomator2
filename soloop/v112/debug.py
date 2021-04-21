#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/28
File: debug.py
"""
import pytest
import uiautomator2 as u2

from soloop.v112.flow import *
from soloop.v112.page import *


def steps(d):   # 执行单条用例
    # videoexport_page = VideoExportPage(d)
    # videoexport_page.click_my_tab()
    # a_page = APage(d)
    # a_page.click_fast_film()
    pass


def debug_by_pytest():   # 执行整个tets_x.py 的用例
    args = ["case/test_level_a.py"]
    pytest.main(args)


def debug():
    driver = u2.connect()
    driver.implicitly_wait(5.0)
    driver.set_fastinput_ime(True)
    driver.unlock()
    steps(driver)
    driver.set_fastinput_ime(False)


if __name__ == "__main__":
    debug_by_pytest()
    # debug()
