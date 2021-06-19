#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_department_api.py
import pytest

from api_auto_demo.api_auto_demo2.api.contact.department import Department
from api_auto_demo.api_auto_demo2.testcases.base_testcase import BaseTestcase


class TestDepartmentApi(BaseTestcase):
    def setup_class(self):
        self.dp = Department()

    def setup(self):
        self.dp.clear()

    def test_get_department(self):
        r = self.dp.get_department_list()
        self.assert_suuc_code(r)
        self.assert_eq(len(r.json()["department"]), 1)

    def test_create_department(self):
        name = "test_department"
        parentid = 1
        r = self.dp.create_department(name=name, parentid=parentid)
        self.assert_suuc_code(r)

        id = r.json()["id"]
        r = self.dp.get_department_list()
        self.assert_suuc_code(r)
        id_list = [department["id"] for department in r.json()["department"]]
        self.assert_in(id, id_list)

    def test_update_department(self):
        name = "test_department"
        parentid = 1
        r = self.dp.create_department(name=name, parentid=parentid)
        id = r.json()["id"]

        name = "update_" + name
        r = self.dp.update_department(id=id, name=name)
        self.assert_suuc_code(r)

        r = self.dp.get_department_list()
        self.assert_suuc_code(r)
        name_list = [department["name"] for department in r.json()["department"]]
        self.assert_in(name, name_list)

    def test_delete_department(self):
        name = "test_department"
        parentid = 1
        r = self.dp.create_department(name=name, parentid=parentid)
        id = r.json()["id"]

        r = self.dp.delete_department(id=id)
        self.assert_suuc_code(r)

        r = self.dp.get_department_list()
        self.assert_suuc_code(r)
        id_list = [department["id"] for department in r.json()["department"]]
        self.assert_not_in(id, id_list)

    @pytest.mark.smoke
    @pytest.mark.department
    def test_smoke(self):
        """创建、编辑、删除、查询部门全流程验证/冒烟场景"""
        # 创建部门
        name = "test_department"
        parentid = 1
        r = self.dp.create_department(name=name, parentid=parentid)
        self.assert_suuc_code(r)

        id = r.json()["id"]
        r = self.dp.get_department_list()
        self.assert_suuc_code(r)
        id_list = [department["id"] for department in r.json()["department"]]
        self.assert_in(id, id_list)

        # 编辑部门
        name = "update_" + name
        r = self.dp.update_department(id=id, name=name)
        self.assert_suuc_code(r)

        r = self.dp.get_department_list()
        self.assert_suuc_code(r)
        name_list = [department["name"] for department in r.json()["department"]]
        self.assert_in(name, name_list)

        # 删除部门
        r = self.dp.delete_department(id=id)
        self.assert_suuc_code(r)

        r = self.dp.get_department_list()
        self.assert_suuc_code(r)
        id_list = [department["id"] for department in r.json()["department"]]
        self.assert_not_in(id, id_list)
