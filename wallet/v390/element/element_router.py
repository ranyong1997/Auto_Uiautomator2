#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: 80243990
Date: 2020/9/30
File: element_router.py
"""
import os

from common.config_parser import ReadConfig
from common.yaml_parser import ReadYaml
from wallet.v380 import root_dir

mapping = {
    "CommonPage": "common_cn_element.yaml",
    "HomePage": "home_cn_element.yaml",
    "UnionPayPage": "unionpay_cn_element.yaml",
    "MinePage": "mine_cn_element.yaml",
    "ChangePage": "change_cn_element.yaml",
    "TrafficPage": "traffic_cn_element.yaml",
    "KeyPage": "key_cn_element.yaml",
    "SettingPage": "setting_cn_element.yaml",
    "ThirdPartyPage": "third_party_cn_element.yaml",
    "MessagePage": "message_cn_element.yaml",
    "EIDPage": "eid_cn_element.yaml"
}


class ElementRouter:
    """定位元素选择路由"""

    @staticmethod
    def select(page_name):
        region = ReadConfig().get_region
        platform = ReadConfig().get_platform
        filename = None
        if platform == "android":
            if region == "cn":
                filename = mapping.get(page_name)
        elif platform == "ios":
            pass
        if filename is None:
            raise TypeError("cannot find the mapping relationship for " + page_name)
        return ReadYaml().read(os.path.join(root_dir, "element", filename))
