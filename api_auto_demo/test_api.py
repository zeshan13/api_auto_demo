#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_api.py
import json
import pytest
import requests
from tools import Tools


class TestAPI:
    def setup_class(self):
        # 获取token
        corpid = ""
        corpsecret = ""
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        res = requests.get(url=url, params=params)
        print("url:%s;params:%s" % (url, params))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        self.token = res.json()["access_token"]

        self.t = Tools()

        # 清理数据
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        params = {
            "access_token": self.token
        }
        res = requests.post(url=url, params=params)
        print("url:%s;params:%s" % (url, params))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        rsp = res.json()
        tag_list = [tag["id"] for group in rsp["tag_group"] for tag in group["tag"]]

        if len(tag_list) > 2:
            url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
            params = {"access_token": self.token}
            json_datas = {
                "tag_id": tag_list[2:]
            }

            res = requests.post(url=url, params=params, json=json_datas)
            print("url:%s;params:%s;datas:%s" % (url, params, json_datas))
            print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    def test_get_corp_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        params = {
            "access_token": self.token
        }
        res = requests.post(url=url, params=params)
        print("url:%s;params:%s" % (url, params))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        rsp = res.json()
        assert rsp["errcode"] == 0

    def test_add_corp_tag(self):
        tag_count = self.t.get_init_data("tag_count", "./init_datas_count.yaml")
        group_count = self.t.get_init_data("tag_count", "./init_datas_count.yaml")
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        params = {"access_token": self.token}
        json_datas = {
            "group_name": "GROUP_NAME_" + str(group_count),
            "tag": [{
                "name": "TAG_NAME_" + str(tag_count)
            }]
        }

        res = requests.post(url=url, params=params, json=json_datas)
        print("url:%s;params:%s;datas:%s" % (url, params, json_datas))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

        rsp = res.json()
        assert rsp["errcode"] == 0
        assert rsp["tag_group"]["group_name"] == json_datas["group_name"]
        assert rsp["tag_group"]["tag"][0]["name"] == json_datas["tag"][0]["name"]

    def test_edit_corp_tag(self):
        # 调用add_corp_tag新增标签，获取tag_id
        tag_count = self.t.get_init_data("tag_count", "./init_datas_count.yaml")
        group_count = self.t.get_init_data("tag_count", "./init_datas_count.yaml")
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        params = {"access_token": self.token}
        json_datas = {
            "group_name": "GROUP_NAME_" + str(group_count),
            "tag": [{
                "name": "TAG_NAME_" + str(tag_count)
            }]
        }

        res = requests.post(url=url, params=params, json=json_datas)
        print("url:%s;params:%s;datas:%s" % (url, params, json_datas))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        tag_id = res.json()["tag_group"]["tag"][0]["id"]

        # eidt
        tag_count = self.t.get_init_data("tag_count", "./init_datas_count.yaml")
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag"
        params = {"access_token": self.token}
        json_datas = {
            "id": tag_id,
            "name": "NEW_TAG_NAME" + str(tag_count),
        }
        res = requests.post(url=url, params=params, json=json_datas)
        print("url:%s;params:%s;datas:%s" % (url, params, json_datas))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

        rsp = res.json()
        assert rsp["errcode"] == 0

        # 调用get_corp_tag_list获取修改后的标签名
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        params = {
            "access_token": self.token
        }
        json_datas_1 = {
            "tag_id":
                [
                    tag_id
                ],
        }
        res = requests.post(url=url, params=params, json=json_datas_1)
        print("url:%s;params:%s;datas:%s" % (url, params, json_datas_1))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        rsp = res.json()
        # 断言 tag_name是否与传入的一致
        assert rsp["tag_group"][0]["tag"][0]["name"] == json_datas["name"]

    def test_del_corp_tag(self):
        # 调用add_corp_tag新增标签，获取tag_id
        tag_count = self.t.get_init_data("tag_count", "./init_datas_count.yaml")
        group_count = self.t.get_init_data("tag_count", "./init_datas_count.yaml")
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        params = {"access_token": self.token}
        json_datas = {
            "group_name": "GROUP_NAME_" + str(group_count),
            "tag": [{
                "name": "TAG_NAME_" + str(tag_count)
            }]
        }

        res = requests.post(url=url, params=params, json=json_datas)
        print("url:%s;params:%s;datas:%s" % (url, params, json_datas))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        tag_id = res.json()["tag_group"]["tag"][0]["id"]

        # del
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        params = {"access_token": self.token}
        json_datas = {
            "tag_id": [
                tag_id
            ]
        }

        res = requests.post(url=url, params=params, json=json_datas)
        print("url:%s;params:%s;datas:%s" % (url, params, json_datas))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

        # 调用get_corp_tag_list获删除后的tag信息，断言deleted字段
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        params = {
            "access_token": self.token
        }
        json_datas_1 = {
            "tag_id":
                [
                    tag_id
                ],
        }
        res = requests.post(url=url, params=params, json=json_datas_1)
        print("url:%s;params:%s;datas:%s" % (url, params, json_datas_1))
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        rsp = res.json()
        # 断言get_corp_tag_list获取到的deleted字段
        assert rsp["tag_group"][0]["deleted"] == True
