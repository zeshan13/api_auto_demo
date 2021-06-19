#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_wework_tag.py

import time
import jsonpath
import pytest

from api_auto_demo.api_auto_demo2.api.externalcontact.tag import Tag


class TestWeWorkApi:
    def setup_class(self):
        self.tag = Tag()
        self.tag.clear_all_tags()

    def teardown_class(self):
        # （1）尽量不在teardown*中清理数据，如果进程被临时终止，将得不到清理
        # （2）用例跑完，数据不会被清理，方便排查问题
        pass

    def test_get_corp_tag(self):
        r = self.tag.get_corp_tag()
        assert r.status_code == 200
        # 断言返回errorcode
        assert r.json()["errcode"] == 0
        assert len(r.json()["tag_group"]) == 0

    def test_add_corp_tag(self):
        # 传参加入时间,避免重复添加
        rq = str(time.time())
        tag_name1 = "TAG_NAME_1" + rq
        tag_name2 = "TAG_NAME_2" + rq
        tag_list = [{"name": tag_name1}, {"name": tag_name2}]
        group_name = "GROP_NAME" + rq
        r = self.tag.add_corp_tag(tag_list=tag_list, group_name=group_name)
        # 断言返回errorcode
        assert r.json()["errcode"] == 0

        # 调用get_corp_tag查询接口，查询当前所有标签
        r = self.tag.get_corp_tag()
        assert r.json()["errcode"] == 0
        assert group_name in [group["group_name"] for group in r.json()["tag_group"]]

        # 使用jsonpath
        tag_name_list = jsonpath.jsonpath(r.json(), "$..tag[*].name")
        assert tag_name1 in set(tag_name_list)
        assert tag_name2 in set(tag_name_list)

    def test_del_corp_tag_by_tag_id(self):
        # 添加数据
        rq = str(time.time())
        tag_list = [{"name": "TAG_NAME_1" + rq}]
        r = self.tag.add_corp_tag(tag_list=tag_list, group_name="GROP_NAME" + rq)

        tag_id = r.json()["tag_group"]["tag"][0]["id"]

        tag_id_list = [tag_id]
        r = self.tag.del_corp_tag(tag_id_list=tag_id_list)

        # 断言返回errorcode
        assert r.json()["errcode"] == 0
        # 调用get_corp_tag查询接口，查询当前所有标签
        res_body = self.tag.get_corp_tag().json()
        # 获取tag_id列表
        tag_id_list = [j["id"] for i in res_body["tag_group"] for j in i["tag"]]
        # 断言，被删除的tag_id不在tag_id列表中
        assert tag_id not in tag_id_list

    def test_del_corp_tag_by_group_id(self):
        # 添加数据
        rq = str(time.time())
        tag_list = [{"name": "TAG_NAME_1" + rq}]
        r = self.tag.add_corp_tag(tag_list=tag_list, group_name="GROP_NAME" + rq)
        group_id = r.json()["tag_group"]["group_id"]

        json_data = {
            "json": {"group_id": [group_id]}
        }
        r = self.tag.del_corp_tag(**json_data)

        # 断言返回errorcode
        assert r.json()["errcode"] == 0
        # 调用get_corp_tag查询接口，查询当前所有标签
        res_body = self.tag.get_corp_tag().json()
        # 获取group_id列表
        group_id_list = [i["group_id"] for i in res_body["tag_group"]]
        # 断言，被删除的group_id不在group_id列表中
        assert group_id not in group_id_list

    def test_edit_corp_tag(self):
        # 添加数据
        rq = str(time.time())
        tag_list = [{"name": "TAG_NAME_1" + rq}]
        r = self.tag.add_corp_tag(tag_list=tag_list, group_name="GROP_NAME" + rq)
        tag_id = r.json()["tag_group"]["tag"][0]["id"]

        # 修改标签
        name = "EDIT_NAME_1" + rq
        r = self.tag.edit_corp_tag(tag_id=tag_id,name=name)
        # 断言返回errorcode
        assert r.json()["errcode"] == 0

        # 调用get_corp_tag查询接口，查询修改的tag name
        rsp_body = self.tag.get_corp_tag(tag_id).json()
        # 断言 tag_name是否与传入的一致
        tag_name_list = [tag["name"] for group in rsp_body["tag_group"] for tag in group["tag"]]
        assert name in tag_name_list

    @pytest.mark.smoke
    def test_smoke_flow(self):
        # 冒烟测试
        # 线上巡检
        # 全流程测试 添加 编辑 删除 查询
        # 重要测试数据

        # 添加标签
        rq = str(time.time())
        tag_list = [{"name": "TAG_NAME_1" + rq}]
        r = self.tag.add_corp_tag(tag_list=tag_list, group_name="GROP_NAME" + rq)
        tag_id = r.json()["tag_group"]["tag"][0]["id"]

        # 修改标签
        name = "EDIT_NAME_1" + rq
        r = self.tag.edit_corp_tag(tag_id=tag_id, name=name)
        # 断言返回errorcode
        assert r.json()["errcode"] == 0

        # 调用get_corp_tag查询接口，查询修改的tag name
        rsp_body = self.tag.get_corp_tag(tag_id).json()
        # 断言 tag_name是否与传入的一致
        tag_name_list = [tag["name"] for group in rsp_body["tag_group"] for tag in group["tag"]]
        assert name in tag_name_list

        # 删除标签
        tag_id_list = [tag_id]
        r = self.tag.del_corp_tag(tag_id_list=tag_id_list)
        # 断言返回errorcode
        assert r.json()["errcode"] == 0

        # 调用get_corp_tag查询接口，查询当前所有标签
        res_body = self.tag.get_corp_tag().json()
        # 获取tag_id列表
        tag_id_list = [j["id"] for i in res_body["tag_group"] for j in i["tag"]]
        # 断言，被删除的tag_id不在tag_id列表中
        assert tag_id not in tag_id_list
