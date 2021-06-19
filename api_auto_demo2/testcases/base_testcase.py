#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : base_testcase.py
import logging

logging.basicConfig(level=logging.INFO)


class BaseTestcase:
    def login(self):
        pass

    def prepare_testdatas(self):
        pass

    def assert_eq(self, a, b):
        assert a == b

    def assert_not_eq(self, a, b):
        assert a == b

    def assert_in(self, a, b):
        assert a in b

    def assert_not_in(self, a, b):
        assert a not in b

    def assert_suuc_code(self, rsp, status_code=200, errcode=0):
        self.assert_eq(rsp.status_code, status_code)
        self.assert_eq(rsp.json()["errcode"], errcode)
