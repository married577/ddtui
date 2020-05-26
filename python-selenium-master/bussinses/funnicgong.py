import yaml
import os
from time import sleep
from util import log
# -*- coding: utf-8 -*-

# 返回当前进程的工作目录
path = os.getcwd()


# 登录模块封装
class Logintest:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.log_message()

        self.file = open(path+"\\data\\page_data.yaml", "r", encoding="utf-8")
        self.data = yaml.full_load(self.file)
        self.file.close()

        self.url = self.data['login'].get('url')
        self.username = self.data['login'].get('username')
        self.password = self.data['login'].get('password')
        self.denglu_btn = self.data['login'].get('denglu_btn')

        self.driver.get(self.url)
        self.driver.implicitly_wait(2)

    def login(self, username, password):
        try:
            self.driver.find_element_by_xpath(self.username).send_keys(username)
            sleep(2)
            self.driver.find_element_by_xpath(self.password).send_keys(password)
            sleep(2)
            self.driver.get_screenshot_as_file(path + '\\resultpang\\login.png')
            sleep(2)
            self.driver.find_element_by_xpath(self.denglu_btn).click()
            sleep(2)
        except Exception as e:
            self.logs.error_log('登录用例执行失败，原因：%s' % e)


# 学校模块封装
class SchoolTest:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.log_message()

        self.file = open(path+"\\data\\page_data.yaml", "r", encoding="utf-8")
        self.data = yaml.full_load(self.file)
        self.file.close()

        self.school_list = self.data['school'].get('school_list')
        self.school_list_select = self.data['school'].get('school_list_select')
        self.school_result_select = self.data['school'].get('school_result_select')
        self.school_select = self.data['school'].get('school_select')
        self.school_shichang_list = self.data['school'].get('school_shichang_list')
        self.school_shichang_choose = self.data['school'].get('school_shichang_choose')

    def name_select(self, school_name):
        try:
            self.driver.find_element_by_xpath(self.school_list).click()
            sleep(2)
            self.driver.find_element_by_xpath(self.school_list_select).send_keys(school_name)
            sleep(2)
            self.driver.find_element_by_xpath(self.school_result_select).click()
            sleep(2)
            self.driver.find_element_by_xpath(self.school_select).click()
            sleep(2)
            self.driver.get_screenshot_as_file(path + '\\resultpang\\school_select.png')
            sleep(2)
            self.driver.refresh()
        except Exception as e:
            self.logs.error_log('学校搜索用例执行失败，原因：%s' % e)

    def name_select2(self):
        try:
            self.driver.find_element_by_xpath(self.school_shichang_list).click()
            sleep(2)
            self.driver.find_element_by_xpath(self.school_shichang_choose).click()
            sleep(2)
            self.driver.find_element_by_xpath(self.school_select).click()
            sleep(2)
            self.driver.get_screenshot_as_file(path + '\\resultpang\\school_select2.png')
            sleep(2)
        except Exception as e:
            self.logs.error_log('学校搜索2用例执行失败，原因：%s' % e)


# 学生模块封装
class StudentTest:
    def __init__(self, driver):
        self.driver = driver
        self.logs = log.log_message()

        self.file = open(path+"\\data\\page_data.yaml", "r", encoding="utf-8")
        self.data = yaml.full_load(self.file)
        self.file.close()

        self.student_list = self.data['student'].get('student_list')
        self.student_name = self.data['student'].get('student_name')
        self.student_select = self.data['student'].get('student_select')
        self.student_js = self.data['student'].get('student_js')
        self.student_page = self.data['student'].get('student_page')

    def name_select(self, student_name):
        try:
            self.driver.find_element_by_xpath(self.student_list).click()
            sleep(2)
            self.driver.find_element_by_xpath(self.student_name).send_keys(student_name)
            sleep(2)
            self.driver.find_element_by_xpath(self.student_select).click()
            sleep(2)
            self.driver.get_screenshot_as_file(path + '\\resultpang\\student_select.png')
            sleep(2)
            self.driver.refresh()
        except Exception as e:
            self.logs.error_log('学生搜索用例执行失败，原因：%s' % e)

    def fenye(self):
        try:
            self.driver.execute_script(self.student_js)
            sleep(2)
            self.driver.find_element_by_xpath(self.student_page).click()
            sleep(2)
            self.driver.get_screenshot_as_file(path + '\\resultpang\\student_page.png')
            sleep(2)
        except Exception as e:
            self.logs.error_log('学生分页用例执行失败，原因：%s' % e)





