#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/28
File: conftest.py
"""

import os

import pytest

from common.config_parser import ReadConfig
from common.utils import get_installed_package_name
from common.yaml_parser import ReadYaml
from soloop.v112 import root_dir


@pytest.fixture(scope="function")
def data():
    filename = "data.yaml"
    return ReadYaml().read(os.path.join(root_dir, "data", filename))


# @pytest.fixture(scope="function")
# def clear_all_message(driver):
#     driver.open_notification()
#     if ReadConfig().get_platform == "android":
#         element = driver(resourceId="com.android.systemui:id/shelf_dismiss_text")
#         if element.wait(timeout=3.0):
#             element.click()
#         else:
#             driver.press("back")

