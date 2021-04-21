#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/28
File: conftest.py
"""

import os

import pytest


from common.yaml_parser import ReadYaml
from soloop.v122 import root_dir


@pytest.fixture(scope="function")
def data():
    filename = "data.yaml"
    return ReadYaml().read(os.path.join(root_dir, "data", filename))


# @pytest.fixture(scope="function")
# def clear_all_message(driver):
#     driver.open_notification()
#     if ReadConfig().get_platform == "android":
#         driver(resourceId="com.android.systemui:id/shelf_dismiss_text").click()
