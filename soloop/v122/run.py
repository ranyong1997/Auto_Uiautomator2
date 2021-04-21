#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: W9007851
Date: 2020/10/28
File: run.py
"""

import os
import time
import pytest

from common import project_dir
from common.config_parser import ReadConfig
from soloop.v122 import root_dir

platform = ReadConfig().get_platform
os.system('python -m uiautomator2 init')


def local_run():
    # env = ReadConfig().get_env
    args = [root_dir + "/case/", "-m B", "--alluredir", project_dir + "/report/raw_data/"]   # 单独执行一个级别用例
    # args = [root_dir + "/case/", "--alluredir", project_dir + "/report/raw_data/"]
    # args = [root_path + "/case/", "-m", env, "--alluredir", project_dir + "/report/raw_data/"]
    # args = [root_dir + "/case/", "-m S", "--reruns", "1", "--reruns-delay", "5", "--alluredir", project_dir + "/report/raw_data/"]
    # args = [root_dir + "/case/", "--reruns", "1", "--reruns-delay", "5", "--alluredir", project_dir + "/report/raw_data/"]
    pytest.main(args)


def generate_report():
    report_path = os.path.join(project_dir, "report", "html_report_" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
    os.system("allure generate " + project_dir + "/report/raw_data/ -o " + report_path)
    return report_path


def open_report(report_path):
    os.system("allure open " + report_path)


if __name__ == "__main__":
    local_run()
    open_report(generate_report())