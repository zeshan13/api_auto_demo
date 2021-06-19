#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_wework_api.py
import time

from .tools import Tools
from .wework_api import WeWorkApi


class TestWeWorkApi:
    def setup_class(self):
        self.api = WeWorkApi()
        self.api.clear_tags()
        t = Tools()
        wework_api_path = "wework_api.yaml"
        self.datas = t.read_yaml(wework_api_path)

    def test_get_corp_tag(self):
        res = self.api.get_corp_tag()
        # 断言返回errorcode
        assert res.json()["errcode"] == 0
        assert res.json()["tag_group"] == []

    def test_add_corp_tag(self):
        json_datas = self.datas["test_add_corp_tag"]["json_datas"]
        res = self.api.add_corp_tag(json_datas=json_datas)
        # 断言返回errorcode
        assert res.json()["errcode"] == 0
        # 获取返回结果中的tagid
        tag_id = res.json()["tag_group"]["tag"][0]["id"]
        # 获取返回结果中的groupid
        group_id = res.json()["tag_group"]["group_id"]
        # 调用get_corp_tag查询接口，查询当前所有标签
        rsp_body = self.api.get_corp_tag().json()
        # 获取tag_id列表
        tag_id_list = [j["id"] for i in rsp_body["tag_group"] for j in i["tag"]]
        # 获取group_id列表
        group_id_list = [i["group_id"] for i in rsp_body["tag_group"]]
        # 断言tag_id是否在返回的列表中
        assert tag_id in tag_id_list
        # 断言group_id是否在返回的列表中
        assert group_id in group_id_list

    def test_del_corp_tag_by_tag_id(self):
        # 添加标签
        json_datas = self.datas["test_del_corp_tag_by_tag_id"]["add_json_datas"]
        res = self.api.add_corp_tag(json_datas=json_datas)
        # 断言返回errorcode
        assert res.json()["errcode"] == 0
        # 获取返回结果中的tagid
        tag_id = res.json()["tag_group"]["tag"][0]["id"]
        self.datas["test_del_corp_tag_by_tag_id"]["json_datas"]["tag_id"][0] = tag_id

        # 删除标签
        json_datas = self.datas["test_del_corp_tag_by_tag_id"]["json_datas"]
        res = self.api.del_corp_tag(json_datas=json_datas)
        # 断言返回errorcode
        assert res.json()["errcode"] == 0

        # 调用get_corp_tag查询接口，查询当前所有标签
        rsp_body = self.api.get_corp_tag().json()
        # 获取tag_id列表
        tag_id_list = [j["id"] for i in rsp_body["tag_group"] for j in i["tag"]]
        # 断言，被删除的tag_id不在tag_id列表中
        assert tag_id not in tag_id_list

    def test_del_corp_tag_by_group_id(self):
        # 添加标签
        json_datas = self.datas["test_del_corp_tag_by_group_id"]["add_json_datas"]

        res = self.api.add_corp_tag(json_datas=json_datas)
        # 断言返回errorcode
        assert res.json()["errcode"] == 0
        # 获取返回结果中的groupid
        group_id = res.json()["tag_group"]["group_id"]
        self.datas["test_del_corp_tag_by_group_id"]["json_datas"]["group_id"][0] = group_id
        # 删除标签
        json_datas = self.datas["test_del_corp_tag_by_group_id"]["json_datas"]
        res = self.api.del_corp_tag(json_datas=json_datas)
        # 断言返回errorcode
        assert res.json()["errcode"] == 0

        # 调用get_corp_tag查询接口，查询当前所有标签
        rsp_body = self.api.get_corp_tag().json()
        # 获取group_id列表
        group_id_list = [i["group_id"] for i in rsp_body["tag_group"]]
        # 断言，被删除的group_id不在group_id列表中
        assert group_id not in group_id_list

    def test_edit_corp_tag(self):
        # 添加标签
        json_datas = self.datas["test_edit_corp_tag"]["add_json_datas"]
        res = self.api.add_corp_tag(json_datas=json_datas)
        # 断言返回errorcode
        assert res.json()["errcode"] == 0
        # 获取返回结果中的tagid
        tag_id = res.json()["tag_group"]["tag"][0]["id"]
        self.datas["test_edit_corp_tag"]["json_datas"]["id"] = tag_id
        self.datas["test_edit_corp_tag"]["get_json_datas"]["tag_id"][0] = tag_id

        # 编辑标签
        json_datas = self.datas["test_edit_corp_tag"]["json_datas"]
        res = self.api.edit_corp_tag(json_datas=json_datas)
        # 断言返回errorcode
        assert res.json()["errcode"] == 0

        # 调用get_corp_tag查询接口，查询修改的tag name
        json_datas_1 = self.datas["test_edit_corp_tag"]["get_json_datas"]
        rsp_body = self.api.get_corp_tag(json_datas_1).json()
        # 断言 tag_name是否与传入的一致
        assert rsp_body["tag_group"][0]["tag"][0]["name"] == json_datas["name"]
