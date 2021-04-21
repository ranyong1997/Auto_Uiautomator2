#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Author: 80243990
Date: 2020/12/15
File: test_speed.py
"""
import allure

from conftest import serial, package_name
from wallet.v390.page import HomePage


@allure.epic("速度类测试")
class TestSpeed:

    @allure.feature("冷启动")
    @allure.title("冷启动10次统计启动速度")
    def test_speed_0001(self, driver, speed):
        model_file = "D:\\Development\\MTN\\tools\\timemachine-project\\videos\\cold_launch.h5"
        speed.model_file(model_file)  # 设置训练模型路径
        speed.end_stage_list_index(2)  # 表示取第几个非稳定阶段
        speed.end_stage_frame_index(-1)  # 表示取上面非稳定阶段的第几帧
        driver.swipe_ext("left")
        for i in range(10):
            speed.start_record(serial, package_name)
            driver(text="钱包").click()
            driver.sleep(5)
            speed.stop_record(serial)
            driver.app_stop(package_name)

    @allure.feature("热启动")
    @allure.title("热启动10次统计启动速度")
    def test_speed_0002(self, driver, speed):
        model_file = "D:\\Development\\MTN\\tools\\timemachine-project\\videos\\hot_launch.h5"
        speed.model_file(model_file)  # 设置训练模型路径
        speed.end_stage_list_index(0)  # 表示取第几个非稳定阶段
        speed.end_stage_frame_index(-1)  # 表示取上面非稳定阶段的第几帧
        driver.swipe_ext("left")
        driver(text="钱包").click()
        driver.sleep(3)
        driver.press("home")
        for i in range(10):
            speed.start_record(serial, package_name)
            driver(text="钱包").click()
            driver.sleep(3)
            speed.stop_record(serial)
            driver.press("home")

    @allure.feature("唤醒启动")
    @allure.title("唤醒启动10次统计启动速度")
    def test_speed_0003(self, driver, speed):
        model_file = "D:\\Development\\MTN\\tools\\timemachine-project\\videos\\wake_up.h5"
        speed.model_file(model_file)  # 设置训练模型路径
        speed.start_stage("0")
        # speed.start_stage_list_index(0)
        # speed.start_stage_frame_index(0)
        speed.end_stage("2")  # 设置结束帧属于哪个阶段，最终会取该阶段的第一帧作为结束帧
        # speed.end_stage_list_index(1)  # 表示取第几个非稳定阶段
        # speed.end_stage_frame_index(-1)  # 表示取上面非稳定阶段的第几帧
        driver.swipe_ext("left")
        for i in range(2):
            speed.start_record(serial, package_name)
            driver.press("power")
            driver.sleep(0.5)
            driver.press("power")
            driver.press("power")  # 双击电源唤醒
            driver.sleep(3.5)
            speed.stop_record(serial)
            driver.app_stop(package_name)
            driver.unlock()

    @allure.feature("页面切换")
    @allure.title("卡包切换10次统计启动速度")
    def test_speed_0004(self, driver, speed):
        model_file = "D:\\Development\\MTN\\tools\\timemachine-project\\videos\\card_package.h5"
        speed.model_file(model_file)  # 设置训练模型路径
        speed.end_stage_list_index(-2)  # 表示取第几个非稳定阶段
        speed.end_stage_frame_index(-1)  # 表示取上面非稳定阶段的第几帧
        home_page = HomePage(driver)
        driver.swipe_ext("left")
        for i in range(10):
            driver(text="钱包").click()
            home_page.click_home_tab()
            speed.start_record(serial, package_name)
            driver.sleep(2)
            home_page.click_card_package()
            driver.sleep(3)
            speed.stop_record(serial)
            driver.app_stop(package_name)
