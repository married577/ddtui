from bussinses.funnicgong import Logintest
from bussinses.funnicgong import SchoolTest
import ddt
import unittest
import os
from util import log
from selenium import webdriver
from util.gettestdata import huoqu_test
# -*- coding: utf-8 -*-

path = os.getcwd()
case_path = path+'\\data\\case.xlsx'

# 参数格式为[{},{}]或[{}]
school_data = huoqu_test(case_path, 2)
login_list = huoqu_test(case_path, 0)

# excle内同一sheet取值
data = login_list[0]

# 用列表包一层，是因为格式问题
login_data = [data]


@ddt.ddt
class TestSchoolselect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logs = log.log_message()
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.login_fun = Logintest(cls.driver)
        cls.school_fun = SchoolTest(cls.driver)

    @ddt.data(*login_data)
    def test_a_login(self, login_data):
        self.username = login_data['username']
        self.password = login_data['password']

        self.login_result = self.login_fun.login(self.username, self.password)
        self.logs.info_log('实际返回数据为:%s' % self.login_result)

    @ddt.data(*school_data)
    def test_b_name_select(self, school_data):
        self.school_name = school_data['school_name']

        self.school_result = self.school_fun.name_select(self.school_name)
        self.logs.info_log('实际返回数据为:%s' % self.school_result)

    def test_c_name_select2(self):
        self.school_result = self.school_fun.name_select2()
        self.logs.info_log('实际返回数据为:%s' % self.school_result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
