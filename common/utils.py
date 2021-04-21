#!/usr/bin/env python
# -*- coding:utf-8 -*-


import logging
import os

import uiautomator2 as u2
from git import Repo

from common import project_dir
from common.config_parser import ReadConfig

platform = ReadConfig().get_platform


def get_android_version() -> int:
    android_version = os.popen("adb shell getprop ro.build.version.release").read().split(".")[0]
    logging.info("current android version is: {}".format(android_version))
    return int(android_version)


def get_installed_package_name() -> str:
    package_name = None
    for package in ReadConfig().get_package_name:
        package_info = os.popen("adb shell \"pm list packages |grep " + package + "\"").read()
        if package_info is not None:
            package_name = package
            break
    if package_name is None:
        raise RuntimeError("can not find package: {}".format(package_name))
    return package_name


def install_app(file_path):
    logging.info("install app path: {}".format(file_path))
    try:
        if platform == "android":
            os.popen("adb install -d -r " + file_path)
            d = u2.connect()
            d.unlock()
            if get_android_version() >= 10:
                logging.info("install app finished")
                return
            element = d(text="重新安装")
            if element.wait(timeout=10.0):
                element.click()
            d.click(0.75, 0.95)  # 点击安装(比例定位)
            element = d(textContains="安装完成")
            if element.wait(timeout=20.0):
                d.click(0.25, 0.95)  # 点击完成(比例定位)
        elif platform == "ios":
            pass
        logging.info("install app finished")
    except Exception as e:
        logging.error("install app failed： {}".format(e))
        raise


def git_pull():
    repo = Repo(project_dir)
    repo.remote().pull()
