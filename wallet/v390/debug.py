#!/usr/bin/env python
# -*- coding:utf-8 -*-


import uiautomator2 as u2

from wallet.v380.flow import *
from wallet.v380.page import *


def steps(d):
    p = KeyPage(d)
    assert p.check_text_existance("待录入")


def debug():
    driver = u2.connect()
    driver.implicitly_wait(5.0)
    driver.set_fastinput_ime(True)
    driver.unlock()
    steps(driver)
    driver.set_fastinput_ime(False)


if __name__ == "__main__":
    debug()
