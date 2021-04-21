#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/28
File: element_router.py
"""
import os

from common.config_parser import ReadConfig
from common.yaml_parser import ReadYaml
from soloop.v128 import root_dir

# page和element文件的映射
mapping = {
    "VideoExportPage": "videoexport_cn_element.yaml",
    "MainPage": "main_cn_element.yaml",
    "Mark_A_Page": "videoexport_cn_element.yaml",
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
