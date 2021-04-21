'''
Descripttion: 
version: 
Author: 冉勇
Date: 2021-04-01 18:51:27
LastEditTime: 2021-04-06 19:15:05
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import os
import re
import shutil
import time

import pytest

from common import project_dir
from common.config_parser import ReadConfig
from common.utils import get_android_version, install_app, git_pull
from wallet.v390 import root_dir

platform = ReadConfig().get_platform


def local_run():
    env = ReadConfig().get_env
    args = [root_dir + "/case/", "-m S", "--alluredir", project_dir + "/report/raw_data/"]
    # args = [root_dir + "/case/", "--alluredir", project_dir + "/report/raw_data/"]
    # args = [root_path + "/case/", "-m", env, "--alluredir", project_dir + "/report/raw_data/"]
    # args = [root_path + "/case/", "--reruns", "1", "--reruns-delay", "5", "--alluredir", project_dir+ "/report/raw_data/"]
    pytest.main(args)


def cct_run(*args):
    task_id, execution_id, pkg_list = args

    logging.info("update project code... ")
    git_pull()

    logging.info("start installing wallet")
    install_wallet(pkg_list)

    logging.info("start run test cases")
    env = None
    if execution_id == 1:
        env = "release"
    elif execution_id == 2:
        env = "test"
    args = [root_dir + "/case/", "-m", env, "--reruns", "1", "--reruns-delay", "5", "--alluredir",
            project_dir + "/report/raw_data/"]
    result = pytest.main(args)  # 0: pass, 1,2,3,4,5: fail
    logging.info("taskId: {}, run result: {}".format(task_id, result))

    src = generate_report()
    dst = os.path.join(project_dir, "web", "app", "static", "report", str(task_id))
    report_path = shutil.copytree(src, dst)

    logging.info("report path: {}".format(report_path))
    return result, report_path


def install_wallet(pkg_list):
    file_path = None
    if platform == "android":
        android_version = get_android_version()
        for pkg_path in pkg_list:
            if os.name == "nt":
                package_name = pkg_path.split("\\")[-1]
            else:
                package_name = pkg_path.split("/")[-1]
            if android_version >= 10:
                if re.match("FinShellWallet.+", package_name) is not None:
                    file_path = pkg_path
                    logging.info("matched: " + file_path)
                    break
            else:
                if re.match("OPPOWallet.+", package_name) is not None:
                    file_path = pkg_path
                    logging.info("matched: " + file_path)
                    break
    install_app(file_path)


def generate_report():
    report_path = os.path.join(project_dir, "report",
                               "html_report_" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
    os.system("allure generate " + project_dir + "/report/raw_data/ -o " + report_path)
    return report_path


def open_report(report_path):
    os.system("allure open " + report_path)


if __name__ == "__main__":
    local_run()
    open_report(generate_report())
