#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_user_api.py

import pytest

from api_auto_demo.api_auto_demo2.api.contact.department import Department
from api_auto_demo.api_auto_demo2.api.contact.user import User
from api_auto_demo.api_auto_demo2.testcases.base_testcase import BaseTestcase


class TestUserApi(BaseTestcase):
    def setup_class(self):
        self.user = User()
        self.user.clear_members()

        # 创建部门
        self.dp = Department()
        self.dp.clear()
        name = "test_department"
        parentid = 1
        r = self.dp.create_department(name=name, parentid=parentid)
        self.department_id = r.json()["id"]
        self.department_list = [self.department_id]

    def test_get_member(self):
        userid = "HuangZeShan"
        r = self.user.get_member(userid)
        self.assert_suuc_code(r)
        self.assert_eq(r.json()["userid"], userid)

    def test_create_member(self):
        userid = "123"
        name = "test123"
        mobile = "13700000000"
        department_list = self.department_list
        r = self.user.create_member(userid, name, mobile, department_list)
        self.assert_suuc_code(r)

        # 查询成员
        r = self.user.get_member(userid)
        self.assert_suuc_code(r)
        self.assert_eq(r.json()["userid"], userid)
        self.assert_eq(r.json()["name"], name)
        self.assert_eq(r.json()["mobile"], mobile)
        self.assert_eq(r.json()["department"], department_list)

    def test_update_member(self):
        # 新增成员
        userid = "1234"
        name = "test1234"
        mobile = "13700000001"
        department_list = self.department_list
        r = self.user.create_member(userid, name, mobile, department_list)
        self.assert_suuc_code(r)

        name = "test1234edit"
        r = self.user.update_member(userid, name)
        self.assert_suuc_code(r)

        # 查询成员
        r = self.user.get_member(userid)
        self.assert_suuc_code(r)
        self.assert_eq(r.json()["userid"], userid)
        self.assert_eq(r.json()["name"], name)

    def test_delete_member(self):
        # 新增成员
        userid = 12345
        name = "test12345"
        mobile = "13700000002"
        department_list = self.department_list
        r = self.user.create_member(userid, name, mobile, department_list)
        self.assert_suuc_code(r)

        r = self.user.delete_member(userid)
        self.assert_suuc_code(r)

        # 查询成员
        r = self.user.get_member(userid)
        self.assert_eq(r.json()["errcode"], 60111)

    @pytest.mark.smoke
    @pytest.mark.department
    def test_smoke(self):
        """创建、编辑、删除、查询成员全流程验证/冒烟场景"""
        userid = "12356"
        name = "test1234"
        mobile = "13700000005"
        department_list = self.department_list
        r = self.user.create_member(userid, name, mobile, department_list)
        self.assert_suuc_code(r)

        # 查询成员
        r = self.user.get_member(userid)
        self.assert_suuc_code(r)
        self.assert_eq(r.json()["userid"], userid)
        self.assert_eq(r.json()["name"], name)
        self.assert_eq(r.json()["mobile"], mobile)
        self.assert_eq(r.json()["department"], department_list)

        # 编辑成员
        name = "test1234edit"
        r = self.user.update_member(userid, name)
        self.assert_suuc_code(r)

        # 删除成员
        r = self.user.delete_member(userid)
        self.assert_suuc_code(r)

        # 查询成员
        r = self.user.get_member(userid)
        self.assert_eq(r.json()["errcode"], 60111)
