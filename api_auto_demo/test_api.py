#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : test_api.py
import json
import requests


class TestAPI:
    def setup_class(self):
        corpid = "XXXXXXXXXXX"
        corpsecret = "XXXXXXXXXXX"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        res = requests.get(url=url, params=params)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
        self.token = res.json()["access_token"]

    def test_get_corp_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        params = {
            "access_token": self.token
        }
        res = requests.post(url=url, params=params)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    def test_add_corp_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        params = {"access_token": self.token}
        json_datas = {
            "group_name": "GROUP_NAME",
            "tag": [{
                "name": "TAG_NAME_1",
                "order": 1
            }]
        }

        res = requests.post(url=url, params=params, json=json_datas)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))

    def test_del_corp_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        params = {"access_token": self.token}
        json_datas = {
            "tag_id": [
                "etjPoZCgAAAsRevEUFbGWlp-S6Gkvlgg"
            ]
        }

        res = requests.post(url=url, params=params, json=json_datas)
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
