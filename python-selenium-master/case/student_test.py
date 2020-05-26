from bussinses.funnicgong import Logintest
from bussinses.funnicgong import StudentTest
import ddt
import unittest
import os
from util import log
from selenium import webdriver
from util.gettestdata import huoqu_test
# -*- coding: utf-8 -*-
# 数据填充

path = os.getcwd()
case_path = path+'\\data\\case.xlsx'

# 参数格式为[{},{}]或[{}]
student_data = huoqu_test(case_path, 1)
login_list = huoqu_test(case_path, 0)

# excle内同一sheet取值
data = login_list[0]

# 用列表包一层，是因为格式问题
login_data = [data]


@ddt.ddt
class Testselect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logs = log.log_message()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.login_fun = Logintest(cls.driver)
        cls.student_fun = StudentTest(cls.driver)

    @ddt.data(*login_data)
    def test_a_login(self, login_data):
        self.username = login_data['username']
        self.password = login_data['password']

        self.login_result = self.login_fun.login(self.username, self.password)
        self.logs.info_log('实际返回数据为:%s' % self.login_result)

    @ddt.data(*student_data)
    def test_b_name_select(self, student_data):
        self.student_name = student_data['student_name']

        self.student_result = self.student_fun.name_select(self.student_name)
        self.logs.info_log('实际返回数据为:%s' % self.student_result)

    def test_c_page(self):
        self.student_result = self.student_fun.fenye()
        self.logs.info_log('实际返回数据为:%s' % self.student_result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
